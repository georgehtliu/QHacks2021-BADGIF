import discord
import requests
import json
import random
# settings.py
from dotenv import load_dotenv
import os 
from nlp_analyze import get_sentiment_score 
from scrape_word import get_random_happy_word
# load
load_dotenv()
client = discord.Client()
# Env vars
SECRET_KEY = os.getenv("token")
TENOR_KEY = os.getenv("tenorkey")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(''):
        vals = message.content.split(" ")
        mood = get_sentiment_score(" ".join(vals))
        author = message.author
        timestamp = message.created_at
        channel = message.channel.id
        if mood < 0:
            search_term = get_random_happy_word()
        else: 
            search_term = "sad"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=1" % (search_term, TENOR_KEY))
        parsed = json.loads(r.content)
        good = parsed['results'][0]['media'][0]['tinygif']['url']
        await message.channel.send(good)
        await message.channel.send(search_term)
        await message.channel.send("%s %s %s %s" % (author, mood, timestamp, channel))
        # savetodb(author, mood, timestamp, channel)

client.run(SECRET_KEY)