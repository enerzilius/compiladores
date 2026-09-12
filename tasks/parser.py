import re


def extract_emails():
    with open("./data/e-mails.txt", "r") as file:
        data = file.read()

    # extrair emails
    data = re.findall(r"<(.*)>", data)

    print(data)


def extract_links():
    with open("./data/utfpr-cm.html", "r") as file:
        data = file.read()

    data = re.findall(r'"(https?://[^"]*)"', data)
    print(data)


extract_links()
