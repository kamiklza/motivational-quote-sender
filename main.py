import smtplib

my_email = "xxxxxxx"
my_password = "xxxxxxx"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="kamiklza@hotmail.com", msg="Testing 2")


import random
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 4:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        random_quote = random.choice(quotes)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="kamiklza@hotmail.com", msg=f"Subject: Today motivational quote\n\n{random_quote}")

else:
    print("Goodbye")
