import re
import email.utils

patttern = re.compile("[a-zA-Z]([a-z0-9-._]*)@([a-z]+)\.([a-z]{0,3})$", re.IGNORECASE)

for _ in range(int(input())):
    name, email_addr = email.utils.parseaddr(input())
    match = re.match(patttern, email_addr)

    if match:
        print(email.utils.formataddr((name, email_addr)))
