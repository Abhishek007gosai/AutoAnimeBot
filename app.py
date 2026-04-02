import os
from flask import Flask
from threading import Thread
from pyrogram import Client

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

class Bot(Client):
    def __init__(self):
        super().__init__(
            "my_bot",
            api_id=int(os.getenv("API_ID")),
            api_hash=os.getenv("API_HASH"),
            bot_token=os.getenv("BOT_TOKEN")
        )

def run_web():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

def run_bot():
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    Thread(target=run_web).start()
    run_bot()
