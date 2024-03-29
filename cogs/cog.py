from typing import List
import discord
from discord import app_commands, embeds
from discord.ext import commands
from dateutil import tz
from datetime import datetime
from pytz import timezone
from discord.app_commands import Choice
import requests
import json

guild_id = 826766972204744764

MY_GUILD_ID = discord.Object(guild_id)

import requests


class SearchGame():
    def __init__(self, game):
        url = "https://api.igdb.com/v4/search/"

        data = requests.post(
            url=url,
            headers={
                'Client-ID': 'o5xvtlqq670n8hhzz05rvwpbr7hjt4',
                'Authorization': "Bearer sd089a9azgftad7tbbaroxitu6x71k",
            },
            data=fr'search "{game}";limit 5; fields name, game.id, game.platforms.name; where game.cover.image_id != null & game.version_parent = null & game.screenshots != null & game.follows != null & game.aggregated_rating != null;'
        )
        result = data.json()
        self.results = result


class Game():

    def __init__(self, id):

        url = "https://api.igdb.com/v4/games"
        data = requests.post(url=url,
                             data=fr"fields name, genres.name, aggregated_rating, platforms.name, platforms.id, release_dates.human, summary, cover.image_id, involved_companies.company.name; where id = {id};",
                             headers={
                                 'Client-ID': 'o5xvtlqq670n8hhzz05rvwpbr7hjt4',
                                 'Authorization': "Bearer sd089a9azgftad7tbbaroxitu6x71k",
                             })
        result = data.json()
        game_data = result[0]
        genres = []
        genre_list = game_data["genres"]
        for genre in genre_list:
            genres.append(genre["name"])
        genre_string = ", ".join(genres)
        companies = []

        inv_companies = game_data["involved_companies"]
        for company in inv_companies:
            companies.append(company["company"]["name"])

        company_string = ", ".join(companies)

        platforms = []
        platform_data = game_data["platforms"]
        for platform in platform_data:
            platforms.append(platform["name"])

        platform_string = ", ".join(platforms)

        game_summary = game_data["summary"]
        if len(game_summary) > 3200:
            game_summary = game_summary[:3200] + "..."

        self.platforms = platform_string
        self.genres = genre_string
        self.devs = company_string
        self.name = game_data["name"]
        self.description = game_summary
        self.cover = f"https://images.igdb.com/igdb/image/upload/t_cover_big/{game_data['cover']['image_id']}.jpg"
        self.rating = int(game_data["aggregated_rating"])
        self.date = game_data['release_dates'][0]['human']


