import json
from models import User

DB_PATH = "database.json"

def load_users():
    try:
        with open(DB_PATH, "r") as f:
            data = json.load(f)
        users = {}
        for uname, info in data.items():
            u = User(uname, info['password'], info['balance'])
            u.account.history = info.get('history', [])
            users[uname] = u
        return users
    except:
        return {}

def save_users(users):
    data = {}
    for uname, user in users.items():
        data[uname] = {
            "password": user.password,
            "balance": user.account.balance,
            "history": [[str(h[0]), h[1]] for h in user.account.history]
        }
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)
