import os
import hikari

TOKEN = os.environ['DISCORD_TOKEN']
bot = hikari.GatewayBot(token=TOKEN)

@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started')

bot.run()
