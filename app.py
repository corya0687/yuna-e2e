import sqlite3, subprocess, yaml, hashlib, requests
from flask import request

def get_user(db):
    name = request.args.get("name")
    db.execute(f"SELECT * FROM users WHERE name = '{name}'")

def run(cmd):
    subprocess.call(request.args["cmd"], shell=True)

def load(data):
    return yaml.load(data)

def fetch(url):
    return requests.get(url, verify=False)

def hash_pw(pw):
    return hashlib.md5(pw.encode()).hexdigest()
