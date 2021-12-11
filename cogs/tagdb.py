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
    async def on_meassage(self,message):
        taglist = []
        for i in tag_handler:
            tagname = i["name"]
            taglist.append(tagname)
        print(taglist)
        
        for i in taglist:
            if message.content=='!'+i:
                tagcalled = i
                break
        tag1 = tag_handler.find_one({"name" : tagcalled})
        await message.channel.send(tag1["content"])


            
        
    




    @commands.command()
    async def tag(self,ctx,action:str,name:str,*,content:str=None):
        if action.lower()=="create":
            newtag = {"name" : name, "content" : content, "creator" : ctx.author.id}
            tag_handler.insert_one(newtag)
        if action.lower()=="edit":
            tag_handler.update_one({"name" : name}, {"$set" : {"content" : content}})

def setup(client):
    client.add_cog(tagdb(client))




        
            

            
          

        
        