import discord
import requests
import json
import random

# settings.py
from dotenv import load_dotenv
import os
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from discord.ext import commands
from nlp_analyze import get_sentiment_score 
from nlp_analyze import get_entity_link
from scrape_word import get_random_happy_word, get_random_sad_word
import pymongo
from pymongo import MongoClient
import urllib
import uuid
plt.style.use('seaborn-darkgrid')
# load
load_dotenv()
# Env vars
SECRET_KEY = os.getenv("token")
TENOR_KEY = os.getenv("tenorkey")

client = discord.Client()
mongo_uri = "mongodb+srv://qhackteam2021:" + urllib.parse.quote("Password@123") + "@mycluster.7ok43.mongodb.net/test"
cluster = MongoClient(mongo_uri)
# cluster = MongoClient("mongodb+srv://qhackteam2021:Password@123@mycluster.7ok43.mongodb.net/test")
db = cluster["mydatabase"]
collection = db["qhacks"]

bot = commands.Bot(command_prefix='$')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)
    pass

@bot.command()
async def plot(self, ctx, xvals, yvals):
    await ctx.send(xvals)
    

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$data'):
        tag = message.author.name + "_" + message.author.discriminator
        timestamps = [x['timestamp'].strftime("%H:%M:%S") for x in collection.find() if tag==x['username']]
        moods = [x['mood'] for x in collection.find() if tag==x['username']]
        xList = timestamps
        yList = moods
        # xList.sort()
        # yList.sort()
        x = np.array(xList)
        y = np.array(yList)
        # x_r = np.round(x, 3)
        # y_r = np.round(y, 2)
        await message.channel.send(x)
        await message.channel.send(y)
        plt.clf()
        plt.plot(x, y)
        plt.gcf().autofmt_xdate()
        plt.ylim(-1.0,1.0)
        plt.title(f'{message.author}\'s Graph')
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        tick_frequency = round(len(x)/10)+1
        ax = plt.gca()
        ax.set_xticks(ax.get_xticks()[::tick_frequency])
        plt.savefig(fname='plot')
        await message.channel.send(file=discord.File('plot.png'))
        os.remove('plot.png')
    else:
        vals = message.content.split(" ")
        mood = get_sentiment_score(" ".join(vals))
        ent_link = get_entity_link(" ".join(vals))
        timestamp = message.created_at
        server = message.guild.id
        channel = message.channel.id
        wikiSent = False
        tag = message.author.name + "_" + message.author.discriminator

        # Save info
        post = {"_id": uuid.uuid4(), "username": tag, "message": message.content, "mood": mood, "timestamp": timestamp, "server": server, "channel": channel}
        collection.insert_one(post)
        if randint(0,10) == 5:
            try:
                await message.channel.send(ent_link)
                wikiSent = not wikiSent
            except:
                print("wiki not found")
        if mood < 0:
            search_term = get_random_happy_word()
        else: 
            search_term = "fortnitedance"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=1" % (search_term, TENOR_KEY))
        parsed = json.loads(r.content)
        good = parsed['results'][0]['media'][0]['tinygif']['url']
        if not wikiSent:
            await message.channel.send(good)

client.run(SECRET_KEY)