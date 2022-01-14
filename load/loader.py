import sqlite3
import datetime


class Loader:
    def __init__(self):
        self.con = sqlite3.connect(f'data/recruits_{datetime.date.today()}.db')
        self.cur = self.con.cursor()
        self.__create_table()

    def __create_table(self):
        create_sql = f'''CREATE TABLE IF NOT EXISTS recruits(
            id integer primary key,
            url text,
            title text,
            region text,
            company text,
            emp_type text,
            start_date text,
            end_date text,
            category text,
            created_date date,
            unique (url, title)
        )'''
        self.cur.execute(create_sql)

    def load(self, data):
        insert_sql = f'''INSERT into recruits(url, title, region, company, emp_type, start_date, end_date, category, created_date)
            values (?, ?, ?, ?, ?, ?,?, ?, ?)'''
        params = (data.url, data.title, data.region, data.company, data.employee_type,
                  data.start_date, data.end_date, data.category, data.created_date,)
        self.cur.execute(insert_sql, params)

    def load_list(self, data_list):
        for data in data_list:
            self.load(data)

        self.con.commit()
        self.con.close()
