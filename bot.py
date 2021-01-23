import discord
import requests
import json
# settings.py
from dotenv import load_dotenv
load_dotenv()
import os 
from nlp_analyze import get_sentiment_score 
import pymongo
from pymongo import MongoClient
import urllib
SECRET_KEY = os.getenv("token")
TENOR_KEY = os.getenv("tenorkey")


client = discord.Client()
mongo_uri = "mongodb+srv://qhackteam2021:" + urllib.parse.quote("Password@123") + "@mycluster.7ok43.mongodb.net/test"
cluster = MongoClient(mongo_uri)
# cluster = MongoClient("mongodb+srv://qhackteam2021:Password@123@mycluster.7ok43.mongodb.net/test")
db = cluster["mydatabase"]
collection = db["qhacks"]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(''):
        vals = message.content.split(" ")[1:]
        mood = get_sentiment_score(" ".join(vals))
        if mood < 0:
            search_term = "lol"
        else: 
            search_term = "sad"
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=1" % (search_term, TENOR_KEY))
        parsed = json.loads(r.content)
        good = parsed['results'][0]['media'][0]['tinygif']['url']
        
        # post = {"_id": message.author.id, "score": 1}
        # collection.insert_one(post)
        # await message.channel.send('accepted!')

        await message.channel.send(good)
        print(parsed['weburl'])
    


client.run(SECRET_KEY)