import random
from src.api.helpers.general_helpers import return_random_product_type
from src.api.helpers.general_helpers import create_random_string
from src.api.helpers.general_helpers import generate_random_email

class WooPayloadHelpers:
    def create_random_product_payload(self,product_name=None,product_type=None,regular_price=None,stock_quantity=None,**kwargs):
        if not product_type:
            product_type = return_random_product_type()
        random_string = create_random_string()
        if not product_name:
            product_name = "Test Product" +" "+ random_string
        if not regular_price:
            regular_price = str(random.randint(10,999))
        if not stock_quantity:
            stock_quantity = 100

        description = create_random_string()
        product_payload = {
            "name":product_name,
            "type":product_type,
            "description":description,
            "manage_stock":True,
            "regular_price":regular_price,
            "stock_quantity":stock_quantity,
            "categories":[
                {

                }
            ],
            "images":[
                {

                },
                {

                }
            ]

        }
        categories_update = kwargs.pop('categories_update',{})
        if categories_update:
            product_payload['categories'][0].update(categories_update)
        images_update = kwargs.pop('images_update', [])
        if images_update:
            product_payload['images'] = images_update
        if kwargs:
            product_payload.update(kwargs)
        return product_payload

    def create_random_order_payload(self,product_id,quantity=None, **kwargs):
        if not quantity:
            quantity = 1
        random_email = generate_random_email()
        order_payload = {
            "set_paid":True,
            "billing":{
                "first_name":"",
                "last_name":"",
                "city":"",
                "email":random_email
            },
            "line_items":[
                    {
                        "product_id":product_id,
                        "quantity":int(quantity)
                    }

                ],
            "shipping":{
                "first_name":"",
                "last_name": "",
                "city": "",
                "email": random_email

            }

        }
        line_item_updates = kwargs.pop('line_item_updates',{})
        if line_item_updates:
            order_payload["line_items"][0].update(line_item_updates)

        billing_updates = kwargs.pop('billing_updates',{})
        if billing_updates:
            order_payload['billing'].update(billing_updates)

        shipping_updates = kwargs.pop('shipping_updates',{})
        if shipping_updates:
            order_payload['shipping'].update(shipping_updates)

        if kwargs:
            order_payload.update(kwargs)

        return order_payload

    def create_a_customer_payload(self,email=None,**kwargs):
        if not email:
            email = generate_random_email()
        first_name = "TestUser_"
        last_name = create_random_string()
        password = create_random_string()
        customer_payload = {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "password":password,
            "billing": {
                "first_name": first_name,
                "last_name":last_name,
                "email":email
            },
            "shipping":
            {
                "first_name":first_name,
                "last_name":last_name

            }
        }
        billing_updates = kwargs.pop('billing_updates',{})
        if billing_updates:
            customer_payload['billing'].update(billing_updates)

        shipping_updates = kwargs.pop('shipping_updates',{})
        if shipping_updates:
            customer_payload['shipping'].update(shipping_updates)
        if kwargs:
            customer_payload.update(kwargs)
        return customer_payload

    def create_a_coupon_payload(self,coupon_code=None,discount_type=None,discount_amount=None,**kwargs):
        if not discount_type:
            discount_type = "percent"
        if not coupon_code:
            coupon_code="test_coupon_"+create_random_string(string_length=3).lower()
        if not discount_amount:
            discount_amount = 100
        coupon_payload = {
            "code":coupon_code,
            "discount_type":discount_type,
            "amount":str(discount_amount),
            "individual_use": True,
            "exclude_sale_items": False,
            **kwargs
        }
        if kwargs:
            coupon_payload.update(kwargs)

        return coupon_payload