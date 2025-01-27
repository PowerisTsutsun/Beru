import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import my_commands  # Import the renamed commands file

# Load environment variables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Load commands from the external file
my_commands.setup(bot)

# Run the bot
bot.run(TOKEN)
