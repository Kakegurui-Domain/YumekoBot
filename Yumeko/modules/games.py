from telethon.tl.types import InputMediaDice

from lunaBot.events import register


@register(pattern="^/dice(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice(""))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@register(pattern="^/dart(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🎯"))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@register(pattern="^/ball(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🏀"))
    input_int = int(input_str)
    if input_int > 5:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass





__mod_name__ = "ɢᴀᴍᴇ"
