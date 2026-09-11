from flask import Flask
from threading import Thread
import discord
from discord import app_commands
import os

app = Flask('')

@app.route('/')
def home():
    return "Online"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    Thread(target=run, daemon=True).start()

keep_alive()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name="panel", description="Open Forge Hub Panel")
async def panel(interaction):
    embed = discord.Embed(
        description="This is **Forge Hub** Panel, Just click the Get Key and After redeeming your Key then Get the Script.",
        color=discord.Color.dark_theme()
    )
    view = discord.ui.View()
    btn1 = discord.ui.Button(
        label="Redeem Key",
        emoji="🔑",
        style=discord.ButtonStyle.green
    )
    btn2 = discord.ui.Button(
        label="Get Script",
        emoji="📜",
        style=discord.ButtonStyle.blurple
    )
    view.add_item(btn1)
    view.add_item(btn2)
    await interaction.response.send_message(embed=embed, view=view)

@client.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

client.run(os.getenv("BOT_TOKEN"))
