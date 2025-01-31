#!/bin/bash

# فعال کردن محیط مجازی (اگر داری)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# نصب وابستگی‌ها (در صورت نیاز)
pip install -r /home/site/wwwroot/requirements.txt

# اجرای سرور Flask با Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
