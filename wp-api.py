import os
import requests
from dotenv import load_dotenv 
import re

load_dotenv()
path = '.\\results'
os.chdir(path)
ROOT = str(os.getenv('ROOT'))
user = str(os.getenv('user'))
password = str(os.getenv('password'))
START = 'TITLE'
END = '!TITLE'

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        title = text[text.find(START)+len(START):text.rfind(END)]
        text = text.split(END)[-1]
        return title, text

def send_texts():
    title = ''
    text = ''
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{file}"
            title, text = read_text_file(file_path)
    
        data = {
            'title' : f'{title}',
            'content' : f'{text}',
            'status' : 'publish'
        }
        r = requests.post(
            url= ROOT + '/wp-json/wp/v2/posts',
            data=data,
            headers=headers,
            auth=(user, password),
            verify=False
        )
        print(r)

if __name__ == '__main__':
    send_texts()