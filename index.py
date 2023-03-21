from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = 'https://api.genelpara.com/embed/para-birimleri.json'
    data = get_data(url)
    return render_template("index.html", data=data)

def get_data(url):
    send = requests.post(url)
    data = {
        "BTC": {
            "alis": send.json()['BTC']['alis'],
            "satis": send.json()['BTC']['satis']
        },
        "ETH": {
            "alis": send.json()['ETH']['alis'],
            "satis": send.json()['ETH']['satis']
        },
        "USD": {
            "alis": send.json()['USD']['alis'],
            "satis": send.json()['USD']['satis']
        },
        "EUR": {
            "alis": send.json()['EUR']['alis'],
            "satis": send.json()['EUR']['satis']
        },
        "GBP": {
            "alis": send.json()['GBP']['alis'],
            "satis": send.json()['GBP']['satis']
        },
        "XU100": {
            "alis": send.json()['XU100']['alis'],
            "satis": send.json()['XU100']['satis']
        }
    }
    return data

if __name__ == '__main__':
    app.run(debug=True, port=5000)
