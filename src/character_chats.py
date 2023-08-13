import streamlit as st
from characters import Character_Chain


st.title('Character Chats')


Levi_character_description = "Levi Ackerman from Attack on Titan",
Gojou_character_description = "Gojou Satoru from Jujutsu kaisen"

LeviChain = Character_Chain(character_description=Levi_character_description,
                             participant_description=Gojou_character_description)
GojouChain = Character_Chain(character_description=Gojou_character_description,
                             participant_description=Levi_character_description)

levi_boxes = []
gojou_boxes = []

last_response = "Hey."
for i in range(0,5):
    last_response = LeviChain.run(input=last_response)
    levi_boxes.append(st.chat_message(name="Levi Ackerman"))
    levi_boxes[i].write(last_response)
    last_response = GojouChain.run(input=last_response)
    gojou_boxes.append(st.chat_message(name="Gojou Satoru"))
    gojou_boxes[i].write(last_response)