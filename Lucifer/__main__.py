import glob
import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from Lucifer import CMD_HNDLR, bot
from Lucifer.LuciferConfig import Var
from Lucifer.thunderconfig import Config
from Lucifer.utils import load_assistant, load_module

TELE = Var.PRIVATE_GROUP_ID
BOTNAME = Var.TG_BOT_USER_NAME_BF_HER
LOAD_MYBOT = Var.LOAD_MYBOT
sed = logging.getLogger("Lucifer UserBot")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def startup_log_all_done():
    try:
        await bot.send_message(
            TELE,
            f"**Lucifer has been deployed.\nSend** `{CMD_HNDLR}alive` **to see if the bot is working.\n\nAdd** @{BOTNAME} **to this group and make it admin for enabling all the features of userbot**",
        )
    except BaseException:
        print("Either PRIVATE_GROUP_ID is wrong or you have left the group.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN_BF_HER", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished, no errors")
        print("Starting Userbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("Startup Completed")
    else:
        bot.start()

path = "Lucifer/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:

            load_module(shortname.replace(".py", ""))
        except Exception:
            pass
print("Lucifer  has been deployed! ")

print("Setting up Lucifer")


if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "Lucifer/plugins/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:

                load_assistant(shortname.replace(".py", ""))
            except Exception:
                pass
    sed.info("Lucifer Has Been Deployed Successfully !")
    sed.info("╔════❰ Ⲃⲟⲧ Ⲓⲛϝⲟʀⲙⲁⲧⲓⲟⲛ ❱═❍⊱❁۪۪")
    sed.info("║┣⪼ Ⲟⲱⲛⲉʀ - Ƒմʂʂìօղ ᴜꜱᴇʀ ")
    sed.info("║┣⪼ Ⲋⲧⲁⲧυⲋ - Ⲟⲛⳑⲓⲛⲉ")
    sed.info("║┣⪼ Ⲃⲟⲧ Ⳳⲉʀⲋⲓⲟⲛ - 1.2.0")
    sed.info("║┣⪼ Ⳙⲣⲧⲓⲙⲉ - 00h:00m:4s ")
    sed.info("║┣⪼ Ⲃⲟⲧ Ⲣⲓⲛⳋ - 0.006")
    sed.info("║┣⪼ Ⲣⲩⲧⲏⲟⲛ - 3.9.2")
    sed.info("║┣⪼ Ⲧⲉⳑⲉⲧⲏⲟⲛ - 1.17.0 ")
    sed.info("║┣⪼ ✨Lucifer ✨")
    sed.info("║╰━━━━━━━━━━━━━━━➣ ")
    sed.info("╚══════════════════❍⊱❁۪۪")
else:
    sed.info("Lucifer Has Been Installed Sucessfully !")
    sed.info("You Can Visit @Lucifer_support_group For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
