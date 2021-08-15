import asyncio

from Lucifer.utils import admin_cmd


@Lucifer.on(admin_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.01
    animation_ttl = range(0, 288)
    input_str = event.pattern_match.group(1)
    if input_str == "dev":
        await event.edit(input_str)
        animation_chars = [
            "M_ ____",
            "MD ____",
            "MD N___",
            "MD NO__",
            "MD NOO_",
            "MD NOOR",
            "**ANOTHER ONE**",
            "M______ _____",
            "MA_____ _____",
            "MAN____ _____",
            "MANJ___ _____",
            "MANJE__ _____",
            "MANJEE_ _____",
            "MANJEET _____",
            "MANJEET S____",
            "MANJEET SI___" "MANJEET SIN___" "MANJEET SING_" "MANJEET SINGH" "**AND**",
            "D_____",
            "DI____",
            "DIP___",
            "DIPE__",
            "DIPES_",
            "DIPESH",
            "MD NOOR MANJEET SINGH DIPESH THESE ARE MY PERU DEV",
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 72])
