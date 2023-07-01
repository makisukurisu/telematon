import os

app_api_id = input("Enter app_api_id (my.telegram.org): ")
app_api_hash = input("Enter app_api_hash (my.telegram.org): ")
session_string = input("Enter session string: ")

os.system(f"echo {app_api_id} | docker secret create app_api_id -")
os.system(f"echo {app_api_hash} | docker secret create app_api_hash -")
os.system(f"echo {session_string} | docker secret create session_string -")

print("Secrets created.")
