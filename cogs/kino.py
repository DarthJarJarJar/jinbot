from itertools import count
from unittest import result
import requests
import json
import discord
from discord.ext import commands
from discord import app_commands

from cogs.cog import MY_GUILD_ID
 

def filter(list, key, value):
    for dict in list:
        if dict[key]==value:
            return dict


class SearchKino:
    def __init__(self, key) -> None:
        self.key = key
        res = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key=88637c22a27d11937d1168157cf81ce9&language=en-US&query={key}&page=1")
        resulttemp = json.loads(res.text)
        result = resulttemp['results']
        res_list = []
        for movie in result:
            res_list.append({'name': movie['original_title'], 'date': movie['release_date'], 'id':movie['id']})
        self.results = res_list

class Kino:
    def __init__(self, id) -> None:
        self.id = id
        res = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=88637c22a27d11937d1168157cf81ce9&language=en-US")
        self.data = json.loads(res.text)
        data = json.loads(res.text)
        self.description = data['overview']
        self.runtime = data['runtime']
        self.title = data['title']
        self.tagline = data['tagline']
        res2 = requests.get(f"https://api.themoviedb.org/3/movie/{id}/credits?api_key=88637c22a27d11937d1168157cf81ce9&language=en-US")
        credits: dict = json.loads(res2.text)
        crew = (credits['crew'])
        director = filter(crew, 'job', 'Director')
        self.director = director
        poster_path = data['poster_path']
        self.poster = r"https://image.tmdb.org/t/p/w500"+poster_path


class Movie(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna say goodbye')


    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def kino(self, ctx, kino):
        search = SearchKino(kino)
        results = search.results

        embed = discord.Embed(title=f"Search results for {kino}", color=discord.Color.green())
        desc = ""
        counter = 1
        for kino in results:
            desc += f"**{counter}. {kino['name']}** ({kino['data']})\n\n"
        embed.description = desc
        await ctx.send(embed=embed)



    


    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(Movie(client))

    
    






    