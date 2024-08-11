from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Member, Message
from responses import *
import discord
import responses as r


# Load the Discord Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
ROLE_ID: Final[int] = os.getenv('ROLE_VERIFIED_ID')

#Bot setup
intents: Intents = Intents.default()
intents.message_content =  True #NOQA
client: Client = discord.Client(intents=intents)

#Message Functunallity
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled correctly probably ')
        return
    
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def assign_verified_role(member: Member):
    # Replace 'YOUR_ROLE_ID' with the actual role ID
    role_id = ROLE_ID
    role = member.guild.get_role(role_id)
    member.add_roles(role)
    
#Handeling the startup for the bot

@client.event
async def on_ready() -> None:
    print(f'{client}')
    
    #Handel incoming messages

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
        
    username: str = str(message.author)
    user_message: str = message.content
    #channel: str = str(message.channel)

   # print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

     # Assuming 'message.author' is the member who sent the message
    # if message == "Yes!" and message.author.bot:
    if r.giveRole == True:
        print("Role beeing added")
        assign_verified_role(message.author)
        print("Role successfully added")
        r.giveRole = False
        return





#Main entry point

def main() -> None:
    client.run(token =TOKEN)


if __name__ == '__main__':
    main()
