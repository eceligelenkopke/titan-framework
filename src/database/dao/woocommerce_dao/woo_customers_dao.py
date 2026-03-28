from src.database.core.database_core import DBCore

class WooCustomersDao:
    def __init__(self):
        self.db_core = DBCore()
        cursor = self.db_core.create_connection()

    def get_all_customers(self):
        sql = f"SELECT * FROM wp_users;"
        return self.db_core.execute_select(sql)

    def get_a_customer_by_id(self,customer_id):
        sql = f'SELECT * FROM wp_users where ID= {customer_id};'
        return self.db_core.execute_select(sql)[0]

    def get_a_customer_by_email(self,email):
        sql = f'SELECT * FROM wp_users where user_email="{email}";'
        return self.db_core.execute_select(sql)[0]

    def get_the_latest_customer(self):
        sql = f'SELECT * FROM wp_users ORDER BY ID DESC LIMIT 1;'
        return self.db_core.execute_select(sql)[0]

    def get_a_customer_by_username(self,username):
        sql = f'SELECT * FROM wp_users WHERE user_nicename = "{username}";'
        return self.db_core.execute_select(sql)[0]

    def get_a_customer_email_by_user_email(self,user_email=None):
        sql = f'SELECT * FROM wp_users where user_email = "{user_email}";'
        return self.db_core.execute_select(sql)[0]['user_email']
