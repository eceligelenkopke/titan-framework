import string
import random

def create_random_string(string_length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=string_length))

def generate_random_email():
    email_prefix = 'test_user'
    email_endpoint = '@gmail.com'
    return email_prefix + create_random_string() + email_endpoint

def generate_random_password():
    return create_random_string()

def return_random_product_type():
    accepted_product_types = ["simple"]
    return random.choice(accepted_product_types)
