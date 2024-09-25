import os
from pathlib import Path
from dotenv import load_dotenv

from Errors import MissingEnvVarError
from SendGridClient.SendGridClient import SendGridClient
from SendGridClient.Templates import Template
from Validators.Validators import Validate

env_path = Path(".") / ".env.development"
load_dotenv(dotenv_path=env_path)
APIKEY = os.getenv("SENDGRID_API_KEY")


if __name__ == "__main__":
        if APIKEY is None:
            raise MissingEnvVarError("You havent set the API key in .env.development")

        recipient_email = "steffenhvid@gmail.com"
        sender_email = "no_reply@smartsave.dk"
        template = Template.Order
        dynamic_data = {
            "name": "John Doe",
            "order_id": "12345",
            "products": [
                {
                    "name": "Product 1", 
                    "price": 19.99, 
                    "description": "A great product"},
                {
                    "name": "Product 2",
                    "price": 29.99,
                    "description": "An even better product",
                },
                {
                    "name": "Product 3", 
                    "price": 39.99, 
                    "description": "The best product"
                },
            ],
        }

        if not Validate.email(recipient_email):
              print("Recipient email is not valid")

        elif not Validate.email(sender_email):
              print("Sender email is not valit")
        
        elif not Validate.template(template):
              print("The template you have provided is not defined")
        
        elif not Validate.dynamic_data(template, dynamic_data):
              print("The body you have provided does not contain the correct properties.")

        else:
            send_grid_client = SendGridClient(APIKEY)
            send_grid_client.send_email(recipient_email, sender_email, template, dynamic_data)
            print("Succes!")