@client.command()
async def channel(ctx, *args : discord.Member):
        await fasakh(ctx = ctx , amount = 0)
        guild=ctx.message.guild
        number = random.randint(1111,9999)
        chname = "C_S #" + str(number)
        rolename = "C_R #" + str(number)
        print(rolename)
        print(chname)
        await guild.create_role(name = rolename, colour = discord.Color.gold() ,  hoist = False, reason ="Custom role for custom channel")
        await guild.create_voice_channel(name = chname, overwrites=None , category=None , reason=None,bitrate = 64000 , user_limit = 5,)
        for ch in  guild.voice_channels : 
                if str(ch) == chname :
                   newch = ch 
                   print(newch.name)

        ev = guild.roles[0]
        role = discord.utils.get(guild.roles, name=rolename)
        await newch.set_permissions(role, view_channel = True , connect = True)
        await newch.set_permissions(ev, view_channel = False , connect = True)
        
        for mem in args :
          await mem.add_roles(role,reason=None,atomic=True)
                

@client.event
async def on_voice_state_update(member,before,after):
      print("member conncted")
      chx = member.guild.voice_channels
      for ch in chx : 
          print(str(ch))
          if ch.members == [] :
            print("channel empty")
            if "C_S #" in str(ch.name) :
                print("channel found")
                await ch.delete(reason ="out of service")
                print("channel deleted")
                rlname = "C_R #" + str(ch)[-4:]
                print(rlname)
                role = discord.utils.get(member.guild.roles, name=rlname)
                print(role)
                await role.delete(reason = None)
                print("role deleted")
