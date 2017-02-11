#!/usr/bin/python

from emailbot import Email

def main():

    source = raw_input("Enter gmail adress: ")
    passwd = raw_input("Enter gmail password: ")
    dest = "gabriel.gibeault-girard@mail.mcgill.ca"
    title = "test email"
    email = Email(source, passwd, dest, title)


if __name__ == '__main__':
    main()
