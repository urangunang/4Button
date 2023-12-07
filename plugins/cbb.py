from bot import Bot
from config import OWNER
from REA import Data
from pyrogram import filters
from pyrogram.errors import MessageNotModified
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, Message

@Bot.on_message(filters.private & filters.incoming & filters.command("order"))
async def _order(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        Data.ORDER.format(client.username, OWNER),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.inline_buttons("order")),
    )

@Bot.on_message(filters.private & filters.incoming & filters.command("help"))
async def _help(client: Bot, msg: Message):
    await client.send_message(
        msg.chat.id,
        "<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.inline_buttons("help")),
    )


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "order":
        try:
            await query.message.edit_text(
                text=Data.ORDER.format(client.username, OWNER),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.help_buttons),
            )
        except MessageNotModified:
            pass
    elif data == "help":
        try:
            await query.message.edit_text(
                text="<b>Cara Menggunakan Bot ini</b>\n" + Data.HELP,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Data.order_buttons),
            )
        except MessageNotModified:
            pass
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except BaseException:
            pass


    elif data == "toggle":
        # Toggle between order and help buttons
        current_state = "order" if "order" in query.message.text.lower() else "help"
        new_buttons = Data.inline_buttons("order" if current_state == "help" else "help")
        try:
            await query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(new_buttons))
        except MessageNotModified:
            pass
