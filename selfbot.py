import discord
from discord.ext import commands, tasks
import random
import sys
import json
import os
from data import GAMES_LIST, MUSIC_LIST

persona_type = sys.argv[1] if len(sys.argv) > 1 else "gamer"
account_name = sys.argv[2] if len(sys.argv) > 2 else "acc1"

config_file = "config.json"
if os.path.exists(config_file):
    with open(config_file, "r") as f:
        config = json.load(f)
else:
    config = {}

token_key = f"{account_name}_{persona_type}_token"

if token_key not in config or not config[token_key]:
    print(f"\n[!] No user token found for Account: '{account_name}' ({persona_type})")
    print("[WARNING] This script runs on a user account (Selfbot).")
    entered_token = input(f"Please paste the User Token for {account_name}: ").strip()
    config[token_key] = entered_token
    with open(config_file, "w") as f:
        json.dump(config, f, indent=4)
    print(f"[+] Token saved to {config_file}!\n")

token = config[token_key]

bot = commands.Bot(command_prefix="!", self_bot=True, help_command=None)

class HumanSelfbotPersona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.human_behavior_loop.start()

    def cog_unload(self):
        self.human_behavior_loop.cancel()

    @tasks.loop(minutes=2.0)
    async def human_behavior_loop(self):
        status_choices = [discord.Status.online, discord.Status.idle, discord.Status.dnd]
        chosen_status = random.choice(status_choices)

        # 10% chance to simulate going offline ("sleeping")
        if random.random() < 0.10:
            await self.bot.change_presence(status=discord.Status.offline, activity=None)
            return

        if persona_type == "gamer":
            game_name = random.choice(GAMES_LIST)
            activity = discord.Game(name=game_name)
            await self.bot.change_presence(status=chosen_status, activity=activity)
            
        elif persona_type == "music":
            song_name = random.choice(MUSIC_LIST)
            activity = discord.Activity(type=discord.ActivityType.listening, name=song_name)
            await self.bot.change_presence(status=chosen_status, activity=activity)

    @human_behavior_loop.before_loop
    async def before_printer(self):
        await self.bot.wait_until_ready()

@bot.event
async def on_ready():
    print(f"[SELFBOT - {account_name.upper()}] Logged in as {bot.user} ({persona_type} persona).")
    await bot.add_cog(HumanSelfbotPersona(bot))

@bot.command()
async def say(ctx, *, message: str = None):
    await ctx.message.delete()
    if message:
        await ctx.send(message)

try:
    bot.run(token, reconnect=True)
except Exception as e:
    print(f"[ERROR] Selfbot login failed: {e}")
