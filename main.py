# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIPIENT_EMAIL = os.environ.get("RECEIPIENT_EMAIL")
DAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}

today = datetime.now()
weekday = DAYS[today.weekday()]

with open('quotes.txt', 'r') as f:
    quotes = f.readlines()
body = random.choice(quotes)

with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
    connection.starttls()
    connection.login(SENDER_EMAIL, SENDER_PASSWORD)
    connection.sendmail(
        from_addr=SENDER_EMAIL,
        to_addrs=RECEIPIENT_EMAIL,
        msg=f"Subject:Here's some {weekday} motivation!\n\n{body}"
    )
