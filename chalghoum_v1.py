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
client.remove_command('help')


db=cluster["Discord_bot"]
bot_servers=db["servers"]
bot_stats = db["stats"]

@client.event
async def on_ready():
        await client.change_presence(activity=discord.Game("Jalel Labes aalih"),status=discord.Status.do_not_disturb)
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
        em.description = f''' **🇨 None**
                                        ✅ **None**
                                        ✅**None**
                                        ✅ **None**
                                        ✅ **None**
                                        
                                        🔁 Sub 1     
                                        🔁 Sub 2
                                        🔁 Sub 3
                                        🔁 Sub 4
                                        🔁 Sub 5   '''
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/712096475806564405/713063877058887790/csgo.png")
        await ctx.send(embed=em) 

@client.command()
async def rl(ctx,pass_context = True , aliases=['sp_rl']):
        em=discord.Embed(color=0x0A48F3)
        em.title = "<:rl:712468020399702036> Spray & Pray Official Rocket League Roster <:rl:712468020399702036>"
        em.description = f""" **🇨 Alzomra**
                                        ✅   **Broken Controlla**
                                        ✅   **Danter**
                                        
                                        🔁 13      
                                        🔁 RifleEZ 
                                        🔁 SPCTREDALI   """
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/709758941956931599/713455918422949930/rl.png")
        await ctx.send(embed=em)


@client.command()
async def valo(ctx,pass_context = True , aliases=['cs','Csgo','sp_cs']):
        em=discord.Embed(color=0xE2124E)
        em.title = "Spray & Pray Official VALORANT Roster"
        em.description = f''' **🇨 None**
                                        ✅ **None**
                                        ✅**None**
                                        ✅ **None**
                                        ✅ **None**
                                        
                                        🔁 Sub 1     
                                        🔁 Sub 2
                                        🔁 Sub 3
                                        🔁 Sub 4
                                        🔁 Sub 5   '''
        em.set_thumbnail(url="https://cdn.discordapp.com/attachments/712097123906093146/717800350173626438/gi0mAjIh_400x400.png")
        await ctx.send(embed=em)

@client.event
async def on_raw_reaction_add(payload):
        guild = payload.member.guild
        channel = guild.get_channel(payload.channel_id)
        member = payload.member
        if    str(channel) == "𝐀𝐔𝐓𝐎-𝐑𝐎𝐋𝐄𝐒" : 
                rolename = str(payload.emoji.name)
                role = discord.utils.get(guild.roles, name=rolename)
                if role != None : 
                 await member.add_roles(role,reason=None,atomic=True)
                 print(f'{rolename} added to {member.display_name}')



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
        em.add_field(name ="‎",value = ":white_check_mark: [SPRAY & PRAY STEAM GROUP](http://steamcommunity.com/groups/sprayandpray)", inline=False)
        #em.add_field(name ="‎",value = ":white_check_mark: [SPRAY & PRAY YOUTUBE CHANNEL (coming soon ...)](http://steamcommunity.com/groups/)", inline=False)
        await ctx.send(embed=em)


async def on_message(message):

        verify = bot_stats.find_one({"member_server_id" : str(message.guild.id),"member_id": str(message.author.id)})
        if bool(verify):
           bot_stats.update_one({"member_server_id" : str(message.guild.id),"member_id": str(message.author.id)}, {"$inc":{"messages sent":1}})
           print("member upadated successfully ! ")
        else :
           stat = {"member_server_id" : str(message.guild.id),"server name " : str(message.guild.name) ,"member name" : str(message.author) ,"member_id":str(message.author.id),"messages sent": 1,"commands sent": 0 }
           bot_stats.insert_one(stat)
           print("new member added & upadated successfully ! ")
        if  not "Chalghoum" in str(message.author):
         if len(message.content) > 2 : 
          if "{" == message.content[0] : 
            bot_stats.update_one({"member_server_id" : str(message.guild.id),"member_id": str(message.author.id)}, {"$inc":{"commands sent":1}})
            print("member upadated successfully (command incremented) ! ")
            print (str(message.author))

@client.event
async def on_command_error(ctx,error):
        if isinstance(error, commands.CommandNotFound):
                print("command not found")
                await ctx.send("commande mouch mawjouda ... ")
                await help(ctx=ctx)


@client.command()
async def source(ctx):
        em = discord.Embed(color = 0x6EEAFF)
        em.title = "Source Code : "
        em.url = "https://github.com/Alzomra/Chalghoum_bot/tree/master"
        await ctx.send(embed = em)


@client.command()
@commands.has_permissions(manage_channels=True)
async def channel(ctx, *args : discord.Member):
        await fasakh(ctx = ctx , amount = 0)
        guild=ctx.message.guild
        number = random.randint(1000,9999)
        chname = "C_C #" + str(number)
        rolename = "C_R #" + str(number)
        await guild.create_role(name = rolename, colour = discord.Color.gold() ,  hoist = False, reason ="Custom role for custom channel")
        print(f'Custom role {rolename} created ...')
        await guild.create_voice_channel(name = chname, overwrites=None , category=None , reason=None,bitrate = 64000 , user_limit = 5,)
        print(f'Custom channel {chname} created ...')
        for ch in  guild.voice_channels : 
                if str(ch) == chname :
                   newch = ch 

        ev = guild.roles[0]
        role = discord.utils.get(guild.roles, name=rolename)
        await newch.set_permissions(role, view_channel = True , connect = True)
        await newch.set_permissions(ev, view_channel = False , connect = True)
        
        for mem in args :
          await mem.add_roles(role,reason=None,atomic=True)
          await mem.move_to(newch)
@channel.error
async def channel_error(ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Maandekch permission bech taamel custom channel ... a7ki maa el Owners')



@client.event
async def on_voice_state_update(member,before,after):
    print("voice activity")
    if str(before.channel) != str(after.channel):
          ch = before.channel
          if ch != None : 
            if ch.members == [] and ("C_C" in str(ch)):
                print("custom channel found empty")
                await ch.delete(reason ="out of service")
                print(f"{str(ch)} deleted successfully")
                rlname = "C_R #" + str(ch)[-4:]
                role = discord.utils.get(member.guild.roles, name=rlname)
                await role.delete(reason = None)
                print(f"{role} role deleted")

     


@client.command()
async def help(ctx): 
        em = discord.Embed(color = 0xE23412)
        em.title = "Chalghoums commands List : (estaamel '{')"
        em.set_footer(text = f"help for {ctx.author}", icon_url= ctx.author.avatar_url)
        em.add_field(name ='**Channel**' , value = "Custom temporary voice channel (with custom role)", inline=False)
        em.add_field(name ='**rl**' , value = "Tachkilet el rocket league mtaa  S&P", inline=False)
        em.add_field(name ='**csgo**' , value = "Tachkilet el CS:GO mtaa  S&P", inline=False)
        em.add_field(name ='**sp**' , value = "Socials mtaa S&P", inline=False)
        em.add_field(name ='**ping**' , value = "twarik el ping mtaa el bot", inline=False)
        em.add_field(name ='**stat**' , value = "Stats mtaa ay membre fel serveur", inline=False)
        em.add_field(name ='**fasakh <number>**' , value = "Tfasakh messaget ", inline=False)
        em.add_field(name ='**tjabbed**' , value = "Tkharraj membre mel serveur", inline=False)
        await ctx.send(embed= em )

client.add_listener(on_message)



client.run(TOKEN)
