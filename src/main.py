#!/usr/bin/python

from emailbot import Email

#used to test email bot

def main():

    source = raw_input("Enter gmail source address: ")
    passwd = raw_input("Enter gmail source password: ")
    dest = raw_input("Enter destination email: ")
    title = "test email"
    email = Email(source, passwd, dest, title)
    email.send_email()


if __name__ == '__main__':
    main()
