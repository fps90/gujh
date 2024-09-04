from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import BANNED_USERS
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils.database import set_loop
from YukkiMusic.utils.decorators import AdminRightsCheck

STOP_COMMAND = get_command("STOP_COMMAND")

@app.on_message(
    filters.command(
        [
            "stop","ايقاف","end"
        ],""
    )
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    await Yukki.stop_stream(chat_id)     
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("مسح", callback_data="delete_message")]
    ])
    
    delete_message = await app.send_message(chat_id, _["admin_9"], reply_markup=keyboard)
    await message.delete()

@app.on_callback_query(filters.regex("delete_message"))
async def on_delete_button_pressed(cli, callback_query):
    await callback_query.message.delete()