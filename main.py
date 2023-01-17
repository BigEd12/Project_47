import requests
from bs4 import BeautifulSoup
import smtplib

MY_EMAIL = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"

URL = "https://www.amazon.co.uk/Instant-Pot-Multicooker-Sousvides-dehydrates/dp/B08XC4JH7Y/ref=sr_1_4?crid=5137V2CZFBHK&keywords=instant%2Bpot&qid=1668360034&sprefix=instant%2Bpot%2Caps%2C181&sr=8-4&th=1"
MAX_PRICE = 200

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=header)
webpage = response.text

soup = BeautifulSoup(response.content, "html.parser")

price_tag = soup.find(class_="a-offscreen")
text_price = price_tag.getText()
text_price_split_list = text_price.split("£")
price = float(text_price_split_list[1])

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Instant Pot Price Alert\n\nHey brother,\nYou wanted to buy this "
                f"when you were learning to code. The price has just dropped to {price} and you were willing to "
                f"pay up to {MAX_PRICE} for it.\nHere's the link so you can buy it:\n{URL}\nHappy shopping."
        )

if price < MAX_PRICE:
    send_email()


