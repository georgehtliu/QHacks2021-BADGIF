import discord
import requests
import json
# settings.py
from dotenv import load_dotenv
load_dotenv()

import os 
SECRET_KEY = os.getenv("token")
TENOR_KEY = os.getenv("tenorkey")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gif'):
        vals = message.content.split(" ")[1:]
        if vals[0] == "dog":
            search_term = "LOL"
        elif vals[0] == "im":
            search_term = "bye"
        else: 
            search_term = vals[0]
        r = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=1" % (search_term, TENOR_KEY))
        parsed = json.loads(r.content)
        good = parsed['results'][0]['media'][0]['tinygif']['url']
        await message.channel.send(good)
        print(parsed['weburl'])
    


client.run(SECRET_KEY)