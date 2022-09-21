import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

STRBUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Add Me To Group 💞", url=f"http://t.me/MutyalaHarshith?startgroup=true")],
                                [InlineKeyboardButton(text="🥳 Channel", url=f"https://t.me/MutyalaHarshith"),
                                 InlineKeyboardButton(text="🤪 Support", url=f"https://t.me/MHGCHAT")],
                                [InlineKeyboardButton(text="😂 Help", callback_data='help'),
                                 InlineKeyboardButton(text="😜 About", callback_data='about')]])

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="😎 Channel", url=f"https://t.me/MutyalaHarshith")],
                                [InlineKeyboardButton(text="🤞 HoME", callback_data='help'),
                                 InlineKeyboardButton(text="🎉 about", callback_data='about'),
                                 InlineKeyboardButton(text="🤩 Group", url=f"http://t.me/MHGcHaT")]])


START_TEXT = """ Hai Dude 😎 {}

I can JsoN From Files And About Yourself Via Text or file I will send to you

For More Help click /help 

[Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)
"""


HELP_TEXT = """**💞 Hᴏᴡ ᴛᴏ Usᴇ 💞**
I ᴄᴀɴ ʜᴇʟᴘ ᴄᴀɴ Fᴇᴛᴄʜ ɪᴅ ᴏғ ʏᴏᴜ
Jsᴏɴ ғɪʟᴇs ᴏғ ʏᴏᴜʀsᴇʟғ
Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ
Cʟɪᴄᴋ /JsoN ᴏғ ᴛᴏ ɢᴇᴛ 👇👇

• Usᴇʀɴᴀᴍᴇ ᴏғ ʏᴏᴜ
• Jsᴏɴ ғɪʟᴇs ᴏғ ʏᴏᴜʀsᴇʟғ

[Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)
"""


ABOUT_TEXT = """**Aʙᴏᴜᴛ Mysᴇʟғ**
• **Bᴏᴛ ɴᴀᴍᴇ:** JsoN Bot
• **Cʀᴇᴀᴛᴏʀ :** [Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/Develoveper)
• **GɪᴛHᴜʙ** : [Fᴏʟʟᴏᴡ](https://GitHub.com/HAIAMH)
• **Sᴏᴜʀᴄᴇ** : [JsoN](https://github.com/HAIAMH/JsoN)
• **Sᴜᴘᴘᴏʀᴛ** : [ᴍʜɢᴄʜᴀᴛ](https://t.me/MHGcHaT)
• **Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 𝟹](https://python.org)
• **Lɪʙʀᴀʀʏ :** [Pʏʀᴏɢʀᴀᴍ ᴠ𝟷.𝟸.𝟶](https://pyrogram.org)
• **Sᴇʀᴠᴇʀ :** [Hᴇʀᴏᴋᴜ](https://heroku.com)"""

@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=STRBUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(update.from_user.mention),
        reply_markup=STRBUTTONS
    )



@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

@Bot.on_message(filters.command(["json", 'mhjs', 'showjson']))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        pk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝙲𝙻𝙾𝚂𝙴",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_text(f"<code>{the_real_message}</code>", reply_markup=pk, quote=True)
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝙲𝙻𝙾𝚂𝙴",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )            
        os.remove("json.text")

print("✨✨ Start BoT By Created HAIAMH✨✨")
Bot.run()
