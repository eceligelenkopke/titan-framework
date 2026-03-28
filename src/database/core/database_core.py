import pymysql


from src.api.helpers.config_helpers import ConfigHelper

class DBCore:
    def __init__(self):
        config_helper = ConfigHelper()
        self.db_credentials = config_helper.get_database_credentials()
    def create_connection(self):
        connection = pymysql.connect(host=self.db_credentials['DB_HOST'],
                                     port=int(self.db_credentials['DB_PORT']),
                                     user=self.db_credentials['DB_USER'],
                                     password=self.db_credentials['DB_PASSWORD'],
                                     db=self.db_credentials['DB_NAME']

        )
        return connection



    def execute_select(self,sql):
        connection = self.create_connection()
        try:
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sql)
            rs_dict = cursor.fetchall()
            cursor.close()
        except Exception as e:
            raise Exception(f"Failed running sql: {sql}\n Error {str(e)}")
        finally:
            connection.close()

        return rs_dict