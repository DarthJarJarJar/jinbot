import discord
from discord.ext import commands, tasks
from discord.ext.commands.errors import PrivateMessageOnly
from discord.utils import get
from discord import asset
from discord.user import User
from discord_slash import SlashCommand,SlashContext, client,ComponentContext
import discord_slash
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import wait_for_component
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash import cog_ext, SlashContext

guilds = [826766972204744764]


class tags(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('and desert you')

    @commands.command()
    async def jin(self,ctx, num=1):
        if ctx.channel.name == ("jin-chain"):
            if num>25:
                await ctx.send("Please use a value less than 25")
            elif num<0:
                await ctx.send("Please use a positive value")
            else:
                for i in range(num):
                    await ctx.send("<:jinhappy1:835921639551008818>")
        else:
            if num>5:
                await ctx.send("Please use a value less than 5")
            elif num<0:
                await ctx.send("Please use a positive value")
            else:
                for i in range(num):
                    await ctx.send("<:jinhappy1:835921639551008818>")
                
    @commands.command(name='xbox')
    async def xbox(self,ctx):
        await ctx.send('better')
    @commands.command()
    async def regret(self,ctx):
        await ctx.send('Today I am filled with regret to inform that we have had to remove a member of our community due to leaking sensitive information.')
    @commands.command()
    async def fortnite(self,ctx):
        await ctx.send('https://tenor.com/view/kratos-kratos-fortnite-fortnite-fortnite-dance-kratos-fortnite-dance-gif-19435698')
        
        
    @commands.command()
    async def gamepass(self,ctx):
        await ctx.send('game pass has over 300 games to play at a low fee of $15 a month and your first 3 months are only a dollar for new members')
        


    @commands.command()
    async def playstation(self,ctx):
        await ctx.send('<:sony:858204031067357195>')
        
        
    @commands.command()
    async def tasm2(self,ctx):
        await ctx.send("Some day, humanity will reach self individualization. Some day we'll move beyond petty scrabbles over the three poisons of life (greed, ignorance, and hatred). Some day, we will have reached a state where we're enlightened enough to watch TASM2 without calamity befalling us.")


    @commands.command()
    async def rickroll(self,ctx):
        await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')
        
    @commands.command()
    async def ratchetandclank(self,ctx):
        await ctx.send("They took the great story of the first game and completely cut out the interesting socioeconomic commentary and themes and satire of corporatism and shoved in the villain from the other franchise's games")

    @commands.command()
    async def rule16(self,ctx):
        await ctx.send('https://tenor.com/view/dead-chat-passione-admin-passione-jojolion-gif-19211422')
    @commands.command()
    async def mole(self,ctx):
        await ctx.send(" I'm going to reveal the truth.\n\n I am the mole.\n\n I in truth actually work with the aquatic animal in American spy ops to keep our country safe, and the government has declared this server a danger of the highest degree. It is to this end that I must monitor this server to make sure it doesn't invoke a third world war. It was for my country. It was for my duty.\n\nGod bless America.")

    @commands.command()
    async def welcome(self,ctx):
        await ctx.send(
            "<:Wjin:865274048988184588><:Ejin:865274113174405131><:Ljin:865274170157432843><:Cjin:865274259353370634><:Ojin:865274346129850408><:Mjin:865274436168450058><:Ejin:865274113174405131>")

    @commands.command()
    async def electro(self,ctx):
        await ctx.send('https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212')
        
    @commands.command()
    async def electrocursed(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/826766972204744767/888332410046001182/resize.gif')
        
    @commands.command()
    async def freeping(self,ctx):
        await ctx.send(f"Here's your free ping! {ctx.author.mention}")
        
    @commands.command()
    async def language(self,ctx):
        await ctx.send("من فضلك لا تستخدم أي لغة أخرى غير Jin")
        
    @commands.command()
    async def chatting(self,ctx):
        await ctx.send("Hey man, so I was thinking what if we make a server that is dedicated to chatting? As this one always seems to be dead :skull: @DarthJinJin")
        
        
    @commands.command()
    async def flameon(self,ctx):
        await ctx.send("https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")

    @commands.command()
    async def tsunami(self,ctx):
        await ctx.send(r"https://cdn.discordapp.com/attachments/826766972204744767/888799786818502656/ezgif-6-f8d0eca0573f.mp4")

    @commands.command()
    async def ill(self,ctx):
        await ctx.send(r'https://cdn.discordapp.com/attachments/316188354255519744/891745760406814720/unknown.png')        
        
        
    @commands.command()
    async def jin34(self,ctx):
        await ctx.send("did you know that in ghost of tsushima, the game engine renders the main character, jin sakai at 34 fps but renders the rest of the game world at 30 fps? the reason this was implemented was because gameplay felt much smoother when the player character was rendered at a higher framerate than the rest of the game world. to learn more google 'jin sakai rule 34' ")
            
    @cog_ext.cog_slash(name="jin", description="sends jins", guild_ids=guilds,options=[create_option(name='number', description='number of jins', required=True, option_type=4)])
    async def jin(self,ctx:SlashContext,number):
        if number>5:
            await ctx.send("Please use a value less than 5", hidden=True)
        elif number<0:
            await ctx.send("Please enter a valid number", hidden=True)
        else:
            for i in range(number):
                await ctx.send('<:jinhappy1:835921639551008818>')
        

    
    
    
    
    
    
    
    
    
    
    
    @cog_ext.cog_slash(name='xbox',guild_ids=guilds)
    async def xbox(self,ctx):
        await ctx.send('better')

    @cog_ext.cog_slash(name='regret',guild_ids=guilds)
    async def regret(self,ctx):
        await ctx.send('Today I am filled with regret to inform that we have had to remove a member of our community due to leaking sensitive information.')

        

    @cog_ext.cog_slash(name='fortnite',guild_ids=guilds)
    async def _fortnite(self,ctx):
        await ctx.send('https://tenor.com/view/kratos-kratos-fortnite-fortnite-fortnite-dance-kratos-fortnite-dance-gif-19435698')
        
        
    @cog_ext.cog_slash(name='gamepass',guild_ids=guilds)
    async def _gamepass(self,ctx):
        await ctx.send('game pass has over 300 games to play at a low fee of $15 a month and your first 3 months are only a dollar for new members')
        
    @cog_ext.cog_slash(name='tasm2',guild_ids=guilds)
    async def _tasm2(self,ctx):
        await ctx.send("Some day, humanity will reach self individualization. Some day we'll move beyond petty scrabbles over the three poisons of life (greed, ignorance, and hatred). Some day, we will have reached a state where we're enlightened enough to watch TASM2 without calamity befalling us.")

    @cog_ext.cog_slash(name='rickroll',guild_ids=guilds)
    async def _rickroll(self,ctx):
        await ctx.send('https://tenor.com/view/dance-moves-dancing-singer-groovy-gif-17029825')
        
    @cog_ext.cog_slash(name='ratchetandclank',guild_ids=guilds)
    async def _ratchetandclank(self,ctx):
        await ctx.send("They took the great story of the first game and completely cut out the interesting socioeconomic commentary and themes and satire of corporatism and shoved in the villain from the other franchise's games")

    @cog_ext.cog_slash(name='rule16',guild_ids=guilds)
    async def _rule16(self,ctx):
        await ctx.send('https://tenor.com/view/dead-chat-passione-admin-passione-jojolion-gif-19211422')
    @cog_ext.cog_slash(name='mole',guild_ids=guilds)
    async def _mole(self,ctx):
        await ctx.send(" I'm going to reveal the truth.\n\n I am the mole.\n\n I in truth actually work with the aquatic animal in American spy ops to keep our country safe, and the government has declared this server a danger of the highest degree. It is to this end that I must monitor this server to make sure it doesn't invoke a third world war. It was for my country. It was for my duty.\n\nGod bless America.")

    @cog_ext.cog_slash(name='electro',guild_ids=guilds)
    async def _electro(self,ctx):
        await ctx.send('https://tenor.com/view/amazing-spiderman2vomit-electro-amazing-spiderman2-spiderman-vomit-sex-gif-13866212')
        
    @cog_ext.cog_slash(name='electrocursed',guild_ids=guilds)
    async def _electrocursed(self,ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/826766972204744767/888332410046001182/resize.gif')
        
    @cog_ext.cog_slash(name='freeping',guild_ids=guilds)
    async def _freeping(self,ctx):
        await ctx.send(f"Here's your free ping! {ctx.author.mention}")
        
    @cog_ext.cog_slash(name='language',guild_ids=guilds)
    async def _language(self,ctx):
        await ctx.send("من فضلك لا تستخدم أي لغة أخرى غير Jin")
        
    @cog_ext.cog_slash(name='chatting',guild_ids=guilds)
    async def _chatting(self,ctx):
        await ctx.send("Hey man, so I was thinking what if we make a server that is dedicated to chatting? As this one always seems to be dead :skull: @DarthJinJin")
        
        
    @cog_ext.cog_slash(name='flameon',description="Flame on and on and on and on!",guild_ids=guilds)
    async def _flameon(self,ctx):
        await ctx.send("https://media.discordapp.net/attachments/826766972204744767/888296963517333564/flameon.gif")
        
            

        
def setup(client):
    client.add_cog(tags(client))

    

