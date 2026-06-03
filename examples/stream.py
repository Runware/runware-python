"""
In your app: from runware import Runware
"""

import asyncio
import sys

from runware import Runware, StreamOptions


async def main() -> None:
    async with Runware() as client:
        # Cancel the stream if it takes too long.
        cancel = asyncio.Event()

        async def cancel_after(seconds: float) -> None:
            await asyncio.sleep(seconds)
            cancel.set()

        timer = asyncio.create_task(cancel_after(30.0))

        try:
            text_stream = await client.stream(
                {
                    "model": "google:gemma@4-31b",
                    "messages": [
                        {
                            "role": "user",
                            "content": "Write a 200-word short story about a lighthouse keeper.",
                        }
                    ],
                },
                StreamOptions(cancel_event=cancel),
            )

            async for chunk in text_stream.text_stream:
                sys.stdout.write(chunk)
                sys.stdout.flush()

            result = await text_stream.result()
            print(f"\n\nFinish reason: {result.finish_reason}")
        finally:
            timer.cancel()


if __name__ == "__main__":
    asyncio.run(main())
