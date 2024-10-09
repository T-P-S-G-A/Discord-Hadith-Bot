import discord
import random
import asyncio

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

client = discord.Client(intents=intents)

Discord_Channel_ID = 0000000000000000000 #Replace this with your Discord Channel ID
discord_token = "YOUR_DISCORD_BOT_TOKEN_HERE" #Replace the token with your Discord Bot token -> It needs to be a string
Role_ID = 0000000000000000000 #Replace this with your Discord Role ID

def get_random_hadith():
    with open("hadiths.txt", "r", encoding="utf-8") as file:
        hadiths = file.readlines()
    return random.choice(hadiths).strip()  # Choosing Random lines from hadiths.txt while removing whitespaces

async def send_hadith_message():
    channel = client.get_channel(Discord_Channel_ID)
    if channel is None:
        print("Error: Channel not found")
        return

    while not client.is_closed():
        print(f"Attempting to send message to channel {channel.name} (ID: {channel.id})...")
        hadith = get_random_hadith()
        await channel.send(f"<@&{Role_ID}> Hadith of the day: \n" + hadith) #Role_ID pings the desired discord
        print("Message sent successfully.")
        
        # waiting for 12 hours before sending the next hadith in the channel
        await asyncio.sleep(43200)
        print("Waiting 12 hours")

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')  # Print debug message when the bot is ready
    await send_hadith_message()

@client.event
async def on_connect():
    print("Bot connected to Discord.")

@client.event
async def on_disconnect():
    print("Bot disconnected from Discord.")

client.run(discord_token)
