import discord
import os 
import asyncio
import random
import time
import pymongo
import datetime
from discord.ext import commands
from pymongo import MongoClient
from datetime import datetime

client = commands.Bot(command_prefix='{')
#client.remove_command('help')

db=cluster["Discord_bot"]
bot_servers=db["servers"]
bot_stats = db["stats"]

@client.event
async def on_ready():
        await client.change_presence(activity=discord.Game("Darbouka"),status=discord.Status.do_not_disturb)
        print('bot is Ready')

@client.event
async def on_guild_join(guild):
        print('i joined a new server')
        serv = {"server name " : str(guild.name) , "server id" : str(guild.id) , "region": str(guild.region) , "owner" : str(guild.owner)}
        bot_servers.insert_one(serv)
        print("server added successfully ! ")


@client.event
async def on_member_join(member):
        guild=member.guild
        role = discord.utils.get(guild.roles, name="DJ")
        await member.add_roles(role,reason=None,atomic=True)
        channel = member.guild.system_channel
        stat = {"member_server_id" : str(member.guild.id),"server name " : str(member.guild.name) ,"member name" : str(member) ,"member_id":str(member.id),"messages sent": 0,"commands sent": 0 }
        bot_stats.insert_one(stat)
        await channel.send(f"mar7ba bik fel serveur {member.mention}")
        print("member added successfully with score 0 ! ")
        print(f'{member} has joined the server.')
@client.event
async def on_member_remove(member):
        channel = member.guild.system_channel
        bot_stats.delete_one({"member_server_id" : str(member.guild.id),"member_id": str(member.id)})
        await channel.send(f"Fel khir nchallah ya {str(member.display_name)}")
        print("member deleted successfully ! ")
        print(f'{member} has left the serever.')

@client.command()
async def ping(ctx):
        em=discord.Embed(color=discord.Color.red())
        em.title = f' :stopwatch: Ping : {round(client.latency * 1000 )}ms :stopwatch:'
        await ctx.send(embed=em)


@client.command()
@commands.has_permissions(manage_messages=True)
async def fasakh(ctx,amount : int):
        await ctx.channel.purge(limit=amount+1)
