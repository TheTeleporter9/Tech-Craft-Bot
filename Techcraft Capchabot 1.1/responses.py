from random import choice, randint

from discord import BotIntegration, Client, Guild, Member
import main as m

isVerified: bool = False
num: int = 0
numCheck: int = 0


giveRole: bool = False

def get_response(user_input: str) -> str:
    global isVerified, num, numCheck

    lowered: str = user_input.lower()

    if lowered == '':
        return "Well, you're awfully silent...."
    
    elif '!verify' in lowered:
        isVerified = True
        num = generate_randNumber()
        print(num)
        return str(num)  # Convert the number to a string before returning
    
    elif isVerified:
        numCheck = int(lowered)
        if num == numCheck:
            isVerified = False
            return "Yes!"
    
    return choice(['I do not understand...',
                   'Can you please rephrase that',
                   'What are you talking about?'])

def generate_randNumber() -> int:
    rand = randint(1000, 9999)
    return rand









# from random import choice, randint

# isVerified: bool = False
# num: int = 0
# numCheck: int = 0

# def get_response(user_input: str) -> str:
#     global isVerified, num, numCheck

#     lowered: str = user_input.lower()

#     if lowered == '':
#         return "Well, you're awfully silent...."
    
#     elif '!verify' in lowered:
#         isVerified = True
#         num = generate_randNumber()
#         print(num)
#         return str(num)  # Convert the number to a string before returning
    
#     elif isVerified:
#         numCheck = int(lowered)
#         if num == numCheck:
#             isVerified = False
#             return "Yes!"
    
#     return choice(['I do not understand...',
#                    'Can you please rephrase that',
#                    'What are you talking about?'])

# def generate_randNumber() -> int:
#     rand = randint(1000, 9999)
#     return rand






