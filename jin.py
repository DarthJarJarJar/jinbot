import discord
from discord.ext import commands, tasks
from discord.gateway import DiscordWebSocket
from discord.utils import get
from discord import asset
from discord.user import User

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import asyncio
import math
from dateutil import tz
from selenium import webdriver

import re
import functools
import itertools
import math
import random
import datetime
from discord_slash import SlashCommand,SlashContext, client,ComponentContext
import discord_slash
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
import sys
from discord_slash.utils.manage_components import wait_for_component
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
import time
from cogs import levelsys,credit,psn,tagdb
from currency_converter import CurrencyConverter

from async_timeout import timeout
  

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix='*', intents=intents)
slash = SlashCommand(client, sync_commands=True)
guilds = [826766972204744764]

welcome = "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>"


@client.event
async def on_ready():
    print('never gonna give you up')
    await client.change_presence(activity=discord.Game(name="Jin of Jinshima"))






cogs = [levelsys,credit,psn,tagdb]

for i in range(len(cogs)):
    cogs[i].setup(client)








@client.event
async def on_member_join(member):
    print(f'welcome {member}')
    channel = client.get_channel(854247382086189066)
    jinchain = client.get_channel(834406006351462420)
    jinrules = client.get_channel(893929998614925322)
    await channel.send(
        "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")
    embed1 = discord.Embed(title=f"Welcome {member}!", description=f"Contribute to {jinchain.mention} and check out {jinrules.mention} to get started! Remember to flame on and on and on and on")
    await channel.send(member.mention)
    await channel.send(embed=embed1)
    await channel.send('https://media.discordapp.net/attachments/826766972204744767/885951474109149274/tumblr_ovbx1zq11b1vo889bo8_400.gifv.gif')
    role = get(member.guild.roles, id=833781809128669265)
    await member.add_roles(role)






@client.event
async def on_member_remove(member):
    print(f'goodbye {member}')
    
    
    
@client.command()
async def jumbo(ctx, emoji: discord.Emoji):
    await ctx.send(emoji.url)
   



@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member : discord.Member):
    mutedrole = discord.utils.get(ctx.guild.roles, name="Mute")
    await member.add_roles(mutedrole)
    await ctx.send("User was muted")
    
@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member : discord.Member):
    mutedrole = discord.utils.get(ctx.guild.roles, name="Mute")
    await member.remove_roles(mutedrole)
    await ctx.send("User was unmuted")
@client.command()
async def work(ctx):
    await ctx.send("it worked")      

        
@client.command()
async def avatar(ctx, avamember : discord.Member=None):
    if avamember == None:
      avamember = ctx.author
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)        
        
                

@client.command(aliases=['colour'])
@commands.has_any_role('Gold 1', 'Gold 2', 'Gold 3', 'Platinum', 'Jin Booster')
async def color(ctx, color = None):
    colorlist = ['blue','green','purple','orange','vomit']
    if color == None:
        await ctx.send(f"Please specify a valid color. Available colors: {colorlist}")
    else:
        #checking the color argument
        if color not in colorlist:
            await ctx.send(f"Please specify a valid color. Available colors: {colorlist}")
        else:
            #checking if author already has a color role
            for role in ctx.author.roles:
                for i in colorlist:
                    current_color_role = discord.utils.get(ctx.guild.roles, name=i)
                    if role == current_color_role:
                        await ctx.author.remove_roles(current_color_role)
                        break


            
            color_role = discord.utils.get(ctx.guild.roles, name=color)
            await ctx.author.add_roles(color_role)
            await ctx.send(f'Colors updated. Set color to {color}')
                   

@client.command()
async def eldenring(ctx):
  
  delta = datetime.datetime(2022,2,25,0,0)-datetime.datetime.now()
  eldendays=str(delta.days)+" days "
  count = 0
  for i in range(len(str(delta))-1):
      if str(delta)[i]==",":
          count = i+2
  x=str(delta)[count:]
  y=x.split(":")

  eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
  eldentime=eldendays+eldenhours
 
  await ctx.send(f"Time until Elden Ring: {eldentime}")
  
  
  


@client.command()
async def countdown(ctx,yy,m,d):
  
  delta = datetime.datetime(int(yy),int(m),int(d),0,0)-datetime.datetime.now()
  eldendays=str(delta.days)+" days "
  count = 0
  for i in range(len(str(delta))-1):
      if str(delta)[i]==",":
          count = i+2
  x=str(delta)[count:]
  y=x.split(":")

  eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
  eldentime=eldendays+eldenhours
 
  await ctx.send(fr"Time until {yy}/{m}/{d}: {eldentime}")
 
