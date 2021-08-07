from userbot import *
from LuciferBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ℓυcιғεя υsεя"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

aura = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={aura})"


PM_IMG = "https://telegra.ph/file/73373552e9217e010e853.jpg"
pm_caption ="**ℓυcιғεя x ιs σηℓιηε**\n\n"

pm_caption += f"**┏━━━━━━━━━━━━━┓**\n"
pm_caption += f"**┣★ мαsтεя : {mention}**\n"
pm_caption += f"**┣★ тεℓεтнση : `{version.__version__}`**\n"
pm_caption += f"**┣★ ℓυcιғεявσт : {Luciferversion}**\n"
pm_caption += f"**┣★ sυ∂σ       : `{sudou}`**\n"
pm_caption += f"**┣★ cнαηηεℓ   : [Join Here](https://t.me/LuciferXUpdates)**\n"
pm_caption += f"**┣★ cяεαтεя    : [Lucifer Here](https://t.me/Murat_30_God)**\n"
pm_caption += f"**┗━━━━━━━━━━━━━┛**\n"

pm_caption += "    [✨REPO✨](https://github.com/kaal0408/Lucifer-X) 🔹 [📜License📜](https://github.com/kaal0408/Lucifer-X/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'awake', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_info(
  'Zinda Hai Kya Bro?'
).add()
