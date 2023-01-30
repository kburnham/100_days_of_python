import smtplib
import random
import datetime as dt

my_email = 'kburnham@gmail.com'
password = 'adthptcaxewbllna'



now = dt.datetime.now()
wd = now.weekday()

if wd == 4:
    infile = 'Birthday Wisher (Day 32) start/quotes.txt'
    with open(infile) as q:
        d = q.read()

    quotes = d.split('\n')

    msg = 'Subject: inspirational message\n\n' + random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = password)
        connection.sendmail(from_addr=my_email, to_addrs= 'mudshark94@yahoo.com', 
                            msg = msg)

    print('message sent!')
else:
    print('not a Friday, no action taken.')
        








