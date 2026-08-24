# LLM-DailyDigest

Daily curated papers, open-source tools, and industry news in the LLM space — automated crawling, Chinese summaries, and topic/research aggregation.

🌐 **Website**: [https://dujh22.github.io/LLMDailyDigestWeb/](https://dujh22.github.io/LLMDailyDigestWeb/)
🔍 **Project analysis**: [deepwiki.com/dujh22/LLM-DailyDigest](https://deepwiki.com/dujh22/LLM-DailyDigest)

## 🏗️ Project Architecture

```
LLM-DailyDigest/
├── co_learner/          # Automation: crawlers + content agents (auto/briefing/info/content_agent)
├── tools/               # ArXiv download / batch translation / paper summarizer / scheduled scripts
├── backend/             # Message submission backend (Flask + LLM extraction)
├── content/             # Hugo content
│   ├── updates/         # Daily digests ([[items]] structured)
│   ├── topic/           # Topics (auto-aggregated)
│   ├── research/        # Research projects (auto-aggregated "Related Work")
│   ├── resources/       # Learning resources
│   └── posts/           # Project introductions
├── layouts/             # Layouts (updates/topic/research aggregation)
├── archetypes/          # Content templates
├── assets/              # Styles / brand logo
└── hugo.toml            # Config
```

## 🌐 Website Content System (Hugo + FixIt)

Content is organized along three dimensions. Structured fields drive **automatic linking** — no manual copying.

### Content Model

```
content/updates/<date>.md   Daily digest with multiple [[items]] (one message per item)
content/topic/<topic>.md     Topic page; auto-aggregates items that match this topic
content/research/<project>.md Research page; auto-aggregates items under this research ("Related Work")
```

### Item Fields (inside the daily digest front matter `+++`)

| Field                                   | Description                                                      |
| --------------------------------------- | ---------------------------------------------------------------- |
| `id`                                    | Anchor (deep-link from topic/research pages back to the digest)  |
| `title` `summary`                       | Title / one-line summary                                         |
| `subtopic`                              | Subtopic; determines which **section** on the topic page         |
| `topics`                                | Topic array; which **topic pages** this item appears on          |
| `research`                              | Research array; which **research pages** (can be empty)          |
| `source`                                | Source (WeChat account / arxiv category / site)                  |
| `paper` `code` `dataset` `link`         | Paper / code / dataset / original link (hidden if empty)         |
| `content` `purpose`                     | Body + purpose & takeaways (multi-line Markdown)                 |

> `topics` / `research` values must match **filenames** under `content/topic/` and `content/research/`.

### Dual Aggregation

- **Topic pages**: "Related Messages" at the bottom, grouped by `subtopic`.
- **Research pages**: "Related Work" at the bottom; header shows **proposer** and **earliest research date**.

Current research projects (proposer: Jinhua Du): LogicEvolve (2025-05), EvolveLRM (2026-01), HarnessEvolve / SwarmEvolve (2026-03), Groom (2026-05), Awesome-RSI (2026-06), DataEvolve / EvalEvolve (2026-08).

### Local Preview

```bash
hugo server --baseURL http://localhost:1313/ -D
```

## 🛠️ Message Submission Backend

`backend/` provides a local web form to enter a single message and append it to today's digest, with LLM field extraction from raw text. It also ships **batch entry** (`/batch/new`), **daily recommendation** (`/recommend`), **topic merge** (`/merge`), and **item dedup** (`/dedup`) pages.

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cp ../api_key.txt.example ../api_key.txt   # repo root; fill in key (gitignored)

python app.py          # → http://localhost:5050
```

> Default GLM gateway `https://api-gateway.glm.ai/v1`, model `gpt-5.6-sol`; override with `LLM_BASE_URL` / `LLM_MODEL`.

**Single submit**: paste raw text → "🔗 Resolve links" / "✨ LLM Extract" fills the form. Links to github / arxiv / HuggingFace / WeChat are **fetched automatically** and fed to the extractor; failed links can be supplemented manually (supplement text is used for extraction only, never written to `notes`). After review, "➕ Submit" appends one `[[items]]`. Keep `hugo server` running and refresh after submit.

**Batch entry** `/batch/new`: upload a txt or paste multiple entries (blank-line separated) → "Process all" runs link-fetch + LLM extraction concurrently (default 100 workers) → each item flows to `review / intervention` status; intervene only where a link failed to fetch, review and submit the rest. Items with unfetchable links skip the LLM call entirely. "⚡ Auto-process & submit" submits the whole batch in one click, skipping manual review (intervention items excluded; failures stay in review with reasons shown).

**Daily recommendation** `/recommend`: auto-collects the last 24h of research-relevant content, scores relevance with an LLM against each research project's profile (direction + scope from `content/research/*.md`), then imports selected items into the batch pipeline. WeChat channels are tiered with title-based dedup — optional real-time appmsg credentials → QbitAI official site (real-time) → [Wechat-Scholar](https://github.com/osnsyc/Wechat-Scholar) academic RSS fallback (≤12h latency) — plus arXiv (cs.CL/cs.AI/cs.LG, auto-widens to 48h/72h when the 24h window is empty). **Works with zero configuration.** Daily cache in `.recommend_cache/`; see `backend/README.md` for details.

**Topic merge** `/merge`: in a 3-level tree (topic ▸ subtopic ▸ article), select tags, enter a target name → preview impact → apply. Subtopics merge globally by string; rewrites are in-place for minimal diff and fully `git checkout`-reversible. Built-in "🤖 LLM suggestions" clusters near-duplicate tags; adopt singly or select several for batch apply.

**Item dedup** `/dedup`: detects duplicate items across the scan window (default 7 days back, up to 90) by normalized-URL matching on `paper`/`code`/`dataset`/`link` (tracking params stripped, arXiv abs/pdf/html unified). Each group keeps the **earliest** occurrence and absorbs the others' fields (fill empty URLs, union topics, append differing notes with a merge marker — never dropped); later duplicates are removed. Preview groups → apply selected / all / singly. Optional "🤖 LLM merge" rewrites summary/content/purpose into one coherent text per group (falls back to rule-based merge on failure). Every `/api/submit` auto-checks the last 7 days and **hard-blocks** same-link submissions with duplicate details shown (override via "allow duplicate"). See `backend/README.md`.

| Method | Path                                  | Description                                      |
| ------ | ------------------------------------- | ------------------------------------------------ |
| GET    | `/` `/batch/new` `/recommend` `/merge` `/dedup` | Single submit / batch / recommend / topic-merge / dedup pages |
| GET    | `/api/topics` `/api/research`         | Valid topics / research list                     |
| POST   | `/api/extract`                        | `{raw, extra?}` → link fetch + structured JSON   |
| POST   | `/api/submit`                         | Append item to today's digest (auto-create topics; same-link dup check over last 7 days, `allow_dup` to override) |
| POST   | `/api/batch/create` `/api/batch/<id>/process` | Create batch / concurrent processing    |
| POST   | `/api/batch/<id>/auto_submit`         | One-click auto-process & submit (skip review)    |
| GET/POST | `/api/recommend/status` `/api/recommend/collect` `/api/recommend/credentials` | Recommend status / collect / credentials |
| POST   | `/api/recommend/to_batch`             | Import selected candidates into a batch          |
| POST   | `/api/merge/preview_multi` `/api/merge/apply_multi` | Multi-group merge preview / batch apply |
| POST   | `/api/dedup/preview` `/api/dedup/apply` | Item-dedup scan / apply (`days` window, `groups` selection, `llm` smart merge) |

## 🚀 How to Use

```bash
git clone https://github.com/dujh22/LLM-DailyDigest.git
```

**Automation pipeline** (crawl → translate → digest):

```bash
cd co_learner && pip install -r requirements.txt
cp config.py config2.py        # edit config2.py with API keys

cd ../tools && pip install -r requirements.txt
python arx.py                  # download ArXiv papers
python arx_batch_to_ch.py      # batch translation
python paper_summarizer.py     # generate daily digest
# Generate a summary digest:
python paper_summarizer.py --data_file <csv> --date <YYYY-MM-DD> \
  --dairy_report_dir tools/summary --is_summary True
```

**Scheduled tasks**:

```bash
chmod +x tools/arx_dairy_summarizer_tmux.sh
./tools/arx_dairy_summarizer_tmux.sh
```

## 📅 Changelog

**2026-08-24**

- Item dedup `/dedup`: normalized-URL duplicate detection on paper/code/dataset/link (tracking params stripped, arXiv unified); keeps the earliest occurrence and absorbs fields, removes the rest; scan window default 7 days (up to 90); preview → apply selected / all / singly
- Dedup supports "🤖 LLM merge" of parsed fields: summary/content/purpose integrated into one coherent text per group (8-way concurrent, outside locks; auto-fallback to rule-based merge on failure)
- Submit-time auto-check: every `/api/submit` (incl. batch auto-submit) checks the last 7 days for same-link items and hard-blocks with duplicate details; "allow duplicate" override available

**2026-08-16**

- Daily recommendation `/recommend`: auto-collect last-24h research-relevant content (QbitAI official site + MachineHeart/NewZhiYuan via Wechat-Scholar academic RSS + optional real-time appmsg enhancement + arXiv 3 categories, title-deduped), LLM relevance scoring against research profiles, one-click import into the batch pipeline; zero-config ready
- Batch entry: "⚡ auto-process & submit" submits the whole batch skipping manual review (intervention items excluded)
- arXiv collection auto-widens 24h → 48h/72h on empty windows (announcement-batch lag)

**2026-08-12**

- Submission backend: auto-fetch body text from github/arxiv/HuggingFace/WeChat links in raw input; manual supplement for unfetchable links (extraction-only, never written to `notes`)
- Batch entry `/batch/new`: txt/paste with blank-line splitting, concurrent (default 100) fetch+extract, item status machine `review / intervention`
- Topic merge `/merge`: 3-level tree select + preview/apply, global subtopic merge, LLM suggestions with batch adopt; in-place rewrites for minimal diff

**2026-08-07**

- Homepage refresh: blue-purple tech theme, light/dark toggle, brand logo, nav/footer
- Structured digests: each message unified as `[[items]]` fields
- Topic/research dual aggregation: auto-join via `topics`/`research`, sections by `subtopic`
- Topic auto-expansion: LLM infers new topics; pages created on submit
- New "Research" section: 8 research projects (see above)
- Message submission backend: Flask form + LLM extraction

## 📞 Contact

- **GitHub**: [dujh22/LLM-DailyDigest](https://github.com/dujh22/LLM-DailyDigest)
- **Discussions**: [github.com/dujh22/LLM-DailyDigest/discussions](https://github.com/dujh22/LLM-DailyDigest/discussions)
- **Email**: dujh22@mails.tsinghua.edu.cn

## 📄 License

MIT. See [LICENSE](LICENSE).
