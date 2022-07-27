import discord
from discord import app_commands
from discord.ext import commands
from pymongo import MongoClient
import os
import urllib.parse
guild_id = 826766972204744764
MY_GUILD_ID = discord.Object(guild_id)

username = urllib.parse.quote_plus(os.environ["MONGODB_USERNAME"])
password = urllib.parse.quote_plus(os.environ["MONGODB_PASS"])

cluster = MongoClient(
    'mongodb+srv://%s:%s@cluster0.u6uh4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority' % (username, password))

level = ["Bronze", "Silver 1", "Silver 2", "Silver 3", "Gold 1", "Gold 2", "Gold 3", "Platinum"]
levelnum = [5, 25, 50, 75, 100, 150, 200, 300]

levelling = cluster["discord"]["levelling"]


class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna let you down')

    @commands.Cog.listener()
    async def on_message(self, message):
        suslist = ["sus", "sussy"]
        for word in suslist:
            if message.content.lower() == word:
                await message.channel.send(
                    "Is this a possible remark with a hidden connection to the video game Among Us (2018) developed by InnerSloth LLC which has gained recent popularity?")

        if " sussy " in message.content.lower():
            await message.channel.send(
                "Is this a possible remark with a hidden connection to the video game Among Us (2018) developed by InnerSloth LLC which has gained recent popularity?")
        if ' sus ' in message.content.lower():
            await message.channel.send(
                "Is this a possible remark with a hidden connection to the video game Among Us (2018) developed by InnerSloth LLC which has gained recent popularity?")
        stats = levelling.find_one({"id": message.author.id})
        if not message.author.bot:
            if stats is None:
                newuser = {"id": message.author.id, "xp": 0, "credit": 0}
                levelling.insert_one(newuser)
            else:
                xp = stats["xp"] + 1
                levelling.update_one({"id": message.author.id}, {"$set": {"xp": xp}})

                lvl = 0
                if xp == 250:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Bronze 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Bronze 1!")

                elif xp == 500:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Bronze 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Bronze 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Bronze 2!")
                if xp == 1250:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Bronze 3"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Bronze 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Bronze 3!")
                elif xp == 2500:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Silver 1"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Bronze 3"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Silver 1!")
                elif xp == 5000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Silver 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Silver 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Silver 2!")
                elif xp == 7500:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Silver 3"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Silver 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Silver 3!")
                elif xp == 10000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Gold 1"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Silver 3"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Gold 1!")
                elif xp == 15000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Gold 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Gold 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Gold 2!")
                elif xp == 20000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Gold 3"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Gold 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Gold 3!")
                elif xp == 30000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Platinum"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Gold 3"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Platinum!")
                elif xp == 100000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Plat 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Platinum"))
                    await message.channel.send(f"{message.author.mention} has levelled up to Plat 2!")

    # ssssssssssss
    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def xp(self, ctx):
        stats = levelling.find_one({"id": ctx.author.id})
        xp = stats["xp"]
        if xp < 250:
            usrlevel = "No Level"
        elif xp > 1250 and xp < 2500:
            usrlevel = "Bronze 3"
        elif xp > 500 and xp < 1250:
            usrlevel = "Bronze 2"
        elif xp > 250 and xp < 500:
            usrlevel = "Bronze 1"

        elif xp > 2500 and xp < 5000:
            usrlevel = "Silver 1"
        elif xp > 5000 and xp < 7500:
            usrlevel = "Silver 2"
        elif xp > 5000 and xp < 7500:
            usrlevel = "Silver 2"
        elif xp > 7500 and xp < 10000:
            usrlevel = "Silver 3"
        elif xp > 10000 and xp < 15000:
            usrlevel = "Gold 1"
        elif xp > 15000 and xp < 20000:
            usrlevel = "Gold 2"
        elif xp > 20000 and xp < 30000:
            usrlevel = "Gold 3"
        elif xp > 30000 and xp < 100000:
            usrlevel = "Platinum"
        elif xp > 100000:
            usrlevel = "Plat 2"

        lvl = 0
        rank = 0

        rankings = levelling.find().sort("xp", -1)
        for x in rankings:
            rank += 1
            if stats["id"] == x["id"]:
                break
        embed = discord.Embed(title=f'**Level: {usrlevel}** (Rank {rank})', description=f"{xp} XP",
                              color=discord.Color.green())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)

        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def leaderboard(self, ctx, num=1):
        if num == 1:
            rankings = levelling.find().sort("xp", -1)
            i = 1
            embed = discord.Embed(title="Leaderboard", color=discord.Color.green())
            embed_desc = ""
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                   # embed.add_field(name=f"{i}: {temp.name}", value=f"{tempxp}", inline=False)
                    embed_desc += f"**{i}: {temp.name}**  {tempxp}\n"
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            embed.description = embed_desc
            await ctx.send(embed=embed)
        elif num == 2:
            rankings = levelling.find().sort("xp", -1)
            i = 11
            embed = discord.Embed(title="Leaderboard", color=discord.Color.green())
            for x in rankings[10:]:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"{tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 21:
                    break
            await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @commands.is_owner()
    async def addxp(self, ctx, user: discord.User, num):
        stats = levelling.find_one({"id": user.id})
        xp = stats["xp"] + int(num)
        levelling.update_one({"id": user.id}, {"$set": {"xp": xp}})
        await ctx.send(f"Added {num} XP to {user.name}")

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @commands.is_owner()
    async def removexp(self, ctx, user: discord.User, num):
        stats = levelling.find_one({"id": user.id})
        xp = stats["xp"] - int(num)
        levelling.update_one({"id": user.id}, {"$set": {"xp": xp}})
        await ctx.send(f"Removed {num} XP from {user.name}")


    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(levelsys(client))


