# 提交工具后端（本地）

交互式填写单条消息，追加到当日日报；支持 LLM 从原始文本自动抽取结构化字段。

## 安装

```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

## 配置 API Key（必需，用于 LLM 抽取）

在**仓库根目录**（不是 backend/）创建 `api_key.txt`，填入 GLM/OpenAI 兼容 api_key：

```bash
cp ../api_key.txt.example ../api_key.txt
# 然后编辑 ../api_key.txt 写入你的 key
```

> `api_key.txt` 已被 `.gitignore` 忽略，**不会上传 git**。缺失时启动会提示，且 `/api/extract` 不可用（表单手动填写仍可用）。

LLM 默认走 `https://api-gateway.glm.ai/v1`、模型 `gpt-5.6-sol`，可用环境变量覆盖：

```bash
export LLM_BASE_URL="https://api-gateway.glm.ai/v1"
export LLM_MODEL="gpt-5.6-sol"
```

## 运行

```bash
python app.py
# → http://localhost:5050
```

建议同时开 `hugo server --baseURL http://localhost:1313/ -D`；每次提交后刷新即可在日报页看到新条目。

## 工作流

1. （可选）粘原始信息 → 「✨ LLM 抽取」自动填表
2. 核对字段，选好「主题」与「子主题」
3. 「➕ 提交」→ 追加一条 `[[items]]` 到 `content/updates/<当日>.md` 的 front matter

## 接口

| 方法 | 路径 | 说明 |
| --- | --- | --- |
| GET | `/` | 表单页 |
| GET | `/api/topics` | 合法主题列表 |
| POST | `/api/extract` | `{raw}` → 结构化字段 JSON |
| POST | `/api/submit` | 提交 item，追加到当日日报 |
