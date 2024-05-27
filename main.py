import random

import streamlit as st

st.title("Cat, Mouse, Cheese")

human_choice = st.radio(
    "Enter your choice (cat, mouse, cheese):", ["cat", "mouse", "cheese"]
)
if st.button("Go!"):
    computer_choice = random.choice(["cat", "mouse", "cheese"])
    if human_choice == "cat":
        if computer_choice == "mouse":
            st.write("Your cat ate the mouse. You win!")
        elif computer_choice == "cheese":
            st.write("The cheese stunk up your cat. You lose!")
        elif computer_choice == "cat":
            st.write("Your cat made a new friend. Tie game!")
    elif human_choice == "mouse":
        if computer_choice == "mouse":
            st.write("The mice are playing. Tie game!")
        elif computer_choice == "cheese":
            st.write("Your mouse ate the cheese. You win!")
        elif computer_choice == "cat":
            st.write("The cat ate your mouse. You lose!")
    elif human_choice == "cheese":
        if computer_choice == "mouse":
            st.write("The mouse ate your cheese. You lose!")
        elif computer_choice == "cheese":
            st.write("Your cheese combined with the other cheese. Tie game!")
        elif computer_choice == "cat":
            st.write("Your cheese stunk up the cat. You win!")