@client.command()
async def jincast(ctx,flag=True):
    if flag==True:
      jincast = discord.utils.get(ctx.guild.roles, name="Jincast Follower")
      if jincast in ctx.author.roles:
        await ctx.send("You already have the Jincast Follower role")
      else:
        await ctx.author.add_roles(jincast)
        await ctx.send("Added the Jincast Follower role")
    elif flag=="remove":
      jincast = discord.utils.get(ctx.guild.roles, name="Jincast Follower")
      if jincast in ctx.author.roles:
        await ctx.author.remove_roles(jincast)
        await ctx.send("Removed the Jincast Follower role")
      else:
        await ctx.send("You don't have the Jincast Follower role")
    else:
      await ctx.send("Enter a valid argument")
        
    
  
        
 ######SLASH COMMANDS#######

@slash.slash(name="echo", description="echoes what you said", guild_ids=guilds,options=[create_option(name="text", description='text you wish to echo',required=True,option_type=3)])
async def echo(ctx : SlashCommand, text : str):
    await ctx.send(text)




@slash.slash(name="button", description="buttons test", guild_ids=guilds)
async def button(ctx:SlashContext):
    buttons = [
        create_button(style=ButtonStyle.blue, label="Electro",custom_id="electrovomit"),
        create_button(style=ButtonStyle.red, label="Flame on",custom_id="flameonandon")
        
    ]
    action_row = create_actionrow(*buttons)
    await ctx.send("Choose one",components=[action_row])
    while True:
        button_ctx: ComponentContext = await wait_for_component(client, components=action_row)
        if button_ctx.custom_id=="electrovomit":
            await button_ctx.edit_origin(content="https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212")
        elif button_ctx.custom_id=="flameonandon":
            await button_ctx.edit_origin(content="https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")



    
@slash.slash(name='eldenring',description="Shows time left until the release of Elden Jin",guild_ids=guilds)
async def eldenring(ctx):
  
  delta = datetime.datetime(2022,2,25,0,0)-datetime.datetime.now()
  eldendays=str(delta.days)+" days "
  count = 0
  for i in range(len(str(delta))-1):
      if str(delta)[i]==",":
          count = i+2
  x=str(delta)[count:]
  y=x.split(":")

  eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
  eldentime=eldendays+eldenhours
 
  await ctx.send(f"Time until Elden Ring: {eldentime}")
  
@slash.slash(name="countdown", description="Shows time remaining until a certain date",guild_ids=guilds, options=[create_option(name="yyyy",description="Year", option_type=4,required=True),create_option(name="mm",description="Month",option_type=4,required=True),create_option(name="dd",description="Date",option_type=4,required=True)])
async def countdown(ctx,yyyy,mm,dd):
  
  delta = datetime.datetime(int(yyyy),int(mm),int(dd),0,0)-datetime.datetime.now()
  eldendays=str(delta.days)+" days "
  count = 0
  for i in range(len(str(delta))-1):
      if str(delta)[i]==",":
          count = i+2
  x=str(delta)[count:]
  y=x.split(":")

  eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
  eldentime=eldendays+eldenhours
 
  await ctx.send(fr"Time until {yyyy}/{mm}/{dd}: {eldentime}")        
                
@slash.slash(name="select",guild_ids=guilds)
async def _select(ctx:SlashContext):
    select = create_select(options=[create_select_option("Electro", value="electro"),create_select_option('Flame On!',value="flameon"),create_select_option("Jin", value="jin")],placeholder="Choose an option",max_values=1)
    
    await ctx.send("test", components=[create_actionrow(select)])
    while True:
        button_ctx: ComponentContext = await wait_for_component(client, components=select)
        if button_ctx.selected_options[0]=="electro":
            await button_ctx.edit_origin(content=f"https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212")
        if button_ctx.selected_options[0]=="flameon":
            await button_ctx.edit_origin(content=f"https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")
        if button_ctx.selected_options[0]=="jin":
            await button_ctx.edit_origin(content=f"https://cdn.discordapp.com/emojis/835921639551008818.png")
        
