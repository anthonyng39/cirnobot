import os
import hikari
import lightbulb

TOKEN = os.environ['DISCORD_TOKEN']
bot = lightbulb.BotApp(
    token=TOKEN,
    default_enabled_guilds=(931786079193931778)
)

# @bot.listen(hikari.GuildMessageCreateEvent)
# async def print_message(event):
#     print(event.content)

@bot.command
@lightbulb.command('ping', 'Says pong')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')

@bot.command
@lightbulb.option('message', 'text you want Cirno to say', type=str)
@lightbulb.command('say', 'Make Cirno say epic thing')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    # print(ctx.options.message)
    await ctx.respond(ctx.options.message)

@bot.command
@lightbulb.command('perfectmathclass', 'Cirno (genius) will perform math operations')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def math(ctx):
    pass 

@math.child
@lightbulb.option('num2', 'The second number', type=float)
@lightbulb.option('num1', 'The first number', type=float)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def add(ctx):
    num1 = str(ctx.options.num1)
    num2 = str(ctx.options.num2)
    answer = str(ctx.options.num1 + ctx.options.num2)
    response = num1 + '+' + num2 + '=' + answer
    await ctx.respond(response)

@math.child
@lightbulb.option('num2', 'The second number', type=float)
@lightbulb.option('num1', 'The first number', type=float)
@lightbulb.command('multiply', 'Multiply two numbers together')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiply(ctx):
    num1 = str(ctx.options.num1)
    num2 = str(ctx.options.num2)
    answer = str(ctx.options.num1 * ctx.options.num2)
    response = num1 + '*' + num2 + '=' + answer
    await ctx.respond(response)

bot.run()
