import os
import mysql.connector
from datetime import date
from dotenv import load_dotenv

load_dotenv()


class UseMysql:
    def __init__(self):
        self.database = os.getenv("MY_SQL_DATABASE")
        self.host = os.getenv("MY_SQL_HOST")
        self.user = os.getenv("MY_SQL_USER")
        self.password = os.getenv("MY_SQL_PASSWORD")

        mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )

        self.mydb = mydb
        self.mydb.close()

    def __str__(self):
        representation = 'mysql'
        return representation

    async def select_query(self, column: str, table: str, condition_column: str = None, condition_value: str | int = None,
                           order_by_column: str = None, ascending: bool = True, limit: int = None, offset: int = 0):
        sql = f"SELECT {column} FROM {table}"

        if condition_column is None or condition_value is None:
            pass
        else:
            if type(condition_value) is str:
                sql += f" WHERE {condition_column} = '{condition_value}'"
            else:
                sql += f" WHERE {condition_column} = {condition_value}"

        if order_by_column is None:
            pass
        else:
            sql += f" ORDER BY {order_by_column}"

        if not ascending:
            sql += " DESC"

        if limit:
            sql += f" LIMIT {offset}, {limit}"

        self.mydb.connect()
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        output = mycursor.fetchall()
        self.mydb.close()
        return output

    async def bot_uses(self):
        today_date = date.today()
        self.mydb.connect()
        mycursor = self.mydb.cursor()
        sql = f"UPDATE bot_info set fandom_bot = fandom_bot + 1 WHERE date = '{today_date}'"
        mycursor.execute(sql)
        self.mydb.commit()
        self.mydb.close()
