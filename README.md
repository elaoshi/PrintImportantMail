Print Important Mail
====================

General
---------

This project is made for automatically printing mails with certain identifiers
in their Title. This can be setup using python2 and the command line of
Linux or Windows.

Preparations
------------

**Windows:**

For running this on Windows you have to download Python2 from their official
website. For Windows you also have to install pywin32 (win32api is the same).
If you have installed everything correctly you should be able to start
the program by typing the following in the cmd:

    python ReceiveMail.py

*Note: You have to switch to the correct directory first and you will not be
able to close the cmd while running the application.*

**Linux:**

Everything you need for Linux is the current Python2 version.
If this is installed simply run the following command:

    sudo python2 ReceiveMail.py

If you want to run this script in the background you can install *"screen"* and
run it with the following code:

    sudo screen -dmS YourNameForThisProcess python2 ReceiveMail.py

This will keep the script running even after you close your terminal. But
note that this will not automatically start the application at system boot!


Command Line Setup
------------------

For setting everything up please follow the prompts given after starting
up the application.
Here are explanations to every prompt:

- POP3 SERVER: Enter the POP3 Server of your email provider here. This should
look similar to this: "pop.gmail.com"
- MAIL ADDRESS: This is your email address. It should look like "user@gmail.com".
- PASSWORD: This is the password for the email account provided as MAIL ADDRESS.
This is needed for retreiving messages from the server.
- IDENTIFIER: This is the identifier that is used for printing your mails. If
this is in the subject of any email (capitalization does not matter) the content
of that mail will be sent directly to your printer.
- UPDATE INTERVAL: The amount of minutes the application will wait until
searching for new mails. This cannot be smaller than 1.