@slash.slash(name="jin34", description="Interesting trivia about the hit PS exclusive Ghost of Tsushima!")
async def jin34(ctx):
    await ctx.send("did you know that in ghost of tsushima, the game engine renders the main character, jin sakai at 34 fps but renders the rest of the game world at 30 fps? the reason this was implemented was because gameplay felt much smoother when the player character was rendered at a higher framerate than the rest of the game world. to learn more google 'jin sakai rule 34' ")

@slash.slash(name="jincast", description="Adds the Jincast follower role", guild_ids=guilds)
async def _jincast(ctx:SlashContext):
    jincastRole = discord.utils.get(ctx.guild.roles, name = "Jincast Follower")
    if jincastRole in ctx.author.roles:
        await ctx.send("You already have the Jincast Follower role!", hidden=True)
    else:
        await ctx.author.add_roles(jincastRole)   

  
@slash.slash(name="color",guild_ids=guilds)
async def _colour(ctx:SlashContext):
    select = create_select(options=[
        create_select_option("blue", value="blue",description="Adds the blue color role"),
        create_select_option('green',value="green",description="Adds the green color role"),
        create_select_option("vomit", value="vomit",description="Adds the vomit color role"),
        create_select_option("orange",value="orange",description="Adds the orange color role"),
        create_select_option("purple",value="purple",description="Adds the purple color role"),
        create_select_option("blurple",value="blurple",description="Adds the blurple color role"),
        create_select_option("peach",value="peach",description="Adds the peach color role"),
        create_select_option("dark red",value="dark red",description="Adds the dark red color role"),
        create_select_option("remove", value="remove",description="Removes any of the color role you have")
        ],
        placeholder="Choose a color",max_values=1)
    
    await ctx.send("Select a color to add", components=[create_actionrow(select)])
    button_ctx: ComponentContext = await wait_for_component(client, components=select)
    colorlist = ['blue','green','purple','orange','vomit',"blurple",'peach','dark red']
    if button_ctx.selected_options[0]=="remove":
        for role in ctx.author.roles:
                    for i in colorlist:
                        current_color_role = discord.utils.get(ctx.guild.roles, name=i)
                        if role == current_color_role:
                            await ctx.author.remove_roles(current_color_role)
                            break
        await button_ctx.edit_origin(content="Removed your color role!")
    else:
        for role in ctx.author.roles:
                    for i in colorlist:
                        current_color_role = discord.utils.get(ctx.guild.roles, name=i)
                        if role == current_color_role:
                            await ctx.author.remove_roles(current_color_role)
                            break   
        colorRole = discord.utils.get(ctx.guild.roles, name=button_ctx.selected_options[0])
        await ctx.author.add_roles(colorRole)
        await button_ctx.edit_origin(content="Added the color role!")


@slash.slash(name="avatar",description="Shows user avatar",guild_ids=guilds, options=[create_option(name="user",description="Select user",option_type=6,required=False)])
async def _avatar(ctx:SlashContext, user : discord.Member = None):
    if user == None:
        await ctx.send(ctx.author.avatar_url)
    else:
        await ctx.send(user.avatar_url)

@slash.slash(name="time",
 description="Formats the timestamp you input so that it reflects as local time for other users", 
 guild_ids=guilds,
 options=[create_option(name="year",description="The year of the timestamp(yyyy)",option_type=4,required=True),
 create_option(name="month",description="The month of the timestamp(mm)",required=True,option_type=4),
 create_option(name="date",description="The date of the timestamp(dd)",option_type=4,required=True),
 create_option(name="hours", description="Hours of the timestamp(24h format, dd)",option_type=4,required=True),
 create_option(name="minutes",description="The minutes of the timestamp",option_type=4,required=True),
 create_option(name="timezone",description="Your timezone",option_type=4,required=True,choices=[create_choice(name="est",value=0),create_choice(name="ist",value=1),create_choice(name="gmt",value=2)])] )
async def _time(ctx:SlashContext,year:int,month:int,date:int,hours:int,minutes:int,timezone:str):
    
    if timezone==0:
        abc = tz.gettz('US/Eastern')
    if timezone==1:
        abc = tz.gettz('Asia/Kolkata')
        minutes +=30
    if timezone==2:
        timediff = tz.gettz('Europe/Belfast')
    
    d = datetime.datetime(year,month,date,hours,minutes,tzinfo=abc)
    unixtime = time.mktime(d.timetuple())
    
    
    #loctime = unixtime+timediff
    await ctx.send(f'<t:{int(unixtime)}>')

