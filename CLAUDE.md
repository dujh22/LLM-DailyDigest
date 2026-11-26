# LLM-DailyDigest 项目约定（AI 必读）

## 研究页人类专属栏目

`content/research/*.md` 中的「## 自研洞察」「## 自研经验」两个栏目（整个小节：从标题到下一个 `##` 标题，含 `human-only` 标记）**只允许人类手动修改**：

- AI 不得擅自新增、修改、删除其中内容，也不得删除或改动其标记；确需修改必须**先询问人类并获得明确同意**。
- 已有防护：后端写研究页时逐字比对（`backend/research_sections.human_violations`），Claude Code 中由 `.claude/hooks/guard_research_human.py` 在改动前强制弹窗询问；栏目内如需小标题请用 `###` 及以下。
- 「## 研究经验」栏目由日报整备自动维护（`backend/app.py` → `refresh_research_experiences`），可正常修改。

格式与新增研究流程见 `README_新增研究.md`。
