import httpx
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SENPAIMUSIC.utils.errors import capture_err 
from SENPAIMUSIC import app
from config import BOT_USERNAME

# Caption Text
start_txt = """<b>✨ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ <u>sᴛʀᴀɴɢᴇʀ ʀᴇᴘᴏs</u></b>

🚀 <b>ᴇᴀsʏ ᴅᴇᴘʟᴏʏ</b> –ᴏɴᴇ ᴄʟɪᴄᴋ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ  
🛡️ <b>ɴᴏ ʜᴇʀᴏᴋᴜ ᴏʀ ɪᴅ ʙᴀɴ ɪssᴜᴇs</b>  
🔋 <b>ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs</b> – ʀᴜɴ 24/7 ʟᴀɢɢ-ғʀᴇᴇ  
⚙️ <b>ғᴜʟʟʏ ғᴜɴᴄᴛɪᴏɴᴀʟ & ᴇʀʀᴏʀ-ғʀᴇᴇ</b>  

<i>ɴᴇᴇᴅ ʜᴇʟᴘ? sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴛᴏ ᴛʜᴇ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ!</i>"""

# Repo Command Handler
@app.on_message(filters.command("repo"))
async def repo_handler(_, msg):
    buttons = [
        [InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [
            InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/Senpai_support"),
            InlineKeyboardButton("👤 ᴏᴡɴᴇʀ", url="https://t.me/kiyoshi784"),
        ],
        [InlineKeyboardButton("🧾 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Senpai_music")],
        [
            InlineKeyboardButton("💥 ʙᴀɴᴀʟʟ", url="https://github.com/okamanx"),
            InlineKeyboardButton("🎧 ᴍᴜsɪᴄ V2", url="https://github.com/okamanx"),
        ],
        [
            InlineKeyboardButton("🎶 ᴍᴜsɪᴄ V1", url="https://github.com/okamanx"),
            InlineKeyboardButton("💬 ᴄʜᴀᴛʙᴏᴛ", url="https://github.com/okamanx"),
        ],
        [
            InlineKeyboardButton("🎯 sᴛʀɪɴɢ ɢᴇɴ", url="https://github.com/okamanx"),
            InlineKeyboardButton("🛠️ ɢᴄ ᴍᴀɴᴀɢᴇʀ", url="https://github.com/okamanx"),
        ],
        [
            InlineKeyboardButton("⚔️ sᴘᴀᴍ ʙᴏᴛs", url="https://github.com/okamanx"),
            InlineKeyboardButton("👾 ʙᴀɴᴀʟʟ 10", url="https://github.com/okamanx"),
        ],
        [
            InlineKeyboardButton("🧪 sᴛʀɪɴɢ ʜᴀᴄᴋ", url="https://github.com/okamax"),
            InlineKeyboardButton("🤖 ɪᴅ ᴜsᴇʀʙᴏᴛ", url="https://t.me/senpai_chats"),
        ],
        [InlineKeyboardButton("👑 sᴜᴘᴇʀ ᴜsᴇʀʙᴏᴛ", url="https://github.com/okamanx")]
    ]

    await msg.reply_photo(
        photo="https://files.catbox.moe/gx8rgz.png",
        caption=start_txt,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/okamanx/SENPAI-MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://github.com/okamanx/SENPAI-MUSIC) | [UPDATES](https://t.me/kiyoshi784)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


