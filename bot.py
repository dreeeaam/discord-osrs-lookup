import requests, json

import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='$')

rs_statsURL = 'https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player='

# Commands
@bot.command()
async def stats(ctx, arg):
    username = arg # $stats <username>
    stats = GetStats.Stats(username)
    await ctx.send(stats)

class GetStats:
    def Stats(username):
        rawStats = GetStats._findPlayer(username)
        stats    = GetStats._sortStats(username, rawStats)
        return stats
    
    def _findPlayer(username):
        link = rs_statsURL + username
        response = requests.get(link)
        return response.content.decode('utf-8')

    def _sortStats(username, rawStats):
        statsList = iter(rawStats.splitlines())

        with open('player-levels.json') as json_file:
            data = json.load(json_file)

            for skill in data['skills']:
                stat = statsList[0].split(',')
                skill['level'] = stat[1]
                skill['xp'] = stat[2]

            with open(username + '.json', 'w') as outfile:
                json.dump(data, outfile)

            

        


bot.run('NDE5MTIyNTI5NDgzODgyNDk3.XfkFbA.S2dmqzwwU1cfvK-y3ITzakAxayY')