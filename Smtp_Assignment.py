import smtplib
import datetime as dt
import random as r
import csv

# Email credentials
MY_EMAIL = "abdulhadistmstudent@gmail.com"
PASSWORD = 'qipn kezf wxfn jphg'

# Find Today Weekday
def get_current_weekday():
    return dt.datetime.now().weekday()

# Read Quotations from Text File
def read_quotes(file_path):
    with open(file_path, 'r') as file:
        quotes = file.readlines()
    return quotes

# Get Random Quote
def get_random_quote(quotes):
    return r.choice(quotes).strip()

# Read Email Addresses from csv file
def read_email_addresses(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        emails = [row[0] for row in reader]
    return emails

def send_emails(email_addresses, quote):
    """Sends the given quote to all email addresses in the list."""
    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        for email in email_addresses:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject: Monday Motivation\n\n{quote}"
            )
    print("Emails sent successfully.")


if get_current_weekday() == 0:  # Check if today is Monday
    quotes = read_quotes("quotes_file.txt")
    
    if quotes:
        quote = get_random_quote(quotes)
        email_addresses = read_email_addresses("email.csv")
    
        if email_addresses:
            send_emails(email_addresses, quote)
        else:
            print("No email addresses found.")
    
    else:
        print("No quotes found.")
    
else:
    print("Today is not Monday. No emails sent.")