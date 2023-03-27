import requests
import time
import bs4

def send_message(message):
    data = {
        'content': message
    }
    response = requests.post(webhook_url, json=data)

webhook_url = 'xxx'




if __name__ == '__main__':
    while True:
        url = "https://pika-network.net/bans/"
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        bans = soup.find_all('div', class_="row")
        for ban in bans:
            info = ban.text
            username = info.split(' ')[0]
            reason = info.split(' ')[1]
            clean_reason = reason.replace('Reason:', '')
            clean_username = username.replace('Username:', '')
            clean_reason = clean_reason.replace('\n', '')
            clean_username = clean_username.replace('\n', '')
            print(f"{clean_username} {clean_reason}")
            send_message(f"{clean_username} {clean_reason}")
        time.sleep(60*5)

