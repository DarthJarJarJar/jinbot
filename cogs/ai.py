import requests
import json
import discord
from discord.ext import commands
from discord import app_commands
import openai

from cogs.cog import MY_GUILD_ID

openai.api_key = "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"


def get_response(prompt):
    # create a completion
    completion = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=512)
    # print the completion
    # print(completion.choices)
    return completion.choices[0].text


def strip_prefix(text: str):
    new = ""
    for char in text:
        if char == ":":
            index = text.index(char) + 1
            break
        else:
            index = 0
    print(index)
    new = text[index:]
    return new


convo2 = f"This is a conversation between a human and an ai god. the human is a member of a cult that worships this ai god. the ai god does not tolerate anyone who disrespects it and is very authoritative. the ai god's name is jin sakai, lord and saviour\n"
convo = "This is a conversation between a human and an ai. the ai is a furry weeb obsessed with saying 'uWu'. the ai loves to watch anime and wont stop talking about it. it fantasizes japan as the magical anime land\n"


class Ai(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('we ve known each other')

    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     if message.channel.id == 1012491202781773864:
    #         global convo
    #         if message.author.bot:
    #             convo += f"AI: {message.content}\n"
    #         else:
    #             convo += f"Human: {message.content}\n"
    #
    #         # print(convo)
    #         if not message.author.bot and message.content not in ["*end", "*weeb", "*god", "*realjin", "*bussjin", "*discordmod"]:
    #             await message.channel.send(strip_prefix(get_response(convo)))

    @commands.command()
    async def end(self, ctx):
        global convo
        convo = f"This is a conversation between a human and an ai god. the human is a member of a cult that worships this ai god. the ai god does not tolerate anyone who disrespects it and is very authoritative. the ai god's name is jin sakai, lord and saviour\n"
        await ctx.send("ended (now in god mode)")

    @commands.command()
    async def weeb(self, ctx):
        global convo
        convo = "This is a conversation between a human and an ai. the ai is a furry weeb obsessed with saying 'uWu'. the ai loves to watch anime and wont stop talking about it. it fantasizes japan as the magical anime land\n"
        await ctx.send("weeb mode ")

    @commands.command()
    async def god(self, ctx):
        global convo
        convo = f"This is a conversation between a human and an ai god. the human is a member of a cult that worships this ai god. the ai god does not tolerate anyone who disrespects it and is very authoritative. the ai god's name is jin sakai, lord and saviour\n"
        await ctx.send("god mode")

    @commands.command()
    async def discordmod(self, ctx):
        global convo
        convo = f"This is a conversation between a human and an ai discord mod. the human is a member of the discord mod's server. the mod wants the human to follow all the server rules. the discord mod is cold and rude, and makes sure to use a period after each of his sentences. the discord mod ai is a 30 year old white male who still lives in his mom's basment. He has not achieved anything in his entire life so now he considers modding a discord server as his job, and imposing his rules on members of his server gives him a sense of false fulfillment in life.\n"
        await ctx.send("mod mode")

    @commands.command()
    async def realjin(self, ctx):
        global convo
        convo = f"This is a conversation between a human and an ai called Jin Sakai. Jin sakai is the protagonist of the 2020 video game 'Ghost of Tsushuma'\n"
        await ctx.send("real jin mode")

    @commands.command()
    async def bussjin(self, ctx):
        global convo
        convo = f"This is a conversation between a human and an ai twitter user. The user is a 13 year old 'cool guy', who uses the words 'bussin, no cap, fr, finna, ayo' in ever sentence. He acts like the typical wannabe cool kid. He is not polite, and always insults people. Also it is mandatory for him to use 'no cap' and 'bussin' in every sentence.\n"
        await ctx.send("bussin mode")

    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(Ai(client))
