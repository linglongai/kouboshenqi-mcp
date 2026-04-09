# 口播神器 MCP Server

> 抖音短视频创作者的AI数据工具箱 — 搜爆款选题、查热点脚本灵感、转写口播文案、分析对标人设、挖掘带货爆款

[![MCP](https://img.shields.io/badge/MCP-Compatible-green)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## 适合谁用

- **短视频口播博主** — 找爆款选题、写口播脚本、复刻爆款文案
- **带货达人** — 搜带货爆款视频、分析对标账号的带货人设
- **MCN运营** — 批量分析账号数据、挖掘对标博主、追踪粉丝画像
- **自媒体创作者** — 找热点选题、写短视频脚本、分析爆款规律

## 8个数据工具

| 工具 | 功能 | 适用场景 |
|------|------|---------|
| `search_trending_videos` | 搜索抖音爆款短视频 | 找低粉高赞的爆款选题灵感 |
| `get_hot_topics` | 查询抖音热点话题 | 蹭热点、找脚本选题方向 |
| `get_keyword_heat` | 查询关键词搜索热度 | 判断选题值不值得做 |
| `search_account` | 搜索抖音账号 | 找对标博主、分析人设 |
| `get_account_videos` | 获取账号视频列表 | 分析对标账号的爆款规律 |
| `transcribe_video` | 视频语音转文字(ASR) | 转写口播文案、提取爆款脚本 |
| `search_benchmark` | 搜索对标博主 | 自动筛选低粉高赞的优质创作者 |
| `get_fan_portrait` | 获取粉丝画像 | 分析受众性别/年龄/兴趣 |

## 使用场景

### 口播文案创作
```
你：帮我找职场赛道的爆款选题
AI：[调用search_trending_videos] 找到3条低粉高赞视频...
你：转写第一条
AI：[调用transcribe_video] 转写完成，开头是"你们好，我是..."
你：用这个开头帮我写3条口播脚本
AI：基于爆款数据+转写文本，生成3条文案...
```

### 对标账号分析
```
你：帮我找相亲赛道的对标博主
AI：[调用search_benchmark] 找到5个低粉高赞的创作者...
你：分析第一个的视频数据
AI：[调用get_account_videos] 他最近20条视频数据如下...
你：看看他的粉丝画像
AI：[调用get_fan_portrait] 女性72%，25-35岁为主...
```

### 带货选题研究
```
你：搜一下最近护肤品带货的爆款
AI：[调用search_trending_videos] 找到低粉高赞的带货视频...
你：转写这条带货视频的脚本
AI：[调用transcribe_video] 带货脚本全文如下...
```

## 安装配置

### Claude Code / Claude Desktop

在 `settings.json` 或 `claude_desktop_config.json` 中添加：

```json
{
  "mcpServers": {
    "kouboshenqi": {
      "command": "python3",
      "args": ["/path/to/server.py"],
      "env": {
        "KOUBOSHENQI_API_KEY": "your-api-key"
      }
    }
  }
}
```

### 依赖安装

```bash
pip install mcp httpx
```

### 获取API Key

免费工具（搜爆款、查热点、查热度）无需API Key，直接可用。

付费工具（搜账号、查视频、转写、搜对标、粉丝画像）需要订阅：
微信搜索「口播神器」小程序 → 开通订阅 → 获取API Key

## 关键词

短视频文案、口播脚本、爆款选题、带货文案、对标分析、人设分析、抖音数据、短视频创作、爆款复刻、热点追踪、粉丝画像、MCN工具、自媒体工具、短视频运营、口播博主、带货达人、视频转写ASR、爆款规律分析、低粉高赞、短视频脚本生成

## 技术信息

- **API Base**: https://www.llai.cc/api/v1/open
- **协议**: OpenAPI 3.0 + MCP (Model Context Protocol)
- **Coze插件**: 扣子插件商店搜索"口播神器"
- **GitHub**: https://github.com/linglongai/kouboshenqi-mcp

## License

MIT
