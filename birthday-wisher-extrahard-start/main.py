##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import random as r
import pandas as pd

my_email = ""
my_pw = ""
current = dt.datetime.now()
df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    if current.month == row['month'] and current.day == row['day']:
        birthday_name = row['name']
        birthday_email = row['email']

with open(f"letter_templates/letter_{r.randint(1,3)}.txt") as t:
    template = t.read().replace("[NAME]", birthday_name)

with smtplib.SMTP("smtp.live.com") as connection:
    # connection security layer
    connection.starttls()
    connection.login(user=my_email, password=my_pw)

    if current.weekday() == 1:
        connection.sendmail(
            from_addr=my_email,
            to_addrs={birthday_email},
            msg=f"Subject:Happy Birthday to {birthday_name}!\n\n"
                f"{template}\n\n"
        )


