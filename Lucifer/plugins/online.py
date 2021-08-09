# Copyright Lion
# For @LuciferHelp coded by @xditya
# Kangers keep credits else I'll take down 🧐

import random
import sys

from telethon import version

from Lucifer import ALIVE_NAME
from Lucifer.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer User"

ONLINESTR = [
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ \n█░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░█  █░║║║╠─║─║─║║║║║╠─░█ \n█░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░█ \n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ \n\n**Lucifer  online.**\n\n**All systems functioning normally !** \n\n**Bot by** [Team Lucifer](tg://user?id=804329190) \n\n**More help -** @LuciferXUpdates \n\n           [🚧 GitHub Repository 🚧](https://github.com/kaal0408/Lucifer-X)",
    f"╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗\n║║║╠─║─║─║║║║║╠─\n╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝\n              **Welcome to Lucifer**\n\n**Hey master! I'm alive. All systems online and functioning normally ✅**\n\n**✔️ Telethon version:** `{version.__version__}` \n\n**✔️ Python:** `{sys.version}` \n\n✔️ More info: @LuciferXUpdates \n\n✔️ Created by: [Team Lucifer](tg://user?id804329190=) \n\n**✔️ Database status:** All ok 👌 \n\n**✔️ My master:** {DEFAULTUSER} \n\n        [🌟 Github repository 🌟](https://github.com/kaal0408/Lucifer-X)",
]


@Lucifer.on(admin_cmd(outgoing=True, pattern="online"))
@Lucifer.on(sudo_cmd(allow_sudo=True, pattern="online"))
async def online(event):
    """ Greet everyone! """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await eor(event, random.choice(ONLINESTR))
