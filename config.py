from pyrogram import filters
import os

class Config:
    API_ID = "24569721"
    API_HASH = "b0081b01a3f015d9c76f5ed9e7b20271"
    #TOKEN = "6521122303:AAGCO3XMjcA0SN5NAi1M0NpmbmMxEtwwYbg"
    TOKEN = os.environ.get("TOKEN", None)
    MONGO_URL = "mongodb+srv://pusers:adcreation@adcreation.k8oapou.mongodb.net/?appName=ADCREATION"
    START_PIC = "https://anya-file-host.vercel.app/xtghy4ll6c"
    SUDOERS = filters.user(["8258238513"])
