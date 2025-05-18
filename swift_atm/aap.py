import streamlit as st
from models import User
from storage import load_users, save_users

st.set_page_config("SwiftATM 💳", layout="centered")
st.title("🏧 SwiftATM – ATM Simulator")

users = load_users()
if "user" not in st.session_state:
    st.session_state.user = None

def register():
    st.subheader("Register")
    uname = st.text_input("Username", key="reg_user")
    pwd = st.text_input("Password", type="password", key="reg_pass")
    if st.button("Create Account"):
        if uname in users:
            st.error("Username exists.")
        else:
            users[uname] = User(uname, pwd)
            save_users(users)
            st.success("Registered successfully!")

def login():
    st.subheader("Login")
    uname = st.text_input("Username", key="log_user")
    pwd = st.text_input("Password", type="password", key="log_pass")
    if st.button("Login"):
        user = users.get(uname)
        if user and user.password == pwd:
            st.session_state.user = uname
            st.success("Logged in!")
        else:
            st.error("Invalid credentials")

def dashboard():
    user = users[st.session_state.user]
    st.subheader(f"Welcome, {user.username}")
    st.metric("Balance", f"${user.account.balance}")
    
    # Deposit
    dep = st.number_input("Deposit $", min_value=0, key="dep")
    if st.button("Deposit"):
        user.account.deposit(dep)
        save_users(users)
        st.success(f"Deposited ${dep}")
    
    # Withdraw
    with_ = st.number_input("Withdraw $", min_value=0, key="with")
    if st.button("Withdraw"):
        if user.account.withdraw(with_):
            save_users(users)
            st.success(f"Withdrew ${with_}")
        else:
            st.warning("Not enough balance")

    # Transfer
    recipient = st.text_input("Transfer to (username)")
    amt = st.number_input("Amount to Transfer $", min_value=0, key="trans")
    if st.button("Transfer"):
        if recipient not in users:
            st.warning("User not found")
        elif users[recipient].username == user.username:
            st.warning("Can't transfer to self")
        elif user.account.transfer(amt, users[recipient]):
            save_users(users)
            st.success(f"Transferred ${amt} to {recipient}")
        else:
            st.warning("Insufficient balance")

    # Bill Payment
    if st.button("Pay Utility Bill – $500"):
        if user.account.withdraw(500):
            user.account.history.append((st.session_state.user, "Paid $500 utility bill"))
            save_users(users)
            st.success("Utility Bill Paid")
        else:
            st.warning("Insufficient balance")

    # History
    st.write("## Transaction History")
    for date, note in reversed(user.account.history[-5:]):
        st.write(f"{date} - {note}")

    if st.button("Logout"):
        st.session_state.user = None
        st.experimental_rerun()

# Routing
page = st.sidebar.selectbox("Menu", ["Login", "Register", "Dashboard" if st.session_state.user else "Login"])

if page == "Login":
    login()
elif page == "Register":
    register()
else:
    dashboard()
