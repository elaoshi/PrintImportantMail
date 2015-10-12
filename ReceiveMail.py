## Here we receive the mails from the server and look for the right identifiers

import poplib
import time
from PrintMail import printmail
from email import parser

# Setup connection details and identifier (identifier in lowercase!)
identifier = ''
emailsprinted = []
subjectArray = []
sleepTimeSec = 60

pop_conn_server = raw_input("POP3 SERVER: ")
pop_conn_username = raw_input("MAIL ADDRESS: ")
pop_conn_password = raw_input("PASSWORD: ")
identifier = raw_input("IDENTIFIER: ").lower()
sleepTimeSec = sleepTimeSec * input("UPDATE INTERVAL: ")

while True:
    pop_conn = poplib.POP3_SSL(pop_conn_server)
    pop_conn.user(pop_conn_username)
    pop_conn.pass_(pop_conn_password)

    # Displaying current status
    print "Searching for new messages..."

    # Retreive messages from server
    messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]

    # Concat message pieces
    messages = ["\n".join(mssg[1]) for mssg in messages]

    # Parse message body and subject
    messages = [parser.Parser().parsestr(mssg) for mssg in messages]

    subjectArray = []
    for message in messages:
        subject = message['subject']
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
        if identifier in subject.lower():
            if subject.lower() not in emailsprinted:
                printmail(subject, body)
                emailsprinted.append(subject.lower())
        subjectArray.append(subject.lower())

    # Delete every message from emailsprinted thats not in the inbox anymore
    for printed in emailsprinted:
        if printed not in subjectArray:
            emailsprinted.remove(printed)

    # Disconnect from server
    pop_conn.quit()

    #Sleep for a certain amount of time
    time.sleep(sleepTimeSec)
    print "\n"
