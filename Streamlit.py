import streamlit as st
import string
import random 
a = string.digits
b = random.sample(a,5)
print(*b,sep="")
st.write("Order-Id",*b,sep="")
