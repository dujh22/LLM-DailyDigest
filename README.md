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

`backend/` provides a local web form to enter a single message and append it to today's digest, with LLM field extraction from raw text.

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

cp ../api_key.txt.example ../api_key.txt   # repo root; fill in key (gitignored)

python app.py          # → http://localhost:5050
```

> Default GLM gateway `https://api-gateway.glm.ai/v1`, model `gpt-5.6-sol`; override with `LLM_BASE_URL` / `LLM_MODEL`.

**Workflow**: paste raw text → "✨ LLM Extract" fills the form (recommended topics/research, up to 3 new topic candidates) → pick topics (can add manually; pages are created on submit) and research → "➕ Submit" appends one `[[items]]`. Keep `hugo server` running and refresh after submit.

| Method | Path                                  | Description                                      |
| ------ | ------------------------------------- | ------------------------------------------------ |
| GET    | `/` `/api/topics` `/api/research`     | Form page / valid topics / research list         |
| POST   | `/api/extract`                        | `{raw}` → structured field JSON                  |
| POST   | `/api/submit`                         | Append item to today's digest (auto-create topics) |

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
