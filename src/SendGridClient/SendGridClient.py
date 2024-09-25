from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from SendGridClient.Templates import Template

class SendGridClient:
    def __init__(self, apikey: str):
        self.apikey = apikey

    def send_email(self, to_email:str, from_email:str, template_name:Template, dynamic_data:dict):
        try:
            # Create the email object and populate it
            message = Mail(
                from_email=from_email,
                to_emails=to_email
            )
            message.template_id=template_name.value
            message.dynamic_template_data=dynamic_data

            sg = SendGridAPIClient(self.apikey)
            sg.send(message)
            
        except Exception as e:
            print(f"Error sending email: {e}")