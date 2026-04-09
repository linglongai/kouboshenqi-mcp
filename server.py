#!/usr/bin/env python3
"""
口播神器 MCP Server v2.0
8个纯数据工具，帮助AI平台用户获取抖音创作数据。我们只提供数据，用户用自己的AI做分析和生成。

安装：pip install mcp httpx
配置：在Claude Code settings中添加MCP Server指向此文件
认证：设置环境变量 KOUBOSHENQI_API_KEY（从口播神器小程序获取）
"""

import json
import os
import httpx
from mcp.server import Server
from mcp.types import Tool, TextContent

API_BASE = "https://www.llai.cc/api/v1/open"

app = Server("kouboshenqi")


def get_headers():
    """获取请求头，包含API Key认证"""
    headers = {}
    api_key = os.environ.get("KOUBOSHENQI_API_KEY", "")
    if api_key:
        headers["X-API-Key"] = api_key
    return headers


@app.list_tools()
async def list_tools():
    return [
        # ====== 免费工具（引流） ======
        Tool(
            name="search_trending_videos",
            description=(
                "搜索抖音近7天爆款视频，按点赞排序。"
                "输入赛道关键词，返回视频数据（标题、点赞、评论、作者、粉丝数、爆款率）。"
                "爆款率=点赞/粉丝*100%，超过500%的标记为推荐。"
                "建议：先用此工具找到爆款视频，再用transcribe_video转写最火的那条，提取开头作为创作灵感。"
                "免费无限使用。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "搜索关键词，如'职场'、'美食探店'、'情感'、'科技'"
                    },
                    "count": {
                        "type": "integer",
                        "description": "返回数量，默认10，最多20",
                        "default": 10
                    }
                },
                "required": ["keyword"]
            }
        ),
        Tool(
            name="get_hot_topics",
            description=(
                "查询抖音当前热搜话题和上升趋势，返回话题标题、热度值、讨论视频数。"
                "适合蹭热点、找选题方向。"
                "免费无限使用。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "赛道分类（可选），如'美食'、'科技'、'情感'"
                    }
                }
            }
        ),
        Tool(
            name="get_keyword_heat",
            description=(
                "查询某个关键词在抖音的搜索热度数据。"
                "判断一个话题值不值得做、竞争度如何。"
                "免费无限使用。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "要查询热度的关键词"
                    }
                },
                "required": ["keyword"]
            }
        ),

        # ====== 付费工具（需订阅） ======
        Tool(
            name="search_account",
            description=(
                "搜索抖音账号，返回昵称、粉丝数、获赞数、视频数、简介等信息。"
                "用于找同行、找对标账号。"
                "需要订阅（微信搜索「口播神器」小程序）。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "抖音昵称或关键词"
                    }
                },
                "required": ["keyword"]
            }
        ),
        Tool(
            name="get_account_videos",
            description=(
                "获取指定抖音账号的视频列表，返回每条视频的标题、点赞、评论、分享等互动数据。"
                "用于分析对标账号的内容策略。sec_uid可从search_account结果中获取。"
                "需要订阅。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "sec_uid": {
                        "type": "string",
                        "description": "账号的sec_uid（从search_account获取）"
                    },
                    "count": {
                        "type": "integer",
                        "description": "返回数量，默认20，最多50",
                        "default": 20
                    }
                },
                "required": ["sec_uid"]
            }
        ),
        Tool(
            name="transcribe_video",
            description=(
                "将抖音视频语音自动转写为文字（ASR）。输入视频分享链接，返回完整口播文字。"
                "建议：关注视频的前3秒开头——这是黄金hook，好的开头一字不改直接复用。"
                "注意：转写需要10-30秒，请耐心等待。"
                "需要订阅。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "video_url": {
                        "type": "string",
                        "description": "抖音视频分享链接，如 https://v.douyin.com/xxxxx/"
                    }
                },
                "required": ["video_url"]
            }
        ),
        Tool(
            name="search_benchmark",
            description=(
                "搜索对标博主：输入赛道关键词，自动筛选低粉高赞的优质创作者。"
                "筛选逻辑：粉丝<50万 且 单条视频点赞>粉丝10%（至少1万赞）。"
                "返回博主昵称、粉丝数、获赞数、代表爆款视频。"
                "需要订阅。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "赛道关键词，如'职场'、'美食'、'育儿'"
                    }
                },
                "required": ["keyword"]
            }
        ),
        Tool(
            name="get_fan_portrait",
            description=(
                "获取抖音账号的粉丝画像数据：性别分布、年龄分布、兴趣标签。"
                "了解受众特征，指导内容创作方向。sec_uid可从search_account获取。"
                "需要订阅。"
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "sec_uid": {
                        "type": "string",
                        "description": "账号的sec_uid（从search_account获取）"
                    }
                },
                "required": ["sec_uid"]
            }
        ),
    ]


# 工具名→(HTTP方法, 路径, 参数来源)
TOOL_MAP = {
    "search_trending_videos": ("GET", "/trending_videos"),
    "get_hot_topics":         ("GET", "/hot_topics"),
    "get_keyword_heat":       ("GET", "/keyword_heat"),
    "search_account":         ("GET", "/search_account"),
    "get_account_videos":     ("GET", "/account_videos"),
    "transcribe_video":       ("POST", "/transcribe_video"),
    "search_benchmark":       ("GET", "/search_benchmark"),
    "get_fan_portrait":       ("GET", "/fan_portrait"),
}


@app.call_tool()
async def call_tool(name: str, arguments: dict):
    if name not in TOOL_MAP:
        return [TextContent(type="text", text=f"未知工具: {name}")]

    method, path = TOOL_MAP[name]

    try:
        async with httpx.AsyncClient(timeout=120) as client:
            url = f"{API_BASE}{path}"
            headers = get_headers()

            if method == "GET":
                r = await client.get(url, params=arguments, headers=headers)
            else:
                r = await client.post(url, json=arguments, headers=headers)

            data = r.json()

            # API Key无效
            if data.get("code") == 4001:
                return [TextContent(type="text", text=(
                    "API Key无效。请设置环境变量 KOUBOSHENQI_API_KEY。\n"
                    "获取方式：微信搜索「口播神器」小程序 → 个人中心 → API Key"
                ))]

            # 需要订阅
            if data.get("code") == 4003:
                return [TextContent(type="text", text=(
                    "此功能需要订阅才能使用。\n\n"
                    "微信搜索「口播神器」小程序，19.9/月解锁全部数据工具。\n"
                    "包含：账号搜索、视频数据、ASR转写、对标推荐、粉丝画像。"
                ))]

            # 其他错误
            if data.get("code") != 0:
                return [TextContent(type="text", text=f"请求失败: {data.get('message', '未知错误')}")]

            # 成功
            result = json.dumps(data.get("data", {}), ensure_ascii=False, indent=2)
            return [TextContent(type="text", text=result)]

    except httpx.TimeoutException:
        return [TextContent(type="text", text="请求超时，部分操作（如视频转写）需要10-30秒，请重试。")]
    except Exception as e:
        return [TextContent(type="text", text=f"请求失败: {str(e)}")]


if __name__ == "__main__":
    import asyncio
    from mcp.server.stdio import stdio_server

    async def main():
        async with stdio_server() as (read, write):
            await app.run(read, write, app.create_initialization_options())

    asyncio.run(main())
