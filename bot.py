import discord
import json

client = discord.Client()
@client.event
async def on_ready():
    print("Connected to Discord")

@client.event
async def on_message(msg):
    print(msg.author," sent ",msg.content)
    if msg.content.startswith("!"):
        cmd=msg.content.replace("!","",1)
        cmdname=cmd.split(" ")[0]
        print(cmdname)
        if cmdname=="intro":
            embed = discord.Embed(title="Welcome",description="**Hello "+msg.author.mention+"! Welcome to Alpha Base. This is the home of USAG Viper. Check out all the channels. One rule. DON'T BE A DICK.**", colour=discord.Colour.teal());
            await msg.channel.send(embed=embed)
        print(cmdname)
        if cmdname=="website":
            embed = discord.Embed(title="Website",description="**Error 404: Website Under Construction. Check with us soon.**", colour=discord.Colour.teal());
            await msg.channel.send(embed=embed)
        print(cmdname)
        if cmdname=="live":
            embed = discord.Embed(title="Live",description="**Hey "+msg.guild.default_role.mention+", I'm live on Twitch right now! https://www.twitch.tv/us_airsofting_and_gaming**", colour=discord.Colour.teal());
            await msg.channel.send(embed=embed)
        print(cmdname)
        if cmdname=="channel":
            embed = discord.Embed(title="Channels",description="**Hey "+msg.author.mention+", I'm on YouTube and Twitch! Youtube:https://www.youtube.com/channel/UCyH_IzCfV_Uh0_rD6w8UKYA Twitch: https://twitch.tv/us_airsofting_and_gaming**", colour=discord.Colour.teal());
            await msg.channel.send(embed=embed)
        print(cmdname)
        if cmdname=="commands":
            embed = discord.Embed(title="Commands",description="**The current commands that we have are !welcome, !website, and !channels at the moment with more to be added.**", colour=discord.Colour.teal());
            await msg.channel.send(embed=embed)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Hello",description="Welcome to Rising Hope. I am your Phoenix API. We are currently under development, but let\'s get you started.", colour=discord.Colour.teal());
    try:
        await member.send(embed=embed)
    except: pass
print("Connecting...")
client.run(json.load(open("auth.json"))["token"])
