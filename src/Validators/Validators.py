import re
import SendGridClient.Templates as t

class Validate:
    def email(email:str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))
    
    def template(template:str) -> bool:
        return template in t.Template
    
    def dynamic_data(template:str, data:dict) -> bool:
        match template:
            case t.Template.Order:
                order_rules = t.OrderRules()
                return order_rules.Validate(data)
            case _:
                return False

