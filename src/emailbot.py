import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email():

    def __init__(self, src, password, dest, title):
        self.src = src
        self.password = password
        self.dest = dest
        self.title = title
        self.send_email()

    def send_email(self):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(self.src, self.password)
        msg = self.generate_email()
        server.sendmail(self.src, self.dest, msg)
        server.quit()

    def generate_email(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.title
        msg['From'] = self.src
        msg['To'] = self.dest

        text = "Hi!\nThis is a test msg.\nHere is a link: http://example.com"
        html = """
        <html>
            <head></head>
            <body>
                <p>Hi!<br>
                    <b>This is a test msg.</b></br>
                    Here is a link: <a href="http://example.com">example.com</a>
                </p>
            </body>
        </html>
        """

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        return msg.as_string()


