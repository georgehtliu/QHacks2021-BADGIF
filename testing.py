import discord

token = """ODAyMzgxNDU0MTgwMjIwOTg4.YAuZ9g.oKaqTNTOdsiLosb7Fz3ttHzv6G4"""
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$gif'):
        vals = message.content.split("")
        await message.channel.send(vals)

client.run(token)