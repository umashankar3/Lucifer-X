import os

from Lucifer import ALIVE_NAME, CUSTOM_PMPERMIT, bot
from Lucifer.LuciferConfig import Var

fuk_uid = bot.uid
HELP_PIC = "https://telegra.ph/file/73373552e9217e010e853.jpg"
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
LUCIFERPIC = (
    PMPERMIT_PIC
    if PMPERMIT_PIC
    else "https://telegra.ph/file/73373552e9217e010e853.jpg"
)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
myid = bot.uid
mybot = Var.TG_BOT_USER_NAME_BF_HER
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Var.PRIVATE_GROUP_ID
MESAG = (
    str(CUSTOM_PMPERMIT)
    if CUSTOM_PMPERMIT
    else "`𝚈𝙾𝙾 𝙷𝙴𝚁𝙴 𝙸𝚂 L U C I F E R 𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈! 𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃 𝚃𝙸𝙻𝙻 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙰𝙿𝙿𝚁𝙾𝚅𝙴. 🤓"
)
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Lucifer User"
USER_BOT_WARN_ZERO = "`𝙸 𝙷𝙰𝚅𝙴 𝚆𝙰𝚁𝙽𝙴𝙳 𝚈𝙾𝚄 𝙽𝙾𝚃 𝚃𝙾 𝚂𝙿𝙰𝙼 😑😑. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙱𝙴𝙴𝙽 𝙱𝙻𝙾𝙲𝙺𝙴𝙳 𝙰𝙽𝙳 𝚁𝙴𝙿𝙾𝚁𝚃𝙴𝙳 𝚄𝙽𝚃𝙸𝙻 𝙵𝚄𝚃𝚄𝚁𝙴 𝙽𝙾𝚃𝙸𝙲𝙴.`\n\n**GoodBye!** "

if Var.LOAD_MYBOT == "True":
    USER_BOT_NO_WARN = (
        "**𝙷𝙴𝚈 𝚃𝙷𝙸𝚂 𝙸𝚂 L U C I F E R 𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 !!! 𝙷𝙴𝚁𝙴 𝚃𝙾 𝙿𝚁𝙾𝚃𝙴𝙲𝚃 [{}](tg://user?id={})**\n\n"
        "{}\n\n"
        "𝙵𝙾𝚁 𝚄𝚁𝙶𝙴𝙽𝚃 𝙷𝙴𝙻𝙿, 𝙿𝙼 𝚅𝙸𝙰 {}"
        "\n𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙷𝙾𝙾𝚂𝙴 𝚆𝙷𝚈 𝚈𝙾𝚄 𝙰𝚁𝙴 𝙷𝙴𝚁𝙴, 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 𝙾𝙿𝚃𝙸𝙾𝙽\n\n".format(
            DEFAULTUSER, myid, MESAG, botname
        )
    )
elif Var.LOAD_MYBOT == "False":
    USER_BOT_NO_WARN = (
        "**𝙿𝙼 𝚂𝙴𝙲𝚄𝚁𝙸𝚃𝚈 𝙾𝙵 [{}](tg://user?id={})**\n\n"
        "{}\n"
        "\n𝙿𝙻𝙴𝙰𝚂𝙴 𝙲𝙷𝙾𝙾𝚂𝙴 𝚆𝙷𝚈 𝚈𝙾𝚄 𝙰𝚁𝙴 𝙷𝙴𝚁𝙴, 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙰𝚅𝙰𝙸𝙻𝙰𝙱𝙻𝙴 𝙾𝙿𝚃𝙸𝙾𝙽\n".format(
            DEFAULTUSER, myid, MESAG
        )
    )

CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "✨")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))

