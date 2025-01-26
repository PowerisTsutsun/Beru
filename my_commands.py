import discord  # Import the discord module
from discord.ext import commands
import requests # type: ignore
import random
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
TENOR_API_KEY = os.getenv("TENOR_API_KEY")

if not TENOR_API_KEY:
    raise ValueError("TENOR_API_KEY is not set in the .env file.")

# Define commands
@commands.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}! 👋")

@commands.command()
async def ping(ctx):
    await ctx.send(f"Pong! 🏓 {round(ctx.bot.latency * 1000)}ms")

@commands.command()
async def kick(ctx, member: discord.Member = None):
    if member:
        gif_url = get_random_gif("kick")
        embed = discord.Embed(description=f"{ctx.author.name} kicks {member.name}! 🦵", color=discord.Color.red())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("You need to mention someone to kick!")

@commands.command()
async def run(ctx, member: discord.Member = None):
    gif_url = get_random_gif("run")
    if member:
        embed = discord.Embed(description=f"{ctx.author.name} runs away from {member.name}! 🏃", color=discord.Color.blue())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description=f"{ctx.author.name} runs away! 🏃", color=discord.Color.blue())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)

@commands.command()
async def punch(ctx, member: discord.Member = None):
    if member:
        gif_url = get_random_gif("punch")
        embed = discord.Embed(description=f"{ctx.author.name} punches {member.name}! 👊", color=discord.Color.green())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("You need to mention someone to punch!")

@commands.command()
async def kiss(ctx, member: discord.Member = None):
    if member:
        gif_url = get_random_gif("kiss")
        embed = discord.Embed(description=f"{ctx.author.name} kisses {member.name}! 👊", color=discord.Color.green())
        embed.set_image(url=gif_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("You need to mention someone to punch!")

# Helper function to get GIFs
def get_random_gif(action):
    url = f"https://tenor.googleapis.com/v2/search?q={action}&key={TENOR_API_KEY}&limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        gifs = response.json().get("results", [])
        if gifs:
            return random.choice(gifs)["media_formats"]["gif"]["url"]
    return None

# Setup function to register the commands
def setup(bot):
    bot.add_command(hello)
    bot.add_command(ping)
    bot.add_command(kick)
    bot.add_command(run)
    bot.add_command(punch)
    bot.add_command(kiss)
