"""
In your app: from runware import Runware
"""

import asyncio

from runware import Runware


async def main() -> None:
    async with Runware(transport_type="websocket") as client:
        # Community / fine-tune models live outside the curated registry, so
        # the SDK can't auto-resolve the taskType from the model AIR. Pass
        # `taskType` explicitly.
        loose = await client.run({
            "taskType": "imageInference",
            "model": "civitai:133005@782002",
            "positivePrompt": "A beautiful sunset over the ocean",
            "width": 1024,
            "height": 1024,
        })
        print("Result:", loose[0])


if __name__ == "__main__":
    asyncio.run(main())
