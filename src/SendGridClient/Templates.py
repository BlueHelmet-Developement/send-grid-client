from enum import Enum

class Template(Enum):
    Order = 'd-273505aa493f42288d70049f1b9df8ed'

class OrderRules:
    required_keys_top_level = {'name', 'order_id', 'products'}
    required_product_keys = {'name', 'price', 'description'}

    def Validate(self,data:dict) -> str:
        if not self.required_keys_top_level.issubset(data):
            print(f"Missing top-level keys: {self.required_keys_top_level - data.keys()}")
            return False
        
        if not isinstance(data['products'], list):
            print("The 'products' field must be a list.")
            return False
        
        # Define required keys for each product
        required_product_keys = {'name', 'price', 'description'}
        
        # Validate each product
        for index, product in enumerate(data['products']):
            if not required_product_keys.issubset(product):
                missing_keys = required_product_keys - product.keys()
                print(f"Product {index + 1} is missing keys: {missing_keys}")
                return False
            
            # Check the types of each field in the product
            if not isinstance(product['name'], str):
                print(f"Product {index + 1} 'name' must be a string.")
                return False
            if not isinstance(product['price'], (int, float)):
                print(f"Product {index + 1} 'price' must be a number.")
                return False
            if not isinstance(product['description'], str):
                print(f"Product {index + 1} 'description' must be a string.")
                return False
        
        # If all checks pass
        return True
