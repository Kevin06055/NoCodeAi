import streamlit as st
import string
import random 
a = random.sample(string.digits,5)
print(a)
st.write("My First APP- Generated NUmber",a)