class PersistentView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='Announcements', style=discord.ButtonStyle.green, custom_id='Annoucements')
    async def a(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the announcements role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Announcements"))

    @discord.ui.button(label='Movies', style=discord.ButtonStyle.green, custom_id='Movies')
    async def m(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the movies role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Movies"))

    @discord.ui.button(label='Games', style=discord.ButtonStyle.green, custom_id='Games')
    async def g(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the games role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Games"))

    @discord.ui.button(label='Polls', style=discord.ButtonStyle.green, custom_id='Polls')
    async def p(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the polls role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Polls"))

    @discord.ui.button(label='Fortnite', style=discord.ButtonStyle.green, custom_id='Fortnite')
    async def f(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Added the fortnite role', ephemeral=True)
        await interaction.user.add_roles(discord.utils.get(interaction.guild.roles, name="Fortnite"))


class SelectColor(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(label="Blue", description="Adds the Blue color role!"),
            discord.SelectOption(label="Green", description="Adds the Green color role!"),
            discord.SelectOption(label="Vomit", description="Adds the Vomit color role!"),
            discord.SelectOption(label="Orange", description="Adds the Orange color role!"),
            discord.SelectOption(label="Purple", description="Adds the Purple color role!"),
            discord.SelectOption(label="Blurple", description="Adds the Blurple color role!"),
            discord.SelectOption(label="Peach", description="Adds the Peach color role!"),
            discord.SelectOption(label="Dark Red", description="Adds the Dark Red color role!"),
            discord.SelectOption(label="Black", description="Adds the Black color role!"),
            discord.SelectOption(label="Remove", description="Remove any color roles that you have!"),
        ]

        super().__init__(placeholder="Select an option", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Remove":
            colorlist = ["Blue", "Green", "Orange", "Purple", "Blurple", "Black", "Peach", "Dark Red", "Vomit"]
            for color in colorlist:
                temprole = discord.utils.get(interaction.guild.roles, name=color)
                await interaction.user.remove_roles(temprole)
                await interaction.message.edit(content=f"Removed your color role!", view=None)


        else:
            colorlist = ["Blue", "Green", "Orange", "Purple", "Blurple", "Black", "Peach", "Dark Red", "Vomit"]
            for color in colorlist:
                temprole = discord.utils.get(interaction.guild.roles, name=color)
                await interaction.user.remove_roles(temprole)
            colorrole = discord.utils.get(interaction.guild.roles, name=self.values[0])
            await interaction.user.add_roles(colorrole)
            await interaction.message.edit(content=f"Added the {self.values[0]} color role!", view=None)


class SelectView(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)
        self.add_item(SelectColor())


class Button5(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()

    @discord.ui.button(label='4', style=discord.ButtonStyle.green)
    async def opt4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 4
        self.stop()

    @discord.ui.button(label='5', style=discord.ButtonStyle.green)
    async def opt5(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 5
        self.stop()


class Button4(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()

    @discord.ui.button(label='4', style=discord.ButtonStyle.green)
    async def opt4(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 4
        self.stop()


class Button3(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()

    @discord.ui.button(label='3', style=discord.ButtonStyle.green)
    async def opt3(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 3
        self.stop()


class Button2(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()

    @discord.ui.button(label='2', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 2
        self.stop()


class ButtonTest(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='420', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 420
        self.stop()

    @discord.ui.button(label='9211', style=discord.ButtonStyle.green)
    async def opt2(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 9211
        self.stop()


class Button1(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='1', style=discord.ButtonStyle.green)
    async def opt1(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.value = 1
        self.stop()


def format_timestamp(timestring: str):
    time_num_str = ""
    time_unit = ""
    for char in timestring:
        if char in "123456789":
            time_num_str += char
        else:
            time_unit += char
    time_num = int(time_num_str)
    timestamp_dict = {
        "year": 0,
        "month": 0,
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0,
    }
    if time_unit.lower() == "y":
        timestamp_dict["year"] = time_num
    elif time_unit.lower() == "mo":
        timestamp_dict["month"] = time_num
    elif time_unit.lower() == "d":
        timestamp_dict["day"] = time_num
    elif time_unit.lower() == "h":
        timestamp_dict["hour"] = time_num
    elif time_unit.lower() == "m":
        timestamp_dict["minute"] = time_num

    elif time_unit.lower() == "s":
        timestamp_dict["second"] = time_num
    tzinfo = tz.gettz('America/Toronto')
    now = discord.utils.utcnow()

    t_dict = timestamp_dict
    year = now.year + t_dict["year"]
    month = now.month + t_dict["month"]
    day = now.day + t_dict["day"]
    hour = now.hour + t_dict["hour"]
    minute = now.minute + t_dict["minute"]
    second = now.second + t_dict["second"]
    if second > 60:
        minute += 1
        second -= 60
    if minute > 60:
        hour += 1
        minute -= 60
    if hour > 24:
        day += 1
        hour -= 24

    newtime = datetime(year=year, month=month, day=day,
                       hour=hour, minute=minute,
                       second=second, ).astimezone(timezone("Europe/London"))

    return newtime - now


class cog(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('never gonna let you down')

    @commands.hybrid_command(description="Replies with pongs")
    @app_commands.guilds(guild_id)
    async def pings(self, ctx):
        await ctx.send('pongs')

    @commands.hybrid_command()
    @app_commands.guilds(guild_id)
    async def mute(self, ctx, member: discord.Member, time: str = None, reason: str = None):
        await member.timeout(format_timestamp(time), reason=reason)
        embed = discord.Embed(title=f"Muted {member.name}", color=discord.Color.green())

        embed.add_field(name="Time until unmute: ", value=time)
        embed.add_field(name="Muted by: ", value=ctx.author.mention)
        embed.add_field(name="Reason: ", value=reason)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(guild_id)
    async def jin(self, ctx):
        await ctx.send('happy')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def hello(self, ctx):
        await ctx.send('there')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def flame(self, ctx):
        await ctx.send('on')

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def unmute(self, ctx, member: discord.Member):
        await member.timeout(None)
        await ctx.send(f"{member.name} was unmuted")

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def currency(self, ctx, convert: str, amount: int, to: str):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={convert}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "qK21tx0R6l5Age8yx1lppVq4O6tbS3i2"
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        res = response.text
        try:

            result = json.loads(res)

            embed = discord.Embed(
                title=f"{result['query']['amount']} {result['query']['from']} to {result['query']['to']}",
                color=discord.Color.green(), timestamp=datetime.fromtimestamp(int(result['info']['timestamp'])))
            embed.description = f"**{result['result']}**"
            embed.set_footer(text=f"Exchange Rate: {result['info']['rate']}")
            await ctx.send(embed=embed)
        except:
            await ctx.send("There was an error. Make sure you specify the correct three letter code for the currencies")

    @commands.command()
    async def jumbo(self, ctx, emoji: discord.Emoji):
        await ctx.send(emoji.url)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @commands.has_permissions(manage_messages=True)
    async def ban(self, ctx, member: discord.Member, reason: str = None):
        name = member.name
        await member.ban()
        embed = discord.Embed(title=f"Banned {name}", color=discord.Color.green())

        embed.add_field(name="Banned by: ", value=ctx.author.mention)

        embed.add_field(name="Reason: ", value=reason)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @commands.has_permissions(manage_messages=True)
    async def unban(self, ctx, member: discord.Member, reason: str = None):
        await member.unban()
        embed = discord.Embed(title=f"Unbanned user", color=discord.Color.green())
        embed.add_field(name="Unbanned by: ", value=ctx.author.mention)
        embed.add_field(name="Reason: ", value=reason)
        await ctx.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        await ctx.send(member.avatar.url)

    async def timezone_autocomplete(self,
                                    interaction: discord.Interaction,
                                    current: str,
                                    ) -> List[app_commands.Choice[str]]:
        timezones = ["Africa/Abidjan", "Africa/Accra", "Africa/Algiers", "Africa/Bissau", "Africa/Cairo",
                     "Africa/Casablanca", "Africa/Ceuta", "Africa/El_Aaiun", "Africa/Johannesburg", "Africa/Juba",
                     "Africa/Khartoum", "Africa/Lagos", "Africa/Maputo", "Africa/Monrovia", "Africa/Nairobi",
                     "Africa/Ndjamena", "Africa/Sao_Tome", "Africa/Tripoli", "Africa/Tunis", "Africa/Windhoek",
                     "America/Adak", "America/Anchorage", "America/Araguaina", "America/Argentina/Buenos_Aires",
                     "America/Argentina/Catamarca", "America/Argentina/Cordoba", "America/Argentina/Jujuy",
                     "America/Argentina/La_Rioja", "America/Argentina/Mendoza", "America/Argentina/Rio_Gallegos",
                     "America/Argentina/Salta", "America/Argentina/San_Juan", "America/Argentina/San_Luis",
                     "America/Argentina/Tucuman", "America/Argentina/Ushuaia", "America/Asuncion", "America/Atikokan",
                     "America/Bahia", "America/Bahia_Banderas", "America/Barbados", "America/Belem", "America/Belize",
                     "America/Blanc-Sablon", "America/Boa_Vista", "America/Bogota", "America/Boise",
                     "America/Cambridge_Bay", "America/Campo_Grande", "America/Cancun", "America/Caracas",
                     "America/Cayenne", "America/Chicago", "America/Chihuahua", "America/Costa_Rica", "America/Creston",
                     "America/Cuiaba", "America/Curacao", "America/Danmarkshavn", "America/Dawson",
                     "America/Dawson_Creek", "America/Denver", "America/Detroit", "America/Edmonton",
                     "America/Eirunepe", "America/El_Salvador", "America/Fort_Nelson", "America/Fortaleza",
                     "America/Glace_Bay", "America/Goose_Bay", "America/Grand_Turk", "America/Guatemala",
                     "America/Guayaquil", "America/Guyana", "America/Halifax", "America/Havana", "America/Hermosillo",
                     "America/Indiana/Indianapolis", "America/Indiana/Knox", "America/Indiana/Marengo",
                     "America/Indiana/Petersburg", "America/Indiana/Tell_City", "America/Indiana/Vevay",
                     "America/Indiana/Vincennes", "America/Indiana/Winamac", "America/Inuvik", "America/Iqaluit",
                     "America/Jamaica", "America/Juneau", "America/Kentucky/Louisville", "America/Kentucky/Monticello",
                     "America/La_Paz", "America/Lima", "America/Los_Angeles", "America/Maceio", "America/Managua",
                     "America/Manaus", "America/Martinique", "America/Matamoros", "America/Mazatlan",
                     "America/Menominee", "America/Merida", "America/Metlakatla", "America/Mexico_City",
                     "America/Miquelon", "America/Moncton", "America/Monterrey", "America/Montevideo", "America/Nassau",
                     "America/New_York", "America/Nipigon", "America/Nome", "America/Noronha",
                     "America/North_Dakota/Beulah", "America/North_Dakota/Center", "America/North_Dakota/New_Salem",
                     "America/Nuuk", "America/Ojinaga", "America/Panama", "America/Pangnirtung", "America/Paramaribo",
                     "America/Phoenix", "America/Port-au-Prince", "America/Port_of_Spain", "America/Porto_Velho",
                     "America/Puerto_Rico", "America/Punta_Arenas", "America/Rainy_River", "America/Rankin_Inlet",
                     "America/Recife", "America/Regina", "America/Resolute", "America/Rio_Branco", "America/Santarem",
                     "America/Santiago", "America/Santo_Domingo", "America/Sao_Paulo", "America/Scoresbysund",
                     "America/Sitka", "America/St_Johns", "America/Swift_Current", "America/Tegucigalpa",
                     "America/Thule", "America/Thunder_Bay", "America/Tijuana", "America/Toronto", "America/Vancouver",
                     "America/Whitehorse", "America/Winnipeg", "America/Yakutat", "America/Yellowknife",
                     "Antarctica/Casey", "Antarctica/Davis", "Antarctica/DumontDUrville", "Antarctica/Macquarie",
                     "Antarctica/Mawson", "Antarctica/Palmer", "Antarctica/Rothera", "Antarctica/Syowa",
                     "Antarctica/Troll", "Antarctica/Vostok", "Asia/Almaty", "Asia/Amman", "Asia/Anadyr", "Asia/Aqtau",
                     "Asia/Aqtobe", "Asia/Ashgabat", "Asia/Atyrau", "Asia/Baghdad", "Asia/Baku", "Asia/Bangkok",
                     "Asia/Barnaul", "Asia/Beirut", "Asia/Bishkek", "Asia/Brunei", "Asia/Chita", "Asia/Choibalsan",
                     "Asia/Colombo", "Asia/Damascus", "Asia/Dhaka", "Asia/Dili", "Asia/Dubai", "Asia/Dushanbe",
                     "Asia/Famagusta", "Asia/Gaza", "Asia/Hebron", "Asia/Ho_Chi_Minh", "Asia/Hong_Kong", "Asia/Hovd",
                     "Asia/Irkutsk", "Asia/Jakarta", "Asia/Jayapura", "Asia/Jerusalem", "Asia/Kabul", "Asia/Kamchatka",
                     "Asia/Karachi", "Asia/Kathmandu", "Asia/Khandyga", "Asia/Kolkata", "Asia/Krasnoyarsk",
                     "Asia/Kuala_Lumpur", "Asia/Kuching", "Asia/Macau", "Asia/Magadan", "Asia/Makassar", "Asia/Manila",
                     "Asia/Nicosia", "Asia/Novokuznetsk", "Asia/Novosibirsk", "Asia/Omsk", "Asia/Oral",
                     "Asia/Pontianak", "Asia/Pyongyang", "Asia/Qatar", "Asia/Qostanay", "Asia/Qyzylorda", "Asia/Riyadh",
                     "Asia/Sakhalin", "Asia/Samarkand", "Asia/Seoul", "Asia/Shanghai", "Asia/Singapore",
                     "Asia/Srednekolymsk", "Asia/Taipei", "Asia/Tashkent", "Asia/Tbilisi", "Asia/Tehran",
                     "Asia/Thimphu", "Asia/Tokyo", "Asia/Tomsk", "Asia/Ulaanbaatar", "Asia/Urumqi", "Asia/Ust-Nera",
                     "Asia/Vladivostok", "Asia/Yakutsk", "Asia/Yangon", "Asia/Yekaterinburg", "Asia/Yerevan",
                     "Atlantic/Azores", "Atlantic/Bermuda", "Atlantic/Canary", "Atlantic/Cape_Verde", "Atlantic/Faroe",
                     "Atlantic/Madeira", "Atlantic/Reykjavik", "Atlantic/South_Georgia", "Atlantic/Stanley",
                     "Australia/Adelaide", "Australia/Brisbane", "Australia/Broken_Hill", "Australia/Darwin",
                     "Australia/Eucla", "Australia/Hobart", "Australia/Lindeman", "Australia/Lord_Howe",
                     "Australia/Melbourne", "Australia/Perth", "Australia/Sydney", "CET", "CST6CDT", "EET", "EST",
                     "EST5EDT", "Etc/GMT", "Etc/GMT+1", "Etc/GMT+10", "Etc/GMT+11", "Etc/GMT+12", "Etc/GMT+2",
                     "Etc/GMT+3", "Etc/GMT+4", "Etc/GMT+5", "Etc/GMT+6", "Etc/GMT+7", "Etc/GMT+8", "Etc/GMT+9",
                     "Etc/GMT-1", "Etc/GMT-10", "Etc/GMT-11", "Etc/GMT-12", "Etc/GMT-13", "Etc/GMT-14", "Etc/GMT-2",
                     "Etc/GMT-3", "Etc/GMT-4", "Etc/GMT-5", "Etc/GMT-6", "Etc/GMT-7", "Etc/GMT-8", "Etc/GMT-9",
                     "Etc/UTC", "Europe/Amsterdam", "Europe/Andorra", "Europe/Astrakhan", "Europe/Athens",
                     "Europe/Belgrade", "Europe/Berlin", "Europe/Brussels", "Europe/Bucharest", "Europe/Budapest",
                     "Europe/Chisinau", "Europe/Copenhagen", "Europe/Dublin", "Europe/Gibraltar", "Europe/Helsinki",
                     "Europe/Istanbul", "Europe/Kaliningrad", "Europe/Kiev", "Europe/Kirov", "Europe/Lisbon",
                     "Europe/London", "Europe/Luxembourg", "Europe/Madrid", "Europe/Malta", "Europe/Minsk",
                     "Europe/Monaco", "Europe/Moscow", "Europe/Oslo", "Europe/Paris", "Europe/Prague", "Europe/Riga",
                     "Europe/Rome", "Europe/Samara", "Europe/Saratov", "Europe/Simferopol", "Europe/Sofia",
                     "Europe/Stockholm", "Europe/Tallinn", "Europe/Tirane", "Europe/Ulyanovsk", "Europe/Uzhgorod",
                     "Europe/Vienna", "Europe/Vilnius", "Europe/Volgograd", "Europe/Warsaw", "Europe/Zaporozhye",
                     "Europe/Zurich", "HST", "Indian/Chagos", "Indian/Christmas", "Indian/Cocos", "Indian/Kerguelen",
                     "Indian/Mahe", "Indian/Maldives", "Indian/Mauritius", "Indian/Reunion", "MET", "MST", "MST7MDT",
                     "PST8PDT", "Pacific/Apia", "Pacific/Auckland", "Pacific/Bougainville", "Pacific/Chatham",
                     "Pacific/Chuuk", "Pacific/Easter", "Pacific/Efate", "Pacific/Enderbury", "Pacific/Fakaofo",
                     "Pacific/Fiji", "Pacific/Funafuti", "Pacific/Galapagos", "Pacific/Gambier", "Pacific/Guadalcanal",
                     "Pacific/Guam", "Pacific/Honolulu", "Pacific/Kiritimati", "Pacific/Kosrae", "Pacific/Kwajalein",
                     "Pacific/Majuro", "Pacific/Marquesas", "Pacific/Nauru", "Pacific/Niue", "Pacific/Norfolk",
                     "Pacific/Noumea", "Pacific/Pago_Pago", "Pacific/Palau", "Pacific/Pitcairn", "Pacific/Pohnpei",
                     "Pacific/Port_Moresby", "Pacific/Rarotonga", "Pacific/Tahiti", "Pacific/Tarawa",
                     "Pacific/Tongatapu", "Pacific/Wake", "Pacific/Wallis", "WET"]
        return [
            app_commands.Choice(name=timezone, value=timezone)
            for timezone in timezones if current.lower() in timezone.lower()
        ]

    @app_commands.command()
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.autocomplete(timezone=timezone_autocomplete)
    async def now(self, interaction: discord.Interaction, timezone: str):
        url = f"https://worldtimeapi.org/api/timezone/{timezone}"
        res = requests.get(url)
        result = json.loads(res.text)
        time = result['datetime'][11:16]
        date = result['datetime'][0:10]
        tz = result['abbreviation']
        embed = discord.Embed(title=f"Current time in {timezone}", color=discord.Color.green())
        embed.add_field(name="Time: ", value=f"**{time}**")
        embed.add_field(name="Date:", value=f"**{date}**")
        embed.add_field(name="Timezone: ", value=f"**{tz}**")
        await interaction.response.send_message(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    @app_commands.describe(timezones="Select timezone to view the current time in that timezone")
    @app_commands.choices(timezones=[
        Choice(name='EST', value="America/Toronto"),
        Choice(name='PST', value="America/Vancouver"),
        Choice(name='CST', value="America/Chicago"),
        Choice(name='Indian Time', value="Asia/Kolkata"),
        Choice(name="South Africa", value="Africa/Johannesburg"),
        Choice(name="UAE", value="Asia/Dubai"),
        Choice(name='Br*tish Time', value="Europe/London"),

    ])
    async def time(self, interaction: discord.Interaction, timezones: Choice[str]):
        fmt = "%Y-%m-%d %H:%M %Z%z"
        fmt1 = "%H:%M"
        fmt2 = "%Y-%m-%d"

        time_tz = datetime.now(tz=timezone(timezones.value))
        time_to_send = time_tz.strftime(fmt1)
        date_to_send = time_tz.strftime(fmt2)
        #  await interaction.send(f"Current time({timezones.name})- **{time_tz.strftime(fmt1)}**")
        embed = discord.Embed(title=f"Current Time({timezones.name})", description=f"**Time:** {time_to_send}\n**Date"
                                                                                   f":** {date_to_send}",
                              colour=discord.Color.green())
        await interaction.send(embed=embed)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def color(self, ctx):
        view = discord.ui.View().add_item(SelectColor())
        await ctx.send(view=view)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def countdown(self, ctx, yy, mm, dd):

        delta = datetime(int(yy), int(mm), int(dd), 0, 0) - datetime.now()
        eldendays = str(delta.days) + " days "
        count = 0
        for i in range(len(str(delta)) - 1):
            if str(delta)[i] == ",":
                count = i + 2
        x = str(delta)[count:]
        y = x.split(":")

        eldenhours = f"{y[0]} hours {y[1]} minutes {round(float(y[2]))} seconds"
        eldentime = eldendays + eldenhours

        await ctx.send(fr"Time until {yy}/{mm}/{dd}: {eldentime}")

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def game(self, ctx, *, game: str):
        search = SearchGame(game).results

        search_results = ""
        for i in range(len(search)):
            game = search[i]
            platforms = []
            platform_data = game["game"]["platforms"]
            for platform in platform_data:
                platforms.append(platform["name"])

            platform_string = ", ".join(platforms)
            search_results += f"**{i + 1}. {game['name']}**\n{platform_string}\n\n"

        embed = discord.Embed(title="Search Results", description=search_results, colour=discord.Color.green())
        view = Button5()
        message = await ctx.send(embed=embed, view=view)
        await view.wait()
        opt = view.value

        game_id = search[opt - 1]["game"]["id"]

        print(game_id)
        game = Game(game_id)
        embed = discord.Embed(title=game.name,
                              description=f"**Description: **\n{game.description}\n\n**Release Date: **{game.date}\n\n**Genres: **{game.genres}\n\n**Platforms: **{game.platforms}\n\n**Developers/Publishers: **{game.devs}\n\n**Rating: **{game.rating}",
                              colour=discord.Color.green())
        embed.set_thumbnail(url=game.cover)
        await message.edit(embed=embed, view=None)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def button(self, ctx):
        view = ButtonTest()
        m = await ctx.send("Hello", view=view)

        await view.wait()
        opt = view.value
        await m.edit(content=f"You chose {opt}", view=None)

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def prepare(self, ctx: commands.Context):
        embed = discord.Embed(title="Self Roles",
                              description="**Announcements:** Get notified for server announcements!\n**Movies:** Get "
                                          "notified when we're watching a movie!\n**Games:** Get notified when we're "
                                          "trying to play a game together!\n**Polls:** Get notified for "
                                          "polls!\n**Fortnite:** Get notified when we're playing Fortnite!")
        await ctx.send(embed=embed, view=PersistentView())

    @commands.hybrid_command()
    @app_commands.guilds(MY_GUILD_ID)
    async def pingping(self, ctx: commands.Context):
        await ctx.send("pongpong")

    @commands.hybrid_command()
    async def globalcommand(self, ctx: commands.Context):
        await ctx.send("this is a global command")

    async def cog_load(self):
        ...


async def setup(client):
    await client.add_cog(cog(client))
