import os
from random import choice, random
from flask import Flask, request
from paebot import Paebot


app = Flask(__name__)

bot = Paebot(os.getenv("BOT_TOKEN"))
bot.api("setWebhook", url="https://example.com/")


@app.post("/")
def handler():
    bot.handle(request.get_json())
    return "OK"


@bot.command("/start")
@bot.command("/help")
def start(update, chat_id, args):
    bot.api("sendMessage", chat_id=chat_id, text="Hi, I'm a bot!")


@bot.command("/cats")
def random_cat(update, chat_id, args):
    bot.api("sendPhoto", chat_id=chat_id, photo=f"https://cataas.com/cat?{random()}")


@bot.command("/roll")
def roll(update, chat_id, args):
    bot.api("sendMessage", chat_id=chat_id, text=choice(list(set(args)) or "🙄"))


# long polling
if __name__ == "__main__":
    try:
        bot.api("deleteWebhook")
        bot.run(timeout=42)
    except KeyboardInterrupt:
        exit()
