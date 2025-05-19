# SwiftATM – Simulated ATM Machine in Streamlit

**SwiftATM** is a simple, secure, and simulated ATM web application built using **Python**, **OOP principles**, and **Streamlit**. It supports user authentication, simulated database storage using JSON, and core banking features like deposit, withdraw, transfer, and utility bill payment.


## 🚀 Features

- User Registration and Login
- Deposit, Withdraw, and Balance Check
- Transfer to Other Users
- Pay Utility Bills
- View Transaction History
- Persistent Data Storage using JSON
- Streamlit UI for a smooth user experience
- Clean Object-Oriented Code Design



## 📂 Project Structure

swiftatm/ ├── app.py          # Main Streamlit app ├── models.py       # User and BankAccount classes (OOP) ├── storage.py      # Load/Save user data in JSON ├── database.json   # Simulated user database (initially empty) ├── README.md       # Project guide



## 🔧 Setup Instructions

### 1. Clone or Download

Download or clone this repo into your machine:

```bash
git clone https://github.com/your-username/swiftatm.git
cd swiftatm

2. Install Requirements

Install the only dependency:

pip install streamlit

3. Create database.json

Make a file named database.json in the root folder and add:

{}

This acts as your simulated database.




▶️ Run the Application

Run the app with:

streamlit run app.py


🧠 Built With OOP Principles

The app uses custom classes:

User – handles user data and login

BankAccount – handles balance and transactions

All user data is stored and loaded from database.json via helper functions





💼 Business Vision

SwiftATM can be transformed into a real-world fintech tool for:

Microfinance

Rural banking simulations

Student practice platforms

Offline ATMs in underbanked areas



---

💡 Future Improvements

Real-time email/SMS alerts

Integration with Razorpay/Stripe for real payments

User profile images and KYC

Role-based access for admins



---

👤 Author

Faiza Anum

Built for OOP Final Project — GIAIC Python Track


---

📜 License

This project is for educational use and personal simulations.

---


