# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]

# set comprehension to extract a clean, unique set of lowercase email addresses

processed_emails = set([email.lower() for email in raw_emails if ("@" in email)])

# print the clean set of email addressed

print(processed_emails)