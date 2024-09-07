from conf import Conf

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import itertools
import numpy as np

def get_santas_for(people, exclusions):
    while True:
        permutation = list(np.random.permutation(people))
        hamilton_permutation = [permutation[-1]] + permutation[:-1]
        if valid(zip(hamilton_permutation, permutation), exclusions):
            return {key: value for (key, value) in zip(permutation, hamilton_permutation)}


def valid(people, exclusions):
    for person, santa in people:
        if person == santa:
            return False
        for excl in exclusions:
            if person in excl and santa in excl:
                return False
    return True

def make_message(giver, taker):
    return "%s, трябва да купиш подарък на %s\n\nЛимит за финанси: 40лв." % (
        giver['name'], taker['name']
    )

def make_email_message(giver, taker):
    msg = MIMEMultipart("alternative")
    msg["From"] = '%s <%s>' % (Conf['mail']['name'], Conf['mail']['email'])
    msg["To"] = giver['email']
    msg["Subject"] = 'Таен дядо'
    body = MIMEText(make_message(giver, taker), "plain", "utf-8")
    msg.attach(body)

    return msg.as_string().encode('ascii')

def send_mail(giver, taker):
    print('Sending mail to %s' % giver['name'])
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
    return get_santas_for(list(Conf['people'].keys()), Conf['exclusions'])

def main():
    for (person_id, santa_id) in santas().items():
        send_mail(Conf['people'][person_id], Conf['people'][santa_id])

if __name__ == '__main__':
    main()
