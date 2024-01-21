from random import randint

import streamlit as st


roll = randint(1, 6)

st.button("Roll!")

"---"

st.write(f"You got a: {roll}")