import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('โค้ชไอซ์'):
        await message.channel.send('นี่คือtiktokของเขา https://www.tiktok.com/@.coachice? ')

    if message.content.startswith('ครูหนึ่งสอนดี'):
        await message.channel.send('ช่องที่สอนเกี่ยวกับเทคโนโลยี https://www.tiktok.com/@kru1d?lang=th-TH ') 
    
    if message.content.startswith('Thairath'):
       await message.channel.send('https://www.youtube.com/user/thairathonline')
    

    if message.content.startswith('one31'):
        await message.channel.send('https://www.youtube.com/c/one31official')
    
    if message.content.startswith('Workpoint'):
       await message.channel.send('https://www.youtube.com/c/WorkpointOfficial') 

    if message.content.startswith('ch7hd'):
        await message.channel.send('https://www.youtube.com/c/ch7hd')

     



client.run('TOKEN')
