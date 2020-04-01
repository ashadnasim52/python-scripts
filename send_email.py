import smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Ashad Nasim'
email['to'] = 'ashadnasim@gmail.com'
email['subject'] = 'Lets see if it works or not'

email.set_content(html.substitute({'name': 'Ashad'}), 'html')

with smtplib.SMTP(host='smtp.gamil.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('ashad@gmail.com', 'pasword')
    smtp.send_message(email)
