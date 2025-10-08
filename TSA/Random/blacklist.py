BLACKLIST =[
    "1chuan.com",
    "7tags.com",
    "a2z4u.net",
    "bluemail.ch",
    "zetmail.com",
    "vovan.ru",
    "twcny.com",
    "suhabi.com",
    "so-simple.org",
    "mail2karate.com"
]

email = input("Enter email: ").strip().split("@")
for b_email in BLACKLIST:
    if email[1] == b_email:
        print(f"Warning: Domain '{b_email}' is blacklisted.")
