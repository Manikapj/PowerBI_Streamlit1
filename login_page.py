import streamlit as st
st.set_page_config(page_title="Login Page", page_icon="🔒")
st.title("Login Page")
with st.form("login_form"):
    st.subheader("Please enter your login details")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")
if login_button:
    if username == "admin" and password == "password123":  # Replace with your validation logic
        st.success("Login successful!")
        st.write("Welcome, ", username)
    else:
        st.error("Invalid username or password. Please try again.")