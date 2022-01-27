# phone_and_email.py
# simple program to find e-mails and phone numbers on large amounts of text

import re, pyperclip

WIDTH = 10  # width for pretty printing data

text = pyperclip.paste() # text from your clipboard

cellphone_regex = re.compile(r'''(
    (\d{2}|\(\d{2}\))?  # area code
    (\s|-)?             # separator
    (9)?                # additional digit
    (\d{4})             # first four digits
    (\s|-)?             # separator
    (\d{4})             # last four digits 
)''', re.VERBOSE)

email_regex = re.compile(r'''(
([a-zA-Z0-9.-_%+]+)     # username
@                       # @
([a-zA-Z0-9.-]+)        # domain name
(.[a-z]{2})             # extension
)''', re.VERBOSE) 

phone_numbers = [group[0] for group in cellphone_regex.findall(text)]
emails = [group[0] for group in email_regex.findall(text)]


def data_print(data, type: str):
    '''Prints all found data that matches the selected type (e-mail/phone number)'''
    for x in data:
        print(type + ' '*WIDTH + x.ljust(WIDTH, ' '))
    print()

data_print(phone_numbers, "NUMBER: ")
data_print(emails, "E-MAIL: ")