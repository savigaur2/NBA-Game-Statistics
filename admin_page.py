import streamlit as st
def app ():
    st.title('Admin Login')

    st.text_input(label = 'Username', value = '')
    st.text_input(label = 'Password', value = '')
    st.button(label= 'Login')
