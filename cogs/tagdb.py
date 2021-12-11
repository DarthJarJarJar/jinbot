import discord
from discord.ext import commands
from pymongo import MongoClient
from discord.utils import get
from discord_slash import cog_ext, SlashContext


import urllib.parse

username = urllib.parse.quote_plus('darthjarjar')
password = urllib.parse.quote_plus('A@yaan12')

cluster = MongoClient('mongodb+srv://%s:%s@cluster0.u6uh4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'% (username, password))


tag_handler = cluster["discord"]["tags"]

class tagdb(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("never gonna say goodbye")


    @commands.Cog.listener()
    async def on_message(self,message):
        taglist = []
        for i in tag_handler.find():
            tagname = i["name"]
            taglist.append(tagname)
        print(taglist)
        if message.content.startswith('*'):
            for i in taglist:
                if message.content[1:]==i:
                    tag1 = tag_handler.find_one({"name" : i})
                    await message.channel.send(tag1["content"])
                    break
            


            
        
    




    @commands.command()
    async def tag(self,ctx,action:str,name:str,*,content:str=None):
        if action.lower()=="create":
            newtag = {"name" : name, "content" : content, "creator" : ctx.author.id}
            tag_handler.insert_one(newtag)
            embed=discord.Embed(title="Tag created")
            embed.add_field(name="Tag name", value=name)
            embed.add_field(name="Content",value=content)
            embed.add_field(name="Creator",value=ctx.author.mention)
            await ctx.send(embed=embed)
        if action.lower()=="edit":
            tag_handler.update_one({"name" : name}, {"$set" : {"content" : content}})
            taginquestion = tag_handler.find_one({"name":name})
            
            embed=discord.Embed(title="Tag edited")
            embed.add_field(name="Tag name", value=name)
            embed.add_field(name="New Content",value=content)
            embed.add_field(name="Editor",value=ctx.author.mention)
            await ctx.send(embed=embed)
        
        if action.lower()=="delete":
            tag_handler.delete_one({"name":name})
            await ctx.send("Tag deleted")


    @commands.command()
    async def tags(ctx):
        taglist = []
        for i in tag_handler.find():
            tagname = i["name"]
            taglist.append(tagname)
        tagstr = ""
        for tag in taglist:
            tagstr+=f"{tag} "
        await ctx.send(f"`{tagstr}`")

    


def setup(client):
    client.add_cog(tagdb(client))




        
            

            
          

        
        