from src.characters import Character_Chain
from dotenv import load_dotenv

Levi_character_description = "Levi Ackerman from Attack on Titan",
Gojou_character_description = "Gojou Satoru from Jujutsu kaisen"

LeviChain = Character_Chain(character_description=Levi_character_description,
                             participant_description=Gojou_character_description)
GojouChain = Character_Chain(character_description=Gojou_character_description,
                             participant_description=Levi_character_description)

load_dotenv()

def test_character_chat_start():
    assert type(LeviChain.run(input="Hello. How are you?")) != None

def test_short_chat():
    last_response = "Hey."
    for i in range(0,5):
        last_response = LeviChain.run(input=last_response)
        print(last_response)
        last_response = GojouChain.run(input=last_response)
        print(last_response)
    assert last_response != "Hey."
