client.command()
@commands.has_permissions(administrator=True)
async def roster_set(ctx,*,command):
        command = command.strip()
        command = command.split()
        game = command[0]
        command.remove(game)
        game = game.upper()
        if "https" not in command[len(command)-1] : 
                command.append("https://cdn.discordapp.com/attachments/712097123906093146/736316563786825748/moustache_PNG38.png")
        verify = roster_db.find_one({"roster_server_id" : str(ctx.guild.id),"game": game})
        if bool(verify) :
                roster_db.update_one({"roster_server_id" : str(ctx.guild.id),"game": game}, {"$set" : {"players" : command }}) 
        else :
                ros = {"roster_server_id" : str(ctx.guild.id),"roster_server_name" : str(ctx.guild),"game": game, "players" : command }
                roster_db.insert_one(ros)
@roster_set.error
async def roster_error(ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Barra dez doura khirlek...')

@client.command()
async def roster(ctx,*,game):
        game = game.strip()
        game = game.upper()
        roster = roster_db.find_one({"roster_server_id" : str(ctx.guild.id),"game": game})
        if bool(roster) :
                players = roster['players']
                em=discord.Embed(color=0xd4af37)
                em.title = f"{str(ctx.guild)} Official {game} Roster"
                em.add_field(name =f"**🇨 {players[0]}**" , value="‎‎‎" , inline=False )
                players.remove(players[0])
                i=0
                if len(players) < 2 :   
                   em.set_thumbnail(url=players[0])    
                else :     
                 for  i in range(len(players)-1) : 
                         em.add_field(name =f"**✅ {players[i]}**" , value="‎" , inline=False )
                 em.set_thumbnail(url=players[i+1])
                await ctx.send(embed=em) 
        else : 
               await ctx.send("Roster Not Found")

@client.command()
async def rosters(ctx):
 doc = roster_db.find({"roster_server_id" : str(ctx.guild.id)})
 rosters =[]
 for d in doc : 
         rosters.append(f"{d['game']}")
 if bool(doc) :
        em = discord.Embed(color =0xd4af37)
        em.title = f"{str(ctx.guild)}'s Game Rosters"   
        if len(rosters) > 0 : 
         for  i in range(len(rosters)) : 
                         em.add_field(name =f"**{rosters[i]}**" , value="‎" , inline=False )
                         em.set_thumbnail(url=ctx.guild.icon_url)
        else :
                em.add_field(name =f"** NO ROSTERS FOUND**" , value="‎" , inline=False )  
 else : 
        em.add_field(name =f"** NO ROSTERS FOUND**" , value="‎" , inline=False )
        
 em.set_thumbnail(url=ctx.guild.icon_url)
 await ctx.send(embed=em) 