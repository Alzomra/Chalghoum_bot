@client.command()
@commands.has_permissions(administrator=True)
async def roster(ctx,*,command):
        command = command.strip()
        command = command.split()
        game = command[0]
        command.remove(game)
        verify = roster_db.find_one({"member_server_id" : str(ctx.guild.id),"game": game})
        if bool(verify) :
                roster_db.update_one({"member_server_id" : str(ctx.guild.id),"game": game}, {"$set" : {"players" : command }}) 
        else :
                ros = {"member_server_id" : str(ctx.guild.id),"game": game, "players" : command }
                roster_db.insert_one(ros)


@client.command()
async def game(ctx,pass_context = True):
        roster = roster_db.find_one({"member_server_id" : str(ctx.guild.id),"game": 'csgo'})
        if bool(roster) :
                players = roster['players']
                em=discord.Embed(color=0xd4af37)
                em.title = f"{str(ctx.guild)} Official CSGO Roster"
                em.description = f''' **🇨 {players[0]}**
                                        ✅ **{players[1]}**
                                        ✅ **{players[2]}**
                                        ✅ **{players[3]}**
                                        ✅ **{players[4]}**'''
                em.set_thumbnail(url="https://cdn.discordapp.com/attachments/712096475806564405/713063877058887790/csgo.png")
                await ctx.send(embed=em) 
        else : 
               await ctx.send("Roster Not Found")                