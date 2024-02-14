import streamlit as st
import string
import random 
a = string.digits
b = random.sample(a,5)
printer = print(*b,sep='')
st.write(*b,sep="")
