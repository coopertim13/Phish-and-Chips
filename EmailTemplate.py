from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailTemplate:
    def __init__(self, recipient_email, recipient_full_name, recipient_first_name, recipient_record, sender_name, recipient, content, subject):
        self.recipient_email = recipient_email
        self.recipient_full_name = recipient_full_name
        self.recipient_first_name = recipient_first_name
        self.recipient_record = recipient_record
        self.sender_name = sender_name
        self.recipient = recipient
        self.content = content
        self.subject = subject
    
    def build(self):
        msg = MIMEMultipart('related')
        msg['Subject'] = self.subject
        msg['From'] = self.sender_name
        msg['To'] = self.recipient
 
        self.content = self.content.format(first_name=self.recipient_first_name, full_name=self.recipient_full_name, record=self.recipient_record, email=self.recipient_email)
        msg.attach(MIMEText(self.content, 'html'))

        return msg