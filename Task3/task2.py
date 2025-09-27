# 2) Regex Log Cleaner
#    - Create a file called "access.log" with 10 fake log lines
#      (mix valid emails and invalid strings).
#    - Use regex to extract all valid emails.
#    - Save them into "valid_emails.txt".
#    - Print how many unique emails were found.

import re
from task7 import log_time

@log_time
def validateEmails():
    fileName = "access.log"
    logLines = ["mhmdabohend@gmail.com","nexample@example.com",
                "fakeemail@email","anotherfakeone.com",
                "mhmdabohend@gmail.com","nexample@example.com",
                "fakeemail@email","anotherfakeone.com",
                "mhmdabohend@gmail.com","nexample@example.com"]
    with open(fileName, "w") as file:
        file.write("\n".join(logLines))
    
    emailPattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    with open(fileName, "r") as file:
        content = file.read()
        emails = re.findall(emailPattern, content, re.MULTILINE)
    
    uniqueEmails = set(emails)
    with open("valid_emails.txt", "w") as file:
        file.write("\n".join(uniqueEmails))

    print(f"{len(uniqueEmails)} unique emails found.")

    