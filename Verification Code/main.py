import smtplib

my_email = "qwerty@hotmail.com"
password = "qwerty" # My password to enter my account and send the message

with smtplib.SMTP("smtp.live.com") as connection:  # Closes connection automatically
    connection.starttls()  # Encrypts your connection so others can't access
    connection.login(user=my_email, password=password)

    connection.sendmail(from_addr=my_email,
                        to_addrs="recipient@hotmail.com",  # Recipient
                        msg="Subject: SMTP\n\nHello"  # Subject then message
                        )
