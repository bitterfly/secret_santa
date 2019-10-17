from conf import Conf

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import itertools
import numpy as np

def get_santas_for(people, couples):
    while True:
        permutation = list(np.random.permutation(people))
        hamilton_permutation = [permutation[-1]] + permutation[:-1]
        if valid(zip(hamilton_permutation, permutation), couples):
            return {key: value for (key, value) in zip(permutation, hamilton_permutation)}


def valid(people, couples):
    for person, santa in people:
        if person == santa or (person, santa) in couples or (santa, person) in couples:
            return False
    return True

def make_message(giver, taker):
    return "\n%s,\nтрябва да купиш подарък на %s\nЛимит за финанси: 40лв." % (
        giver['name'], taker['name']
    )

def make_email_message(giver, taker):
    msg = MIMEMultipart("alternative")
    msg["From"] = Conf['mail']['email']
    msg["To"] = giver['email']
    msg["Subject"] = 'Таен дядо'
    body = MIMEText(make_message(giver, taker), "plain", "utf-8")
    msg.attach(body)

    return msg.as_string().encode('ascii')

def send_mail(giver, taker):
    print('will send mail for ', giver, ' --> ', taker)
    receiver = giver['email']
    msg = make_email_message(giver, taker)

    if Conf['mail']['use_ssl']:
        server = smtplib.SMTP_SSL(Conf['mail']['server'])
        server.ehlo()
    else:
        server = smtplib.SMTP(Conf['mail']['server'])
        server.ehlo()
        server.starttls()

    server.login(Conf['mail']['user'], Conf['mail']['pass'])

    server.sendmail(Conf['mail']['email'], giver['email'], msg)

def santas():
    return get_santas_for(list(Conf['people'].keys()), Conf['couples'])

def main():
    for (person_id, santa_id) in santas().items():
        send_mail(Conf['people'][person_id], Conf['people'][santa_id])

if __name__ == '__main__':
    main()
