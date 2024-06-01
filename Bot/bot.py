import disnake
from disnake.ext import commands
from time import sleep
import os
import json
from utils.utils import load_config


config = load_config()  # Loading the config file
prefix = config.get("prefix")  # Getting the prefix from the config file
token = config.get("token")  # Getting the token from the config file
# Getting the category name from the config file
category_name = config.get("ticket_category_name")
# Getting the channel name from the config file
channel_name = config.get("ticket_channel_name")

bot = commands.Bot(command_prefix=prefix, intents=disnake.Intents.all())


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_button_click(interaction: disnake.MessageInteraction):
    # If the button's custom id is 'ticket' -> creating a ticket
    if interaction.component.custom_id == 'ticket':
        guild = interaction.guild
        moderator = disnake.utils.get(guild.roles, id=config.get(
            "moderator_role_id"))  # Moderator role

        # Create a category for tickets if it doesn't exist
        cat = disnake.utils.get(guild.categories, name=category_name)
        if not cat:
            cat = await guild.create_category(name=category_name)

        overwrites = {  # Overwrites for the channel
            guild.default_role: disnake.PermissionOverwrite(read_messages=False),
            interaction.user: disnake.PermissionOverwrite(read_messages=True),
            moderator: disnake.PermissionOverwrite(read_messages=True)
        }
        channel_s = disnake.utils.get(  # Getting the channel
            interaction.guild.channels, name=f"{channel_name}-{interaction.user.id}")
        if channel_s is None:

            # Create a text channel for the ticket
            channel = await guild.create_text_channel(name=f"{channel_name}-{interaction.user.id}", category=cat,
                                                      overwrites=overwrites)
            # Send a message to the channel
            embed = disnake.Embed(title="Title",  # Title of the embed
                                  description="Description",  # Description of the embed
                                  color=0x800080  # Color of the embed
                                  )
            button = disnake.ui.Button(label="Delete",  # Text on the button
                                       style=disnake.ButtonStyle.gray,  # Color of the button
                                       custom_id='delete'  # ID of the button
                                       )
            view = disnake.ui.View(timeout=None)
            view.add_item(button)

            await channel.send(embed=embed, view=view)

            # Let the user know their ticket was created
            await interaction.send("The channel has been created!!", ephemeral=True)
        else:
            await interaction.send(f"The channel has already been created!!", ephemeral=True)

    # If the button's custom id is 'delete' -> deleting a ticket
    if interaction.component.custom_id == 'delete':
        channel = interaction.channel  # Getting the channel
        await channel.send("The ticket will be deleted in a couple of seconds...")
        sleep(2)
        await channel.delete()  # Deleting the channel


def load_cogs(bot):  # Loading all cogs from 'cogs/'
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    load_cogs(bot)
    bot.run(token)
