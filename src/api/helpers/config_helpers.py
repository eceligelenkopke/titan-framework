import os

class ConfigHelper:
    def __init__(self):
        pass

    @staticmethod
    def get_api_credentials():
        wc_key = os.environ.get('WC_KEY')
        wc_secret = os.environ.get('WC_SECRET')
        if not wc_key or not wc_secret:
            raise Exception('API Credentials "WC_KEY" and "WC_SECRET" must be in env variable.')
        else:
            return {
                "WC_KEY":wc_key,
                "WC_SECRET":wc_secret
            }

    @staticmethod
    def get_database_credentials():
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_host = os.environ.get('DB_HOST')
        db_name = os.environ.get('DB_NAME')
        db_port = os.environ.get('DB_PORT')
        if not db_user or not db_password:
            raise Exception('Database Credentials "DB_USER" and "DB_PASSWORD" must be in env variable.')
        if not db_host or not db_port:
            raise Exception('Database Credentials "DB_HOST" and "DB_PORT" must be in env variable.')
        if not db_name:
            raise Exception('Database Credential "DB_NAME" must be in env variable.')
        else:
            return {
                "DB_USER":db_user,
                "DB_PASSWORD":db_password,
                "DB_HOST":db_host,
                "DB_PORT":db_port,
                "DB_NAME":db_name

            }
    @staticmethod
    def get_base_url():
        url = os.environ.get('BASE_URL')
        if not url:
            raise Exception("API and Selenium Credential URL must be in env variable.")

        else:
            return url

