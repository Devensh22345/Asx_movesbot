#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>𝗔𝗱𝘂𝗹𝘁 𝗔𝗻𝗶𝗺𝗲 𝗶𝗻 𝗵𝗶𝗻𝗱𝗶 [𝟭𝟴+] 👇👇👇 https://t.me/FileStore_Robot?start=Z2V0LTM5NjQ0MDcwNTc3MjU1ODM </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
