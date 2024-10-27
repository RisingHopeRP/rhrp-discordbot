import discord
from discord.ext import commands
import json

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)

@client.event
async def on_message(msg):
    print(msg.author," sent ", msg.content)
    if msg.content.startswith("!"):
        cmd=msg.content.replace("!","",1)
        cmdname=cmd.split(" ")[0]

        if cmdname=="welcome":
            embed = discord.Embed(
                title="Welcome",
                description="**Hello " + msg.author.mention + "!**  \n  \nWelcome to Rising Hope. I am your Phoenix API. We are currently under development, but let\'s get you started.",
                colour=discord.Colour.dark_red()
            )
            embed.set_author(name='Phoenix Specialists Division', icon_url="https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png")
            embed.set_thumbnail(url='https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png')
            embed.set_image(url='https://i.postimg.cc/zGzRjGdt/Untitled_design_(2).png')
            await msg.channel.send(embed=embed)

        if cmdname=="website":
            embed = discord.Embed(
                title="Website",
                description="If you are wanting to support us on our journey, don't be afraid to join us at the following links!  \n  \n**LINKS:**  \n[Documentation](https://rising-hope-rp.gitbook.io/rising-hope-rp-docs/)  \n[Tebex](https://risinghoperp.tebex.io/)",
                colour=discord.Colour.dark_red(),
            )
            embed.set_author(name='Phoenix Specialists Division', icon_url="https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png")
            embed.set_thumbnail(url='https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png')
            embed.set_image(url='https://i.postimg.cc/zGzRjGdt/Untitled_design_(2).png')
            await msg.channel.send(embed=embed)

        if cmdname=="commands":
            embed = discord.Embed(
                title="Commands",
                description="**The current commands that we have are !welcome, !website, and !channels at the moment with more to be added.**",
                colour=discord.Colour.dark_red()
            )
            embed.set_author(name='Phoenix Specialists Division', icon_url="https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png")
            embed.set_thumbnail(url='https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png')
            embed.set_image(url='https://i.postimg.cc/zGzRjGdt/Untitled_design_(2).png')
            await msg.channel.send(embed=embed)

        if cmdname=="verifyme":
            embed = discord.Embed(
                title = "Welcome to Rising Hope RP!",
                description = "After you have read the rules in the Server Docs, make sure to react to this message to allow for you to gain the roles for reading the rules!  \n  \nBe sure to follow the rules of the Discord as you are required to follow them at all times!",
                colour = discord.Colour.dark_red()
            )
            embed.set_author(name='Phoenix Specialists Division', icon_url="https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png")
            embed.set_thumbnail(url='https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png')
            embed.set_image(url='https://i.postimg.cc/zGzRjGdt/Untitled_design_(2).png')
            await msg.channel.send(embed=embed)

        if cmdname=="changelog":
            if msg.author.roles == { '@Developer' }:
                input = discord.ui.TextInput(

                )

                await input.callback()
                embed = discord.Embed(
                    title = 'New Changelog',
                    description = 'What\'s new:'
                )
                await msg.channel.send(embed.embed)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    embed = discord.Embed(
        title="Hello",
        description="Welcome to Rising Hope. I am your Phoenix API. We are currently under development, but let\'s get you started.",
        colour=discord.Colour.dark_red()
    )
    embed.set_author(name='Phoenix Specialists Division', icon_url="https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png")
    embed.set_thumbnail(url='https://i.postimg.cc/J79qCRsV/Rising-Hope-RP-1.png')
    embed.set_image(url='https://i.postimg.cc/zGzRjGdt/Untitled_design_(2).png')

    try:
        await member.send(embed=embed)
    except: pass
print("Connecting...")
client.run(json.load(open("auth.json"))["token"])
