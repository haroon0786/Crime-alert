import logging
import threading
from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Replace with your bot token
TOKEN = "7784331408:AAE8kO3vj5hLMCKM9EkQJHrKg8V3tDx3lVw"

# Replace with actual URLs and Chat IDs
MAIN_CHANNEL_URL = "https://t.me/CYBERCRIMALERT"
CHAT_GROUP_URL = "https://t.me/CYBER_CRIM_CHAT"
ESCROW_GROUP_URL = "https://t.me/ESCROWES_VERIFIED"
OWNER_URL = "https://t.me/PARIVEJxOP"
DEVELOPER_URL = "https://t.me/JODxPREDATOR"
OWNER_CHAT_ID = "7028472133"  # Replace with numeric chat ID if needed

# --- Dummy Flask Web Server for Health Checks ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_flask():
    # Run the Flask server on port 8000, accessible externally.
    app.run(host="0.0.0.0", port=8000)

# --- Bot Command Handlers ---

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=MAIN_CHANNEL_URL),
            InlineKeyboardButton("ɢʀᴏᴜᴘ", url=CHAT_GROUP_URL),
            InlineKeyboardButton("ᴇꜱᴄʀᴏᴡ", url=ESCROW_GROUP_URL),
        ],
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", url=OWNER_URL),
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=DEVELOPER_URL),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "𝙃𝙚𝙡𝙡𝙤 𝙬𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙘𝙮𝙗𝙚𝙧 𝙘𝙧𝙞𝙢𝙚 𝙖𝙡𝙚𝙧𝙩 𝙗𝙤𝙩\n\n"
        "𝙬𝙚 𝙖𝙧𝙚 𝙝𝙚𝙧𝙚 𝙩𝙤 𝙚𝙭𝙥𝙤𝙨𝙚 𝙎𝙘𝙖𝙢𝙢𝙚𝙧𝙨.\n"
        "𝙄𝙛 𝙮𝙤𝙪 𝙜𝙤𝙩 𝙎𝙘𝙖𝙢𝙢𝙚𝙙, 𝙮𝙤𝙪 𝙘𝙖𝙣 𝙧𝙚𝙥𝙤𝙧𝙩 𝙝𝙚𝙧𝙚.\n\n"
        "𝙏𝙮𝙥𝙚 /report 𝙩𝙤 𝙧𝙚𝙥𝙤𝙧𝙩 𝙖 𝙨𝙘𝙖𝙢 𝙥𝙤𝙨𝙩\n"
        "𝙏𝙮𝙥𝙚 /submit 𝙩𝙤 𝙨𝙪𝙗𝙢𝙞𝙩 𝙖 𝙨𝙘𝙖𝙢 𝙧𝙚𝙥𝙤𝙧𝙩",
        reply_markup=reply_markup
    )

# /report and /form command
async def show_form(update: Update, context: ContextTypes.DEFAULT_TYPE):
    form_text = """🚨 𝘾𝙔𝘽𝙀𝙍 𝙍𝙄𝙈𝙀 𝘼𝙇𝙀𝙍𝙏 🚨

𝗦𝗖𝗔𝗠𝗠𝗘𝗥 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 𝗕𝗘𝗟𝗢𝗪 

𝗦𝗖𝗔𝗠𝗠𝗘𝗥 𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 ❌:-

𝗦𝗖𝗔𝗠𝗠𝗘𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞 ❌:- 

𝗦𝗖𝗔𝗠𝗠𝗘𝗥 𝗣𝗛𝗢𝗡𝗘 𝗡𝗨𝗠𝗕𝗘𝗥 ❌ :-

𝗦𝗖𝗔𝗠𝗠𝗘𝗥 𝗨𝗣𝗜 ❌:- 

𝗦𝗖𝗔𝗠 𝗔𝗠𝗢𝗨𝗡𝗧 ❌:- 

‼️ 𝗩𝗜𝗖𝗧𝗜𝗠 𝗦𝗧𝗔𝗧𝗘𝗠𝗘𝗡𝗧 :-

‼️ 𝗩𝗜𝗖𝗧𝗜𝗠 𝗨𝗦𝗦𝗘𝗥𝗡𝗔𝗠𝗘 :-

𝗡𝗢𝗧𝗘 - 𝗔𝗟𝗪𝗔𝗬𝗦 𝗗𝗢 𝗘𝗦𝗖𝗥𝗢𝗪, 𝗗𝗢𝗡'𝗧 𝗧𝗥𝗨𝗦𝗧 𝗕𝗟𝗜𝗡𝗗𝗟𝗬 ❌

❌FUCK HIM HARD GUYS❌

#𝗡𝗢𝗦𝗖𝗔𝗠𝗜𝗡𝗧𝗚 
#𝙎𝙃𝘼𝙍𝙀_𝙆𝘼𝙍𝙊_𝙈𝙄𝙏𝙍𝙊𝙉 
#𝗗𝗘𝗞𝗛𝗢_𝗠𝗔𝗧_𝗣𝗘𝗟𝗧𝗘_𝗥𝗔𝗛𝗢 

✅𝗧𝗢 𝗘𝗫𝗣𝗢𝗦𝗘 𝗦𝗖𝗔𝗠𝗠𝗘𝗥𝗦
@CYBERCRIMALERT ✅
@CYBERCRIMALERT ✅

♥️ 𝗧𝗛𝗔𝗡𝗞𝗦 𝗙𝗢𝗥 𝗦𝗨𝗣𝗣𝗢𝗥𝗧 ♥️

✅ 𝗘𝗦𝗖𝗥𝗢𝗪 𝗩𝗘𝗥𝗜𝗙𝗜𝗘𝗗 𝗨𝗦𝗘𝗥𝗦 -: @Escrowes_Verified ✅
@Escrowes_Verified ✅

❞𝙖𝙟 𝙠𝙖𝙧 𝙡𝙞𝙮𝙖 𝙝𝙤𝙩𝙖 𝙀𝙎𝘾𝙍𝙊𝙒 𝙨𝙚𝙡𝙡𝙚𝙧 𝙨𝙚

𝙩𝙤 𝙗𝙖𝙘𝙝 𝙟𝙖𝙩𝙚 𝙩𝙪𝙢 𝙨𝙘𝙖𝙢𝙢𝙚𝙧 𝙨𝙚"""
    await update.message.reply_text(form_text)

# /submit command
async def submit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        await context.bot.send_message(
            chat_id=OWNER_CHAT_ID,
            text=f"New report from @{update.message.from_user.username}:\n\n{update.message.reply_to_message.text}"
        )
        await update.message.reply_text("✅ Your report has been submitted to the owner!")
    else:
        await update.message.reply_text("⚠️ Please reply to the report message with /submit")

# --- Main Function ---
def main():
    # Start the dummy Flask server in a separate thread.
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    # Build the Telegram bot application.
    application = Application.builder().token(TOKEN).build()

    # Add command handlers.
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("report", show_form))
    application.add_handler(CommandHandler("form", show_form))
    application.add_handler(CommandHandler("submit", submit))

    # Start the bot (this call is blocking).
    application.run_polling()

if __name__ == '__main__':
    main()
