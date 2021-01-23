# Brithday_Wisher_Project
100daysofcode-day50-51

EOD project for my udemy python course
- Send automated birthday emails using python

Automate wishing Birthday to friends and family. This simple app will send emails to your friends and family based on their birthdays.
It includes the following:
- CSV file to add the birthday and email address
- Simple letters

Python Modules in use:
- Python pandas module to ready the data from the CSV file
- Python DateTime module for data and time
- Python random module to randomize the letters
- Python smtplib to send emails

Use function:
- All you need to do is add the DOB and email address in the CSV file.
  Ex. Test,test@yahoo.com,1961,1,22
 - This app will replace the names from template letters and send random birthday wishes using the email address and month, day
 
 
 Caution:
  - To use python smtplib you will need to allow python code to log into your account
  - For gmail, you will need to allow less secure apps to log into Gmail, this is not recommended
  - This is done only for lab purposes and used test Gmail accounts
 
 smtplib how to:
 - What is smtplib?
    The smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. (Google)
 - Important methods:
    - smtplib.SMTP("smtp.mail.yahoo.com", 587)
        - this methods allows us to connect to the email providers mail server
        - this example for yahoo, but its different for different providers
        - google it to find the correct smtp for that provider
        - "with" keyword will close the correct automatically
        - Double \n allows yo write the body of the email
        - Error: Python SMTP Error 10060. Solution added the port number: 587
        - gmail SMTP: smtp.gmail.com, port: 587
        - yahoo SMTP: smtp.mail.yahoo.com
        
        Ex.:
            with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            # encrypting emails with TLS
              connection.starttls()
             # login
              connection.login(user=my_email, password=password)
             # sendemail
              connection.sendmail(from_addr=my_email,
                        to_addrs="[type email address]",
                        msg="Subject:Hello\n\nThis is the body of my email."
                        )
