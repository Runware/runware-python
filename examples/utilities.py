"""
In your app: from runware import Runware
"""

import asyncio

from runware import Runware


async def main() -> None:
    async with Runware(transport="websocket") as client:
        results = await client.model_search({
            "search": "juggernaut XL",
            "category": "checkpoint",
            "limit": 5,
        })

        response = results[0]
        models = response.get("results", [])
        print(f"Found {len(models)} model(s):")
        for model in models:
            print(f"  {model.get('air')} — {model.get('name')}")


if __name__ == "__main__":
    asyncio.run(main())
