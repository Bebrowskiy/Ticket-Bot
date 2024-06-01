import disnake
from disnake.ext import commands
from disnake.ui import View, Button
from utils.utils import load_config


class EmbedCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = load_config()

    @commands.slash_command(name="embed", description="Sends an embed message with button")
    async def embed(ctx: disnake.ApplicationCommandInteraction):
        view = View(timeout=None)
        button = Button(
            label="New Ticket",  # Label for the button
            style=disnake.ButtonStyle.grey,  # Color of the button
            custom_id="ticket"  # ID of the button that's passed to the function when pressed
        )
        view.add_item(button)
        embed = disnake.Embed(
            title="Title",  # Title of the embed
            description="Description",  # Description of the embed
            color=disnake.Color.green(),  # Color of the embed
        )
        await ctx.send(embed=embed, view=view)


def setup(bot):
    bot.add_cog(EmbedCog(bot))
