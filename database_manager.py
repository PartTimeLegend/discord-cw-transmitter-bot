import mysql.connector

class DatabaseManager:
    def __init__(self, config):
        self.config = config

    def __enter__(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def insert_transmission(self, sender, frequency, message, cw_message):
        sql = "INSERT INTO transmissions (sender, frequency, message, cw) VALUES (%s, %s, %s, %s)"
        values = (sender, frequency, message, cw_message)
        self.cursor.execute(sql, values)
        self.connection.commit()
