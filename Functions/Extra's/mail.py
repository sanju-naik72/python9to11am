from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
message = "Thank you"
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()
server.login("ysrcpvote@gmail.com", "@vote9ysrcp")
server.sendmail("ysrcpvote@gmail.com", "mailmenaveenkumar@gmail.com", msg.as_string())
server.quit()
print("Mail Sent")