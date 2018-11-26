import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


def draw(draw_participants_list):
    drawn_dict = {"Babcia": "Waldek"}

    for participant in draw_participants_list:
        if participant not in drawn_dict.keys():
            drawn_person = participant
            while (drawn_person == participant or drawn_person in drawn_dict.values()):
                drawn_person = random.choice(draw_participants_list)
            drawn_dict[participant] = drawn_person

    return drawn_dict


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
    people = ['Waldek', 'Babcia', 'Kasia J', 'Kinga', 'Andrzej', 'Magda', 'Kasia P', 'Dorota', 'Arek', 'Łukasz']

    people_with_emails = {'Waldek': 'jablonskey@mail.com',
                  'Babcia': 'jablonskey@mail.com',
                  'Kasia J': 'jablonskey@mail.com',
                  'Kinga': 'jablonskey@mail.com',
                  'Andrzej': 'jablonskey@mail.com',
                  'Magda': 'no.rehearsall@gmail.com',
                  'Kasia P': 'jablonskey@mail.com',
                  'Dorota': 'jablonskey@mail.com',
                  'Arek': 'jablonskey@mail.com',
                  'Łukasz': 'jablonskey@mail.com'}

    draws = draw(people)

    for person in draws.keys():
        print("%s draws %s and message sent to %s" % (person, draws[person], people_with_emails.get(person)))
        # print("Email sent to %s to %s" % (person, people_with_emails.get(person)))
        # send_email(person, people_with_emails.get(person), draws[person])
        time.sleep(1)


main()
