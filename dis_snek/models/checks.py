from dis_snek.models.discord_objects.context import Context


def has_role(role_id):
    """
    Checks if the author has a role with a specific id.
    :param coro: the function to check
    """

    async def check(ctx: Context) -> bool:
        return any(role.id == role_id for role in await ctx.author.roles)

    return check


def has_id(user_id):
    """
    Checks if the author has the desired ID.
    :param coro: the function to check
    """

    async def check(ctx: Context) -> bool:
        return ctx.author.id == user_id

    return check


def is_owner():
    """
    Is the author the owner of the bot.
    :param coro: the function to check
    """

    async def check(ctx: Context) -> bool:
        return ctx.author.id == await ctx.bot.owner

    return check
