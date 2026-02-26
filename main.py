import discord
from discord.ext import commands
import os
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Free Fire Glory Bot 24/7 Online! 🔥"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user} GLORY BOT LIVE! 🏆')

@bot.command()
async def glory(ctx, points: int = 10):
    await ctx.send(f"🏆 **{ctx.author.display_name}** ko **{points} GLORY POINTS** mile! 💎")

@bot.command()
async def leaderboard(ctx):
    await ctx.send("🏆 **TOP 5 GLORY KINGS:**\n1. BooyahMaster - 5000\n2. HeadshotKing - 4500\n3. ProGamer - 4200")

@bot.command()
async def helpme(ctx):
    await ctx.send("**Commands:** `!glory 50` `!leaderboard` `!helpme`")

Thread(target=run_flask).start()
bot.run(os.getenv('MTQ3NjI5MjE1Mjg2OTkxMjY3Ng.Gy2ifG.8K5El6rUQuvWDW8MNvacL09LJaGvFMh7w5q124'))
