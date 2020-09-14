from os import *
# .env
DISCORD_TOKEN={NzU1MDE1OTYwNzkyMDA2NjYx.X19JaA.giHZXR0Pb3Hx65lo6fYE8TGxXUA}


from discord import *
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.client

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


pip: install -U python-dotenv
python bot.py 
client.run()

