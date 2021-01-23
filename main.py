import pandas
import smtplib
import datetime as dt
import random


my_email = "test@gmail.com"
# from security standpoint not a good idea to hardcode your password inside code
password = ""

# 1. Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Turning the data fine into a dict using dict compression
# using data.iterrows to iterate over the pandas dataframe
birthday_dict = {index: row for index, row in data.iterrows()}
# print(birthday_dict)

# getting date info using datetime module
today = dt.datetime.now()
today_month = today.month
today_day = today.day


# using for loop loop through all the rows in birthday.csv
for num in range(len(birthday_dict)):

    # getting hold of the birthday, month and name
    birthday_day = birthday_dict[num]["day"]
    birthday_month = birthday_dict[num]["month"]
    name = birthday_dict[num]["name"]
    email = birthday_dict[num]["email"]

    # to see if birthday and month matches today's date
    if birthday_day == today_day and birthday_month == today_month:

        # opening one of the random letters
        # using random.randint to pick a random letter
        with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as letter_content:
            # reading and saving the content of the random letters to content
            content = letter_content.read()
            # replacing the name with the birthday boy/girls name
            formated_letter = content.replace("[NAME]", name)


        # 4. Send the letter generated in step 3 to that person's email address.
        # using pythons smtplib to send emails
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday\n\n{formated_letter}"
                                )




