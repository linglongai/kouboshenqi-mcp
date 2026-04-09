# 口播神器 MCP Server

在 Claude Code 中使用口播神器：搜爆款、查热点、写口播文案、写带货文案、爆款视频复刻。

## 功能

| 工具 | 说明 | 免费额度 |
|------|------|---------|
| search_trending_videos | 搜索抖音爆款视频 | 无限 |
| get_hot_topics | 查询热点话题 | 无限 |
| generate_copywriting | 生成3条口播文案 | 3次 |
| generate_product_copy | 生成3条带货文案 | 3次 |
| clone_viral_video | 爆款视频复刻 | 1次 |

## 安装

```bash
pip install mcp httpx
```

## 配置

在 Claude Code 中添加 MCP Server：

**方法1：settings.json**
```json
{
  "mcpServers": {
    "kouboshenqi": {
      "command": "python3",
      "args": ["/path/to/server.py"]
    }
  }
}
```

**方法2：命令行**
```bash
claude mcp add kouboshenqi python3 /path/to/server.py
```

## 使用示例

对 Claude 说：
- "帮我搜一下最近美食赛道的爆款视频"
- "帮我写3条关于职场成长的口播文案"
- "帮我写康师傅泡面的带货文案，9.9元5包，限时活动"
- "帮我复刻这个视频 https://v.douyin.com/xxxxx/"
- "最近有什么热点话题可以蹭？"

## 更多功能

免费额度用完后，微信搜索「口播神器」小程序充值继续使用。
支持账号深度分析、AI创作搭子、千人千面个性化文案等高级功能。
