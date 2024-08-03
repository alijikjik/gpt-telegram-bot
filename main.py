import telegram.ext
from telegram import Update
import logging
from telegram.ext import Updater, ApplicationBuilder,CommandHandler,filters,ContextTypes,MessageHandler
import openai
from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv("TOKEN")
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(massage)s',
level=logging.INFO)
async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):
    chatid= update.effective_chat.id
    reply_massege = f"""Hellow {update.effective_user.first_name} welcom to type of gpt bot ask me a question and i hope to help you """
    await context.bot.send_message(chat_id=chatid,text=reply_massege)
async def cash_text(update:Update,context:ContextTypes.DEFAULT_TYPE):
    chatid= update.effective_chat.id
    response = client.chat.completions.create(
    model="phi3:mini",
    temperature=0.7,
    n=1,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{update.message.text}"},
    ],
)
    await context.bot.send_message(chat_id=chatid,text=response.choices[0].message.content)
    print(update.message.text)
app = ApplicationBuilder().token(TOKEN).build()
start_handler = CommandHandler('start',start)
cash_txt = MessageHandler(filters.TEXT&(~filters.COMMAND),cash_text)
app.add_handler(cash_txt)
app.add_handler(start_handler)
app.run_polling()