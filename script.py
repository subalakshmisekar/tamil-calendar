import smtplib
from email.message import EmailMessage
from datetime import datetime

# Sample Amavasai dates (YYYY-MM-DD)
AMAVASAI_DATES = [
    "2026-04-13",
    "2026-04-17",
    "2026-05-16",
    "2026-06-14",
    "2026-07-14"
]

def send_email():
   try:
    msg = EmailMessage()
    msg.set_content("🔔 Today is Amavasai! நினைவில் வை!")
    msg["Subject"] = "Amavasai Reminder"
    msg["From"] = "ssubasekar@gmail.com"
    msg["To"] = "subaniran217@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("ssubasekar@gmail.com", "yyzhuioyyvspuilp")
        smtp.send_message(msg)

        print("✅ Email sent successfully")

   except Exception as e:
        print("❌ Error sending email:", e)

today = datetime.now().strftime("%Y-%m-%d")

if today in AMAVASAI_DATES:
    send_email()
    print("Email sent ✅")
else:
    print("No Amavasai today")