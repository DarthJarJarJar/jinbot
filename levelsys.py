import discord
from discord.ext import commands
from pymongo import MongoClient
from discord.utils import get



import urllib.parse

username = urllib.parse.quote_plus('darthjarjar')
password = urllib.parse.quote_plus('A@yaan12')

cluster = MongoClient('mongodb+srv://%s:%s@cluster0.u6uh4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'% (username, password))

level = ["Bronze", "Silver 1", "Silver 2", "Silver 3", "Gold 1", "Gold 2", "Gold 3", "Platinum"]
levelnum = [5,25,50,75,100,150,200,300]

levelling = cluster["discord"]["levelling"]

class levelsys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna run around')

    @commands.Cog.listener()
    async def on_message(self,message):
        stats = levelling.find_one({"id" : message.author.id})
        if not message.author.bot:
            if stats is None:
                newuser = {"id" : message.author.id, "xp" : 0}
                levelling.insert_one(newuser)
            else:
                xp = stats["xp"] + 2
                levelling.update_one({"id" : message.author.id}, {"$set" : {"xp" : xp}})
                lvl = 0
                if xp == 250:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Bronze 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                    
                elif xp == 500:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Bronze 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Bronze 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                if xp == 1250:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Bronze 3"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Bronze 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 2500:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Silver 1"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Bronze 3"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 5000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Silver 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Silver 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 7500:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Silver 3"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Silver 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 10000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Gold 1"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Silver 3"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 15000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Gold 2"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Gold 1"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 20000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Gold 3"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Gold 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")
                elif xp == 30000:
                    await message.author.add_roles(discord.utils.get(message.author.guild.roles, name="Platinum"))
                    await message.author.remove_roles(discord.utils.get(message.author.guild.roles, name="Gold 2"))
                    await message.channel.send(f"{message.author.mention} has levelled up!")

    @commands.command()
    async def xp(self, ctx):
        stats = levelling.find_one({"id": ctx.author.id})
        xp = stats["xp"]
        if xp<250:
            usrlevel = "No Level"
        elif xp>1250 and xp<2500:
            usrlevel = "Bronze 3"
        elif xp>500 and xp<1250:
            usrlevel = "Bronze 2"
        elif xp>250 and xp<500:
            usrlevel = "Bronze 1"

        elif xp>2500 and xp<5000:
            usrlevel = "Silver 1"
        elif xp>5000 and xp<7500:
            usrlevel = "Silver 2"
        elif xp>5000 and xp<7500:
            usrlevel = "Silver 2"
        elif xp>7500 and xp<10000:
            usrlevel = "Silver 3"
        elif xp>10000 and xp<15000:
            usrlevel = "Gold 1"
        elif xp>15000 and xp<20000:
            usrlevel = "Gold 2"
        elif xp>20000 and xp<3000:
            usrlevel = "Gold 3"
        elif xp>30000 :
            usrlevel = "Platinum"




        lvl = 0
        rank = 0
     #   while True:
           # if xp < ((50 * lvl ** 2) + (50 * (lvl - 1))):
           #     break
          #  lvl += 1
   #     xp -= ((50 * lvl ** 2) + (50 * (lvl - 1)))
        rankings = levelling.find().sort("xp", -1)
        for x in rankings:
            rank+=1
            if stats["id"]==x["id"]:
                break
        embed = discord.Embed(title=f'**Level: {usrlevel}** (Rank {rank})', description=f"{xp} XP", color=discord.Color.green())
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def leaderboard(self,ctx):
        rankings = levelling.find().sort("xp",-1)
        i = 1
        embed = discord.Embed(title="Leaderboard",color=discord.Color.green())
        for x in rankings:
            try:
                temp = ctx.guild.get_member(x["id"])
                tempxp = x["xp"]
                embed.add_field(name=f"{i}: {temp.name}", value=f"{tempxp}", inline=False)
                i += 1
            except:
                pass
            if i == 11:
                break
        await ctx.channel.send(embed=embed)


    @commands.command()
    @commands.has_role('tamper xp')
    async def addxp(self,ctx,ussr : discord.User, num):
        stats = levelling.find_one({"id": ussr.id})
        xp = stats["xp"] + int(num)
        levelling.update_one({"id": ussr.id}, {"$set": {"xp": xp}})

    @commands.command()
    @commands.has_role('tamper xp')
    async def removexp(self, ctx, ussr : discord.User, num):
        stats = levelling.find_one({"id": ussr.id})
        xp = stats["xp"] - int(num)
        levelling.update_one({"id": ussr.id}, {"$set": {"xp": xp}})




def setup(client):
    client.add_cog(levelsys(client))