if Config.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Hellow"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© Lucifer Help",
                text="{}\ncυяяєηт ρłυgıηs of lucifer υsєяъ๏т: {}".format(
                    query, len(CMD_LIST)
                ),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**lucifer Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n© @Lucifer_support_group ™",
                buttons=[
                    [custom.Button.inline("Stats📊", data="statcheck")],
                    [
                        Button.url(
                            "Repository ✨", "https://github.com/kaal0408/Lucifer-X"
                        )
                    ],
                    [
                        Button.url(
                            "Deploy Lucifer🌌",
                            "https://heroku.com/deploy?template=https://github.com/kaal0408/Lucifer-X",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query == "alive":
            ALIVE = ALV_TXT
            if ALIVE_PIC and ALIVE_PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    ALIVE_PIC,
                    text=ALIVE,
                    buttons=[
                        [
                            Button.url(
                                "Lucifer ᴄʜᴀɴɴᴇʟ", "https://t.me/LuciferXupdates"
                            ),
                            Button.url(
                                "Lucifer sᴜᴘᴘ๏ʀᴛ", "https://t.me/Lucifer_support_group"
                            ),
                        ],
                        [Button.inline("༼•ᴀʙᴏᴜᴛ ᴍʏ  ᴍᴀsᴛᴇʀ•༽", data="master")],
                    ],
                )
            else:
                result = builder.document(
                    text=ALIVE,
                    title="Lucifer-X",
                    file=ALIVE_PIC,
                    buttons=[
                        [
                            Button.url(
                                "Lucifer ᴄʜᴀɴɴᴇʟ", "https://t.me/LuciferXupdates"
                            ),
                            Button.url(
                                "Lucifer sᴜᴘᴘ๏ʀᴛ", "https://t.me/Lucifer_support_group"
                            ),
                        ],
                        [Button.inline("༼•ᴀʙᴏᴜᴛ ᴍʏ  ᴍᴀsᴛᴇʀ•༽", data="master")],
                    ],
                )

        elif event.query.user_id == bot.uid and query.startswith("__knock"):
            LUCIFERBT = USER_BOT_NO_WARN.format(DEFAULTUSER, myid, MESAG)
            result = builder.photo(
                file=LUCIFER_PIC,
                text=LUCIFERBT,
                buttons=[
                    [
                        custom.Button.inline("To Request 😓", data="req"),
                        custom.Button.inline("To Ask❔", data="ask"),
                    ],
                    [
                        custom.Button.inline("For Chatting💬", data="chat"),
                        custom.Button.inline("Something else😶", data="elsi"),
                    ],
                    [custom.Button.inline("What is this❓", data="wht")],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"lucifer - Telegram Userbot.",
                buttons=[
                    [
                        Button.url(
                            "Repository ✨", "https://github.com/kaal0408/Lucifer-X"
                        ),
                        Button.url(
                            "Deploy Lucifer🌌",
                            "https://heroku.com/deploy?template=https://github.com/kaal0408/Lucifer-X",
                        ),
                    ],
                    [Button.url("Support✌️", "https://t.me/Lucifer_support_group")],
                ],
            )
        else:
            result = builder.article(
                "Source Code",
                text="**Welcome to Lucifer υsєяъ๏т**\n\nClick below buttons for more",
                buttons=[
                    [custom.Button.url("Creator👀", "https://t.me/Murat_30_God")],
                    [
                        custom.Button.url(
                            "💾Source Code", "https://github.com/kaal0408/Lucifer-X"
                        ),
                        custom.Button.url(
                            "Deploy🌌",
                            "https://heroku.com/deploy?template=https://github.com/kaal0408/Lucifer-X",
                        ),
                    ],
                    [
                        custom.Button.url(
                            "Updates and Support Group↗️",
                            "https://t.me/Lucifer_support_group",
                        )
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Hey you.🙄 Create Your Own ƛsτʀ๏ υsєяъ๏т Don't touch mine😒"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wht")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "Don't you know what is this🙄?"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"This is the PM Security for {DEFAULTUSER} ✨ To Protect My Master From Scammers And those Who want  to disturb my Master.. PROTECTION IS ON BY [ASTRO_USERBOT](https://t.me/Astro_UserBot).\n If You also wanted to have That Deoloy Astro-Userbot Get Help from [Astro_HelpChat](https://t.me/Astro_HelpChat)"
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"reopen")))
    async def megic(event):
        if event.query.user_id == bot.uid:
            buttons = paginate_help(0, CMD_LIST, "helpme")
            await event.edit("Menu main Opened-Again🍁", buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Hey you.🙄 Get Your Own ƛsτʀ๏ υsєяъ๏т Don't touch mine🙂!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"req")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = (
                "Is it joke🙄You wanna to request your self\nthis is not for you"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"Oki👀You have something to request to {DEFAULTUSER}\nIf {DEFAULTUSER} knows He will glad to help you😊\nDon't Spam wait till he somes🙂"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) is **requesting** something in PM!\nSee what he wants to request 👀!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chat")))
    async def on_pm_click(event):
        event.query.user_id
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = (
                "You wanna to chat your self😆\nThis is not for you Master"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"You wanna to chat👀💬\nOki My master is offline now. if {DEFAULTUSER} will be in mood of chatting he will talk to you😊\nDon't Spam wait till he somes🙂"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you for **Random Chatting**!\nIf you are in mood of chatting You can talk to him👀!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ask")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = (
                "😆 What are you going to ask yourself\n This is not for you Master"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"👀What you want to ask to {DEFAULTUSER} ? Leave Your queies in Single Line\nDon't Spam wait till he somes🙂"
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            tosend = f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to **ASK Something** in PM🤔check his DM👀I told him to leave your message!\ngo and Check🙃!"
            await tgbot.send_message(LOG_GP, tosend)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"elsi")))
    async def on_pm_click(event):
        if event.query.user_id == bot.uid:
            reply_pop_up_alert = "what are u doing 🥴This is not for u"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(
                f"😶ok..!You have something else For my {DEFAULTUSER} \nNow wait...! My master is offline NoW🥴When he will come he will Reply\nDon't Spam till wait he comes 🙂."
            )
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            ok = event.query.user_id
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            first_name = html.escape(target.user.first_name)
            await tgbot.send_message(
                LOG_GP,
                f"Hey {DEFAULTUSER}, [{first_name}](tg://user?id={ok}) wants to PM you\nHE HAVE **Something Else** For u😲\nGo and check..",
            )

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "Menu Closed!!🍂", buttons=[Button.inline("Re-open Menu", data="reopen")]
            )
        else:
            reply_pop_up_alert = (
                "Hey you.🙄 Get Your Own Lucifer υsєяъ๏т Don't touch mine🙂 "
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = astrostats
        await event.answer(text, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"master")))
    async def ok(event):
        text = masterinfo
        await event.answer(text, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  # pylint:disable=E0602
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = (
                "Hey you.🙄 Get Your Own Lucifer υsєяъ๏т Don't touch mine🙂!"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"Commands Available in {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} has no detailed info.\nUse .help {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n Use .unload {} to remove this plugin\n\
                © Lucifer UserBot".format(
                plugin_name
            )
            if len(help_string) >= 140:
                oops = "Commands List is Big😓Check Your Saved Message Commands list is Forwarded There🙃!"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\nThis will be auto-deleted in 2 minute!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("me", help_string)
                    await asyncio.sleep(120)
                    await ok.delete()
            else:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = (
                "Hey you.🙄 Create Your Own Lucifer υsєяъ๏т Don't touch mine😒"
            )
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = HELP_ROWS
    number_of_cols = HELP_COLOUMNS
    tele = CUSTOM_HELP_EMOJI
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline("{} {}".format(tele, x), data="us_plugin_{}".format(x))
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⊰≾•ρяєѵıσυs", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("⎝⎝cłσsє⎠⎠", data="close"),
                custom.Button.inline(
                    "ηєxт•≳⊱", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
