#!/usr/bin/env python3
"""
Example Python script that shows how to use edge-tts as a module
"""

import asyncio
import tempfile

from playsound import playsound

import edge_tts


async def main():
    """
    Main function
    """
    communicate = edge_tts.Communicate()
    ask = input("What do you want TTS to say? ")
    with tempfile.NamedTemporaryFile() as temporary_file:
        async for i in communicate.run(ask):
            if i[2] is not None:
                temporary_file.write(i[2])
        playsound(temporary_file.name)


if __name__ == "__main__":
    # Fix for "RuntimeError: Event loop is closed" on Windows
    # and Python 3.8+
    if (
        os.name == "nt"
        and sys.version_info >= (3, 8)
        and hasattr(asyncio, "WindowsSelectorEventLoopPolicy")
    ):
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
