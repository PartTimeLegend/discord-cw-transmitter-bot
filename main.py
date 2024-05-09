import discord
import logging
import os
from discord_bot import DiscordBot
from database_manager_factory import DatabaseManagerFactory
from radio_controller_factory import RadioControllerFactory
from morse_code import load_morse_code_dict

logging.basicConfig(level=logging.INFO)

def convert_to_cw(message, morse_code_dict):
    cw_message = ''
    for char in message.upper():
        if char in morse_code_dict:
            cw_message += morse_code_dict[char] + ' '
        else:
            cw_message += ' '
    return cw_message.strip()

def transmit_message(ctx, frequency, message, db_manager, morse_code_dict, radio_controller):
    sender = ctx.author.name
    cw_message = convert_to_cw(message, morse_code_dict)
    radio_controller.send_message_to_radio(frequency, cw_message)

    with db_manager as db:
        db.insert_transmission(sender, frequency, message, cw_message)

    logging.info(f"Message transmitted on frequency {frequency} kHz in CW: {cw_message}")
    return f"Message transmitted on frequency {frequency} kHz in CW: {cw_message}"

def main():
    discord_token = os.getenv('DISCORD_TOKEN')
    database_config = {
        'host': os.getenv('DB_HOST'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME')
    }

    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.members = True

    bot = DiscordBot(command_prefix='!', discord_token=discord_token, intents=intents)
    db_manager = DatabaseManagerFactory.create_database_manager(database_config)
    morse_code_dict = load_morse_code_dict('morse_code.dict')
    radio_controller = RadioControllerFactory.create_radio_controller()

    @bot.command(name='tx')
    async def transmit(ctx, frequency: float, *, message):
        if "tx" in [role.name for role in ctx.author.roles]:
            response = transmit_message(ctx, frequency, message, db_manager, morse_code_dict, radio_controller)
            await ctx.send(response)
        else:
            await ctx.send("You don't have permission to use this command.")

    bot.run(bot.token)

if __name__ == "__main__":
    main()
