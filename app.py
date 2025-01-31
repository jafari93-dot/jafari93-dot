from flask import Flask, request, Response
import requests
import time

app = Flask(__name__)

# تنظیم سشن
session = requests.Session()

# تنظیم هدرهای مرورگر برای جلوگیری از بلاک شدن
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Referer": "https://www.walmart.ca"
})

@app.route('/scrape', methods=['GET'])
def scrape():
    url = request.args.get("url")
    if not url:
        return Response("URL is required", status=400, mimetype='text/plain')

    try:
        response = session.get(url, allow_redirects=True)
        response.raise_for_status()
        time.sleep(2)  # تأخیر برای جلوگیری از بلاک شدن
        return Response(response.text, mimetype='text/plain')
    except requests.exceptions.RequestException as e:
        return Response(str(e), status=500, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)