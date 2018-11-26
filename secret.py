import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


def do_the_draw(list):
    drawn = {"Jola": "Waldek",
             "Babcia": "Jola"}

    for person in list:
        if person not in drawn.keys():
            draw = person
            while (draw == person or draw in drawn.values()):
                draw = random.choice(list)
            drawn[person] = draw

    return drawn


def send_email(person, email, draw):
    fromaddr = "santasekretny@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "SECRET SANTA - LOSOWANIE 2018 - Informacja dla %s" % (person)

    body = "HO HO HO!\n\n" \
           "Gratuluję %s! W tegorocznej edycji SECRET SANTA wylosowałeś: %s.\n\n" \
           "Wesołych Świąt!\n" \
           "Sekretny Santa" % (person, draw)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "!0.nrzbrlzzpk.1")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def main():
    ppl = ['Jola', 'Waldek', 'Babcia', 'Kasia J', 'Kinga', 'Andrzej', 'Magda', 'Kasia P', 'Dorota', 'Arek', 'Łukasz']

    ppl_emails = {'Jola': 'jablonskey@mail.com',
                  'Waldek': 'jablonskey@mail.com',
                  'Babcia': 'jablonskey@mail.com',
                  'Kasia J': 'jablonskey@mail.com',
                  'Kinga': 'jablonskey@mail.com',
                  'Andrzej': 'jablonskey@mail.com',
                  'Magda': 'no.rehearsall@gmail.com',
                  'Kasia P': 'jablonskey@mail.com',
                  'Dorota': 'jablonskey@mail.com',
                  'Arek': 'jablonskey@mail.com',
                  'Łukasz': 'jablonskey@mail.com'}

    draws = do_the_draw(ppl)

    for person in draws.keys():
        # print("%s draws %s and message sent to %s" % (person, draws[person], ppl_emails.get(person)))
        print("Email sent to %s to %s" % (person, ppl_emails.get(person)))
        send_email(person, ppl_emails.get(person), draws[person])
        time.sleep(2)


main()
