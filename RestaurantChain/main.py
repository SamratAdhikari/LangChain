import streamlit as st
from helper import generate_restaurant_name_and_items

st.title("Restaurant Chain")

nationality = st.sidebar.selectbox("Pick a nationality", ("Nepali", "Chiese", "Arabic", "Indian", "Italian", "Mexican"))

if nationality:
    response = generate_restaurant_name_and_items(nationality)
    
    st.header(response['restaurant_name'].strip().strip('"'))
    menu_items = response['menu_items'].strip().split(",")

    st.subheader("**Menu Items**")
    for item in menu_items:
        st.write("-", item.strip()) 