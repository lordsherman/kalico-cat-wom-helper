import requests
import json

def get_members():
    id_response = requests.get("https://api.wiseoldman.net/groups/909/members")
    return id_response

def main():
    members = get_members()
    print(members.json())

if __name__ == '__main__':
    main()