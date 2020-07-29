@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=int(amount) + 1):
              messages.append(message)
              
    await channel.delete_messages(messages)
