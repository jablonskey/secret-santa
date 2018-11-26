import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random


def draw(draw_participants_list):
    drawn_dict = {"Babcia Danusia": "Waldek"}

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

    body = "HO HO HO!\n\n\n\n\n\n\n\n\n\n\n\n\n\n" \
           "Gratuluję %s! W tegorocznej edycji SECRET SANTA wylosowana dla Ciebie osoba to: %s.\n\n" \
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
    people = ['Waldek', 'Babcia Danusia', 'Kasia Jabłońska', 'Kinga', 'Andrzej', 'Magda', 'Kasia Peek', 'Dorota',
              'Arek', 'Łukasz']

    people_with_emails = {'Waldek': 'wjkierka@gmail.com',
                          'Babcia Danusia': 'jablonskey@gmail.com',
                          'Kasia Jabłońska': 'kapple.jbl@gmail.com',
                          'Kinga': 'kinga.aureliajbl@gmail.com',
                          'Andrzej': 'andrze1jablonski@gmail.com',
                          'Magda': 'no.rehearsall@gmail.com',
                          'Kasia Peek': 'kasiapeek@gmail.com',
                          'Dorota': 'dorotamjablonska@gmail.com',
                          'Arek': 'arusjablonski@gmail.com',
                          'Łukasz': 'jablonskey@gmail.com'}

    # people_with_emails2 = {'Waldek': 'jablonskey@mail.com',
    #                       'Babcia Danusia': 'jablonskey@mail.com',
    #                       'Kasia Jabłońska': 'jablonskey@mail.com',
    #                       'Kinga': 'jablonskey@mail.com',
    #                       'Andrzej': 'jablonskey@mail.com',
    #                       'Magda': 'jablonskey@mail.com',
    #                       'Kasia Peek': 'jablonskey@mail.com',
    #                       'Dorota': 'jablonskey@mail.com',
    #                       'Arek': 'jablonskey@mail.com',
    #                       'Łukasz': 'jablonskey@gmail.com'}

    draws = draw(people)

    for person in draws.keys():
        # print("%s draws %s and message sent to %s" % (person, draws[person], people_with_emails.get(person)))
        print("Email sent to %s to %s" % (person, people_with_emails.get(person)))
        send_email(person, people_with_emails.get(person), draws[person])
        time.sleep(1)


main()
