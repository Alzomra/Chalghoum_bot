# Chalghoum (Tunisian discord bot)
  Hello everyone ! This is the official repo of my discord bot "CHALGHOUM" , and its my first project using python and discord.py rewrite version. 

# Chalghoums commands List : 
## E-SPORTS

### Server rosters : 

 - roster_set <game> [Names] <image_link>  : sets custom roster
   example : {roster_set RL player1 player2 https://image_url // creates a roster named RL with the mentionned players.
 - roster <game> :  displays game roster
  {roster RL // Displays RL roster 
 - rosters :  displays all server rosters
  
### Server Tournaments : 
  NOTE : ONE ACTIVE TOURNAMENT PER SERVER.
 - start <tournament name> [players per team] 
   example : {start Rocket_league 2 // Starts a Rocket_league tournament with 2 players per team.
 - register <team_name> [players]
   example : {register Cloud9 Chandler Danter // regiters team in the server's active tournament
 - teams : displays registered teams in active tournaments
 - generate : generates & displays groups with registered teams
 - groups : Displays groups with registered teams
 - generate_matches : generates & displays all matches for each group
 - matches : Displays all matches for each group
 - start_match <group number> <match number> : starts targeted match and moves each team's players to custom channels 
   example : start_match 

## MODERATION 

 - Ban @User : Bans member from voice channels
 - Unban @User : Unbans member from voice channels
 - Bans : List of banned member from voice channels

## CUSTOM ROLE FOR NEW MEMBERS

 - default_role Role_name : sets custom role to assign 		for new members (default is DJ)
 - default_role : Shows current custom role
 
 
 ## WELCOME AND GOODBYE CUSTOM MESSGAES
 
  - set_welcome  : sets custom server welcome message
  - welcome : displays current server welcome message
  - toggle_welcome : Toggles ON / OFF custom message 
  
  - set_leave  : sets custom server welcome message
  - leave : displays current server welcome message
  - toggle_leave : Toggles ON / OFF custom message
  
## UTILITIES

 - Corona <country> : Corona virus info
 - ping : Bot ping
 - stat @[member] : Member Stats
 - fasakh <number> :  delete messages
 - tjabbed @[member]  : kick member from server
 - channel @[members]  : Custom Private channel that deletes itself after all members leave it 


## GAMES

 - blackjack @[members]  : Blackjack !
 - flip <credit> : Coin Flip 50/50!
 - flous  : your credits !
 - Bonus  : Bonus credits every 24h !
