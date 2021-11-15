import discord
from discord.ext import commands
from pymongo import MongoClient
from discord.utils import get
from discord_slash import cog_ext, SlashContext
import json
import random



import urllib.parse

username = urllib.parse.quote_plus('darthjarjar')
password = urllib.parse.quote_plus('A@yaan12')

cluster = MongoClient('mongodb+srv://%s:%s@cluster0.u6uh4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'% (username, password))

guilds = [826766972204744764]

levelling = cluster["discord"]["levelling"]






#These are the lists where the possible outcomes are stored.
posibilities = []
weights = []

#This function simply loads the json file. You shouldn't need to use it outside of this program.
def load_odds_json():
        #Opens the 'odds.json' file.
        odds_file = open("/app/cogs/odds.json")
        #Loads it into a JSON object.
        data = json.load(odds_file)
        
        #For every entry in the JSON file...
        for x in data:
            #Add the properties to their respective list.
            posibilities.append(x["multiplier"])
            weights.append(x["weight"])
        
        print("Odds loaded successfully!")

#This function handles the mathmatics of the gambling here. Returns a tuplet containing the the new amount, the multiplier, and the original amount.
def gamble(n):
    multiplier = random.choices(posibilities, weights)[0]
    
    return (n*multiplier, multiplier, n)

load_odds_json()


class credit(commands.Cog):
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
                newuser = {"id" : message.author.id, "xp" : 0, "credit" : 0}
                levelling.insert_one(newuser)
            else:
                
                socialcredit = 10
                jinlist = ['<:jinhappy1:835921639551008818>',
                '<:jintroll:887239493856423947>',
                '<:jintrol:900420574893981698>',
                '<:jinhollow:887994492903383080',
                'jinwolloh:890624462561624144>'
                ,'<:jinhype:883393914143387699>'
                ,'<:jincool:854229962088251424>'
                ,'<:Jingrief:886952606168133732>'
                ,'<:jtl:900422440482635857>',
                '<:Jinwide2:856038550738698250>',
                '<:jinchad:888109451872174091>'  ]
                for emoji in jinlist:
                    if emoji in message.content:
                        socialcredit = 20
                        break
                
                credwords = {
                    'jai hind' : 20,
                    'jai jind' : 20,
                    'jin sucks' : -100,
                    'wah wah' : 20,
                    'something happened in jinanmen square in 1989' : -60000000,
                    'fish' : -100000
                }
                for word in credwords:
                    if word in message.content.lower():
                        socialcredit = credwords[word]
                
                credit = stats["credit"] + socialcredit
                
                levelling.update_one({"id" : message.author.id}, {"$set" : {"credit" : credit}})

    @commands.command()
    
    async def gift(self,ctx,ussr : discord.User, num:int):
    
        stats = levelling.find_one({"id": ctx.author.id})
        if num>stats["credit"]:
            await ctx.channel.send("You can't gift more credits than what you have")
        else:
            giftercredit = stats["credit"] - int(num)
            levelling.update_one({"id": ctx.author.id}, {"$set": {"credit": giftercredit}})
            stats2 = levelling.find_one({"id": ctx.author.id})
            gifteecredit = stats2["credit"] + int(num)
            levelling.update_one({"id": ussr.id}, {"$set": {"credit": gifteecredit}})
            await ctx.channel.send(f"Gifted {num} jincord social credits to {ussr.name}")

    @commands.command(name="credit")
    async def jcredit(self,ctx):
        stats = levelling.find_one({"id": ctx.author.id})
        credit = stats["credit"] 
        await ctx.send(f'Your jincord social credit is {credit}')


    @commands.command()
    async def creditboard(self,ctx, num=1):
        if num == 1:
            rankings = levelling.find().sort("credit",-1)
            i = 1
            embed = discord.Embed(title="Jincord Credits Leaderboard",color=discord.Color.green())
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["credit"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"{tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)
        elif num==2:
            rankings = levelling.find().sort("credit",-1)
            i = 11
            embed = discord.Embed(title="Jincord Credits Leaderboard",color=discord.Color.green())
            for x in rankings[10:]:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["credit"]
                    embed.add_field(name=f"{i}: {temp.name}", value=f"{tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 21:
                    break
            await ctx.channel.send(embed=embed)

    @commands.command(name='gamble')
    async def _gamble(ctx,n:int):
        stats = levelling.find_one({"id": ctx.author.id})
        gambleTuple = gamble(n)
        tempcredit = stats["credit"]-n
        newcredit = tempcredit+gambleTuple[0]
        levelling.update_one({"id": ctx.author.id}, {"$set": {"credit": newcredit}})
        await ctx.send(f"New total: {gambleTuple[0]}\nMultiplier: {gambleTuple[1]}\nOriginal amount: {gambleTuple[2]}")
        



def setup(client):
    client.add_cog(credit(client))


    


    




