"""recommend.py 离线冒烟测试（monkeypatch 网络，不访问外网、不写 content/）。
运行：python3.12 tools/test_recommend_smoke.py
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
import recommend as R  # noqa: E402

# ---------- 1) 公众号采集：monkeypatch appmsg ----------
now = time.time()
page = {"base_resp": {"ret": 0}, "app_msg_list": [
    {"title": "<b>新文章A</b>", "link": "https://mp.weixin.qq.com/s/A",
     "digest": "摘要A", "create_time": int(now) - 3600},
    {"title": "新文章B", "link": "https://mp.weixin.qq.com/s/B",
     "digest": "", "create_time": int(now) - 7200},
    {"title": "旧文章", "link": "https://mp.weixin.qq.com/s/old",
     "digest": "", "create_time": int(now) - 90000},
]}
calls = []


def fake_appmsg(cred, fakeid, begin, count):
    calls.append((fakeid, begin))
    return 0, page["app_msg_list"], page


R._appmsg_request = fake_appmsg
res = R.collect_wechat({"cookie": "x", "token": "1"}, int(now) - 86400)
assert len(res["items"]) == 6, len(res["items"])   # 3 个号 × 2 条新
assert res["items"][0]["title"] == "新文章A"
assert len(calls) == 3, calls                       # 未满 10 条 → 每号 1 页即停
print("wechat collect ok:", len(res["items"]), "items,", len(calls), "requests")


def bad_appmsg(cred, fakeid, begin, count):
    return 2000, [], {"base_resp": {"ret": 2000}}


R._appmsg_request = bad_appmsg
res = R.collect_wechat({"cookie": "x", "token": "1"}, int(now) - 86400)
assert res["items"] == [] and all(e.get("credentials_expired") for e in res["errors"])
print("wechat expired-cred path ok:", res["errors"][0]["error"])

# ---------- 2) arXiv：伪造 Atom XML，同 id 去重 ----------
atom = """<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
<entry><id>http://arxiv.org/abs/2408.11111v2</id><title>Paper  One</title>
<summary>  About\n self-improvement. </summary><published>2026-08-15T00:00:00Z</published></entry>
<entry><id>http://arxiv.org/abs/2408.11111v2</id><title>Dup</title><summary>x</summary></entry>
<entry><id>http://arxiv.org/abs/2408.22222v1</id><title>Paper Two</title><summary>y</summary></entry>
</feed>
"""


class FakeResp:
    text = atom

    def raise_for_status(self):
        pass


R._get = lambda url, params=None, headers=None: FakeResp()
from datetime import datetime, timedelta, timezone  # noqa: E402

res = R.collect_arxiv(datetime.now(timezone.utc) - timedelta(hours=24))
assert len(res["items"]) == 2
assert res["items"][0]["key"] == "https://arxiv.org/abs/2408.11111"
assert res["items"][0]["summary"] == "About self-improvement."
print("arxiv collect+dedup ok:", [i["key"] for i in res["items"]])

# ---------- 3) 研究画像 ----------
prof = R.build_research_profile()
n_files = len(list(Path(R.RESEARCH_DIR).glob("*.md")))
assert len(prof) == n_files, [p["name"] for p in prof]
bad = [p["name"] for p in prof if not p["direction"] or not p["scope"]]
assert not bad, f"研究页缺「> 研究方向：」或「## 研究范畴」: {bad}"
ev = next(p for p in prof if p["name"] == "EvolveLLM")
assert "自我进化" in ev["direction"] and ev["scope"]
print("research profile ok:", len(prof), "projects")

# ---------- 4) LLM 筛选：monkeypatch，一个 chunk 抛异常 ----------
cands = [{"key": f"k{i}", "source": "arXiv", "title": f"t{i}",
          "summary": "s", "link": f"l{i}"} for i in range(3)]


def fake_chunk(profile, chunk, api_key):
    if any(c["title"] == "t1" for c in chunk):
        raise RuntimeError("LLM down")
    out = {}
    for c in chunk:
        if c["title"] == "t0":
            out[c["_i"]] = {"relevant": True, "research": ["EvolveLLM"], "reason": "匹配"}
        elif c["title"] == "t2":
            out[c["_i"]] = {"relevant": False, "research": [], "reason": "无关"}
    return out


R._filter_chunk = fake_chunk
R.FILTER_CHUNK = 1  # 每条一个 chunk，才能真正验证「单 chunk 失败不影响其他条」
R.filter_relevance(cands, api_key="fake-key")
assert cands[0]["relevant"] is True and cands[0]["research"] == ["EvolveLLM"]
assert cands[1]["relevant"] is None
assert cands[2]["relevant"] is False
print("filter partial-failure ok:", [(c["title"], c["relevant"]) for c in cands])

# ---------- 5) 量子位官网采集：伪造首页 + 正文页 meta ----------
homepage = """
<a href="https://www.qbitai.com/2026/08/473001.html">新文章标题足够长可以入选</a>
<a href="https://www.qbitai.com/2026/08/473001.html">新文章标题足够长可以入选</a>
<a href="https://www.qbitai.com/2026/08/473002.html">旧文章标题足够长会被时间过滤掉</a>
<a href="https://www.qbitai.com/2026/08/473003.html">短</a>
"""


class FakeResp2:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass


# 新文章时间相对当前动态生成，避免测试随日期推移过期
_fresh = datetime.now().astimezone() - timedelta(hours=1)
PAGES = {
    "https://www.qbitai.com/": FakeResp2(homepage),
    "https://www.qbitai.com/2026/08/473001.html": FakeResp2(
        f'<span class="date">{_fresh:%Y-%m-%d}</span><span class="time">{_fresh:%H:%M}</span>'
        '<meta property="og:description" content="  这是 摘要。 ">'),
    "https://www.qbitai.com/2026/08/473002.html": FakeResp2(
        '<span class="date">2020-01-01</span>'),
    "https://www.qbitai.com/2026/08/473003.html": FakeResp2("no meta"),
}
R._get = lambda url, params=None, headers=None: PAGES[url]
res = R.collect_qbitai(datetime.now(timezone.utc) - timedelta(hours=24))
assert len(res["items"]) == 1, res["items"]
assert res["items"][0]["summary"] == "这是 摘要。"
assert res["items"][0]["published"].startswith(f"{_fresh:%Y-%m-%d}"), res["items"][0]
print("qbitai collect ok:", res["items"][0]["title"], res["items"][0]["published"])

# 标题归一化去重辅助
assert R._norm_title("AI 发布！重磅") == R._norm_title("ai 发布 重磅")
print("title norm ok")

# ---------- 6) Wechat-Scholar RSS 采集：伪造 RSS 2.0 ----------
import email.utils as _eu
_now = datetime.now(timezone.utc)
rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel><title>t</title>
<item><title>新鲜文章标题</title><link>http://mp.weixin.qq.com/s?__biz=new</link>
<pubDate>{_eu.format_datetime(_now)}</pubDate></item>
<item><title>陈旧文章标题</title><link>http://mp.weixin.qq.com/s?__biz=old</link>
<pubDate>{_eu.format_datetime(_now - timedelta(days=3))}</pubDate></item>
<item><title>无日期文章标题</title><link>http://mp.weixin.qq.com/s?__biz=nodate</link></item>
</channel></rss>
"""


class FakeResp3:
    def __init__(self, text):
        self.text = text

    def raise_for_status(self):
        pass


_saved_feeds = dict(R.WECHAT_SCHOLAR_FEEDS)
R.WECHAT_SCHOLAR_FEEDS = {"测试号": "https://example.com/feed.xml"}
R._get = lambda url, params=None, headers=None: FakeResp3(rss)
res = R.collect_wechat_scholar(datetime.now(timezone.utc) - timedelta(hours=24))
R.WECHAT_SCHOLAR_FEEDS = _saved_feeds
assert len(res["items"]) == 2, res["items"]  # 新鲜 + 无日期（保留），旧的被过滤
assert res["items"][0]["source"] == "测试号"
assert res["items"][0]["link"].startswith("http://mp.weixin.qq.com/")
print("wechat-scholar rss ok:", [i["title"] for i in res["items"]])

print("ALL OFFLINE SMOKE TESTS PASSED")
