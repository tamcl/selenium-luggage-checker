import os
from selenium_check import selenium_checker
from email_sender import emailSender
import time
import datetime

code_text = os.environ.get('CODE')
name_text = os.environ.get('USERNAME')

email = os.environ.get('EMAIL')
password = os.environ.get('PASSWORD')

receiver = os.environ.get('RECEIVER').split(' ')
print(receiver)


status = False

while not status:
    print(datetime.datetime.now())
    checker = selenium_checker(code_text, name_text, True)
    status = checker.run()

    if status:
        print('status changed')
        print(checker.status)
        print('alert')
        email_driver = emailSender(email, password)
        for rec in receiver:
            email_driver.send_email(rec, checker.status)
        break
    else:
        print(checker.status)
        print('sleep 300s')
        time.sleep(300)