@fasakh.error
async def fasakh_error(ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.send('9adeh men message t7eb tfasakh !?')

@client.command()
@commands.has_permissions(kick_members=True)
async def tjabbed(ctx, member : discord.Member ,*, reason='oumour zabby'):
      await member.kick(reason=reason)

@tjabbed.error
async def tjabbed_error(ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Maandekch permission :/')

@client.command()
async def chalghoum(ctx):
        em=discord.Embed(color=0xFF0000)
        em.title = "<:mus:712708785491279893> Mar7ba Bik!  <:mus:712708785491279893> "
        em.description = "menu"
        await ctx.send(" marhba bik ! tnjame testaamel el bot bel { ")


@client.command()
async def csgo(ctx,pass_context = True , aliases=['cs','Csgo','sp_cs']):
        em=discord.Embed(color=0xd4af37)
        em.title = "<:csgo:714247876691099679> Spray & Pray Official CSGO Roster  <:csgo:714247876691099679>"
        em.description = f''' **🇨 Alzomra**
                                        ✅ **𝑆 ƙ ! Ɲ α ツ**
                                        ✅**Bloody Pizza**
                                        ✅ **ZuKoViC**
                                        ✅ **Brick's**
                                        
                                        🔁 sub 1       
                                        🔁 sub 2
                                        🔁 sub 3 
                                        🔁 sub 4
                                        🔁 sub 5     '''
        #em.set_image(url="https://cdn.discordapp.com/attachments/712096475806564405/713063877058887790/csgo.png")
        await ctx.send(embed=em) 

@client.command()
async def rl(ctx,pass_context = True , aliases=['sp_rl']):
        em=discord.Embed(color=0x0A48F3)
        em.title = "<:rl:712468020399702036> Spray & Pray Official Rocket League Roster <:rl:712468020399702036>"
        em.description = f""" **🇨 Alzomra**
                                        ✅   **Broken Controlla**
                                        ✅   **Danter**
                                        
                                        🔁 sub 1       
                                        🔁 sub 2
                                        🔁 sub 3    """
        #em.set_image(url="https://cdn.discordapp.com/attachments/709758941956931599/713455918422949930/rl.png")
        await ctx.send(embed=em)

@client.event
async def on_raw_reaction_add(payload):
        print(payload.emoji.name)
        print(str(payload.member.guild))
        guild = payload.member.guild
        channels = guild.text_channels
        for channel in channels :
               if str(channel) == "general":
                  message_id = await channel.pins()
                  for ids in message_id :
                     print (ids)
        member = payload.member
        print(str(payload.emoji))
        if   payload.message_id == ids.id : 
                print("Initiating role select")
                if payload.emoji.name == "csgo" : 
                        role = discord.utils.get(guild.roles, name="Csgo")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("csgo role added")
                elif   payload.emoji.name == "rl" :
                        role = discord.utils.get(guild.roles, name="Rl")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("rocket league role added")
                elif   payload.emoji.name == "valorant" :
                        role = discord.utils.get(guild.roles, name="Valorant")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("Valorant role added")
                elif   payload.emoji.name == "fortnite" :
                        role = discord.utils.get(guild.roles, name="Fortnite")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("Fortnite role added")
                elif   payload.emoji.name == "pubg" :
                        role = discord.utils.get(guild.roles, name="PUBG")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("pubg role added")
                elif   payload.emoji.name == "r6" :
                        role = discord.utils.get(guild.roles, name="R6")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("R6 siege role added")
                elif   payload.emoji.name == "lol" :
                        role = discord.utils.get(guild.roles, name="LOL")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("League of legends role added")
                elif   payload.emoji.name == "gtav" :
                        role = discord.utils.get(guild.roles, name="GTA V")
                        await member.add_roles(role,reason=None,atomic=True)
                        print("Gta V role added")



@client.command()
async def stat(ctx, member : discord.Member):
        stat = bot_stats.find_one({"member_server_id" : str(member.guild.id),"member_id": str(member.id)})
        x = member == member.guild.owner
        own = "Mala zebby Hou ! " if x else "La :("
        msgs = stat["messages sent"]
        comms = stat["commands sent"]
        roles = [role for role in member.roles]
        roles.pop(0)
        color = random.randint(0, 0xFFFFFF)
        em = discord.Embed(color = color)
        em.title = f"**Member Stats - **  {member.display_name}"
        em.timestamp = datetime.today()
        em.set_footer(text = f"EL nasnes {ctx.author}", icon_url= ctx.author.avatar_url)  
        em.set_thumbnail(url = member.avatar_url)
        em.add_field(name ="Dkhal lel serveur fi ",value =f"{member.joined_at}", inline=False)
        em.add_field(name ="9adeh baath men msg",value =f"{msgs}", inline=False)
        em.add_field(name ="9adeh etsaamel men commande",value =f"{comms}", inline=False)
        em.add_field(name =f"Roles ({len(roles)})",value ="  -  ".join([str(role) for role in roles]), inline=False)
        em.add_field(name ="Moula el Moul ?",value =f"{own}", inline=False)
        await ctx.send(embed=em)

@client.command()
async def sp(ctx):
        em = discord.Embed(color = 0xFFFFFF)
        em.title = "SPRAY & PRAY OFFICIAL SOCIAL MEDIAS"
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/425377132114608149/712723944574156850/sp-logo-monogram-triangle-shape-circle-rounded-isolated-gold-colors-style-black-background-design-te.png")
        em.add_field(name ="‎",value = ":white_check_mark: [SPRAY & PRAY FACEBOOK PAGE](https://www.facebook.com/Spray-And-Pray-106373441091998/?notif_id=1590371165383592&notif_t=page_fan)")
        em.add_field(name ="‎",value = ":white_check_mark: [SPRAY & PRAY STEAM GROUP](http://steamcommunity.com/groups/)", inline=False)
        #em.add_field(name ="‎",value = ":white_check_mark: [SPRAY & PRAY YOUTUBE CHANNEL (coming soon ...)](http://steamcommunity.com/groups/)", inline=False)
        await ctx.send(embed=em)


@client.command()
@commands.has_role('Bot tester')
async def reload(ctx,extension):
   client.reload_extension(f'cogs.{extension}')

@reload.error
async def reload_error(ctx,error): 
      await ctx.send('kahtinek el fazet hedhhom ...')


async def on_message(message):
        verify = bot_stats.find_one({"member_server_id" : str(message.guild.id),"member_id": str(message.author.id)})
        if bool(verify):
           bot_stats.update_one({"member_server_id" : str(message.guild.id),"member_id": str(message.author.id)}, {"$inc":{"messages sent":1}})
           print("member upadated successfully ! ")
        else :
           stat = {"member_server_id" : str(message.guild.id),"server name " : str(message.guild.name) ,"member name" : str(message.author) ,"member_id":str(message.author.id),"messages sent": 1,"commands sent": 0 }
           bot_stats.insert_one(stat)
           print("new member added & upadated successfully ! ")
        msg = "{" in message.content
        if msg : 
            bot_stats.update_one({"member_server_id" : str(message.guild.id),"member_id": str(message.author.id)}, {"$inc":{"commands sent":1}})
            print("member upadated successfully (command incremented) ! ")


@client.event
async def on_command_error(ctx,error):
        if isinstance(error, commands.CommandNotFound):
                print("command not found")
                await ctx.send("commande mouch mawjouda ... ")
                await ctx.send_help()



client.add_listener(on_message)



client.run('Token')