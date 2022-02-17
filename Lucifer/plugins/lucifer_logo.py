import os
import random

from PIL import Image, ImageDraw, ImageFont
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos

from . import *

PICS_STR = []


@bot.on(admin_cmd(pattern=r"logo ?(.*)"))
@bot.on(sudo_cmd(pattern=r"logo ?(.*)", allow_sudo=True))
async def lg1(Luciferevent):
    event = await eor(Luciferevent, "Processing.....")
    fnt = await get_font_file(Luciferevent.client, "@umashankar3")
    if Luciferevent.reply_to_msg_id:
        rply = await Luciferevent.get_reply_message()
        logo_ = await rply.download_media()
    else:
        async for i in bot.iter_messages(
            "@LuciferXlogos", filter=InputMessagesFilterPhotos
        ):
            PICS_STR.append(i)
        pic = random.choice(PICS_STR)
        logo_ = await pic.download_media()
    text = Luciferevent.pattern_match.group(1)
    if len(text) <= 8:
        font_size_ = 150
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 130
        strik = 20
    if not text:
        await eod(event, "**Give some text to make a logo !!**")
        return
    img = Image.open(logo_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(fnt, font_size_)
    image_widthz, image_heightz = img.size
    w, h = draw.textsize(text, font=font)
    h += int(h * 0.21)
    image_width, image_height = img.size
    draw.text(
        ((image_width - w) / 2, (image_height - h) / 2),
        text,
        font=font,
        fill=(255, 255, 255),
    )
    w_ = (image_width - w) / 2
    h_ = (image_height - h) / 2
    draw.text(
        (w_, h_), text, font=font, fill="white", stroke_width=strik, stroke_fill="black"
    )
    file_name = "LuciferBot.png"
    img.save(file_name, "png")
    await bot.send_file(
        Luciferevent.chat_id,
        file_name,
        caption=f"**Made By**: [GROUP](t.me/shayari_jok)",
    )
    await event.delete()
    try:
        os.remove(file_name)
        os.remove(fnt)
        os.remove(logo_)
    except:
        pass


async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None,
    )
    font_file_message = random.choice(font_file_message_s)

    return await client.download_media(font_file_message)
