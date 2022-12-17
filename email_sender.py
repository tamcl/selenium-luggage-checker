import smtplib, ssl

class emailSender:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, email, status_change):
        port = 587  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = self.email  # Enter your address
        receiver_email = email  # Enter receiver address
        password = self.password
        message = f"""\
        Subject: Luggage checker alert

        Hi, this is the automatic luggage detecter.
        Your status has changed to {status_change}
        """

        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)