@slash.slash(name="work", description="please work", guild_ids=guilds)
async def _work(ctx:SlashContext):
    await ctx.send("worked")

'''@slash.slash(name="rolesetup", guild_ids=guilds, description="setup for roles")
async def _testrole(ctx:SlashContext):
    buttons = [
        create_button(style=ButtonStyle.blue, label="Announcements",custom_id="announcements"),
        create_button(style=ButtonStyle.blue, label="Polls",custom_id="polls"),
        create_button(style=ButtonStyle.blue, label="Games", custom_id="games"),
        create_button(style=ButtonStyle.blue,label="Movies",custom_id="movies"),
        create_button(style=ButtonStyle.blue,label="Fortnite",custom_id="fortnite")
        
    ]
    action_row = create_actionrow(*buttons)
    embed=discord.Embed(title="Self Roles",
    description="**Announcements:** Get notified for server announcements!\n**Movies:** Get notified when we're watching a movie!\n**Games:** Get notified when we're trying to play a game together!\n**Polls:** Get notified for polls!\n**Fortnite:** Get notified when we're playing Fortnite!")
    await ctx.send(embed=embed,components=[action_row])'''

@slash.slash(name="convert", description="Currency converter command",guild_ids=guilds,options=[create_option(name="first_currency",description="Currency you want to convert form",option_type=3,required=True),create_option(name="second_currency",description="Currency you want to convert to",option_type=3,required=True),create_option(name="amount",description="Amount you want to convert",option_type=4,required=True)])
async def _convert(ctx,first_currency:str,second_currency:str,amount):
    am = amount
    c1 = first_currency
    c2 = second_currency
    driver = webdriver.Chrome(r'/app/.chromedriver/bin/chromedriver')


    driver.get(fr"https://www.google.com/search?q={am}+{c1}+to+{c2}&rlz=1C5CHFA_enCA983CA983&oq={am}+{c1}+&aqs=chrome.0.69i59j69i57j0i67l8.1146j0j7&sourceid=chrome&ie=UTF-8")
    driver.implicitly_wait(10)
    elem = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/div[2]/span[1]")
    val= elem.get_attribute("data-value")

    await ctx.send(f"{am} {c1.upper()} is {val} {c2.upper()}")


@client.command()
async def __convert(ctx,amount,first_currency:str,second_currency:str):
    am = amount
    c1 = first_currency
    c2 = second_currency
    driver = webdriver.Chrome(r'/app/.chromedriver/bin/chromedriver')


    driver.get(fr"https://www.google.com/search?q={am}+{c1}+to+{c2}&rlz=1C5CHFA_enCA983CA983&oq={am}+{c1}+&aqs=chrome.0.69i59j69i57j0i67l8.1146j0j7&sourceid=chrome&ie=UTF-8")
    driver.implicitly_wait(20)
    elem = driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/div[1]/div[2]/span[1]")
    val= elem.get_attribute("data-value")

    await ctx.send(f"{am} {c1.upper()} is {val} {c2.upper()}")


    

@client.event
async def on_component(ctx:ComponentContext):
    if ctx.custom_id=="announcements":
            role = discord.utils.get(ctx.guild.roles, name = "Announcements")
            await ctx.author.add_roles(role)
            await ctx.send(f"Added the announcements role!", hidden=True)
    elif ctx.custom_id=="movies":
            role = discord.utils.get(ctx.guild.roles, name = "Movies")
            await ctx.author.add_roles(role)
            await ctx.send(f"Added the  movies role!", hidden=True)
    elif ctx.custom_id=="games":
            role = discord.utils.get(ctx.guild.roles, name = "Games")
            await ctx.author.add_roles(role)
            await ctx.send(f"Added the  games role!", hidden=True)

    elif ctx.custom_id=="polls":
            role = discord.utils.get(ctx.guild.roles, name = "Polls")
            await ctx.author.add_roles(role)
            await ctx.send(f"Added the  polls role!", hidden=True)
    
    elif ctx.custom_id=="fortnite":
            role = discord.utils.get(ctx.guild.roles, name = "Fortnite")
            await ctx.author.add_roles(role)
            await ctx.send(f"Added the fortnite role!", hidden=True)
    
    

    

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                                 
client.run('ODcyMTk0NzA3MTE0MDQ1NDQw.YQmUng.ZUFMj_ZzY17w-nDKPkxwyLFX6Pg')
