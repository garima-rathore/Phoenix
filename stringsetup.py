#!/usr/bin/env python3
# har jgh credit de dena kangers
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
   """ PLEASE GO-TO my.telegram.org
Login using your Telegram account
click on API Development Tools 
Create a new application , by entering the required details"""
)
APP_ID = int(input("ENTER APP ID HERE: "))
API_HASH = input("ENTER API HASH HERE: ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
   print(client.session.save())
   client.send_message("me",client.session.save())
