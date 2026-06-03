"""
In your app: from runware import Runware
"""

import asyncio

from runware import Runware


async def main() -> None:
    # REST transport — no connect()/disconnect() needed; each request is a
    # standalone HTTP call.
    async with Runware(transport_type="rest") as client:
        # Curated model AIR → the SDK auto-resolves the taskType.
        # No taskType needed in params.
        images = await client.run({
            "model": "runware:400@1",  # Flux 2 Dev
            "positivePrompt": "A beautiful sunset over the ocean",
            "width": 1024,
            "height": 1024,
            "numberResults": 2,
        })

        for image in images:
            print(image.get("imageURL"))


if __name__ == "__main__":
    asyncio.run(main())
