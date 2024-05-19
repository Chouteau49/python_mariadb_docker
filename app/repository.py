import mariadb

class Repository:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.conn = None

    def connect(self):
        try:
            self.conn = mariadb.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cur = self.conn.cursor()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            return False
        return True

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def select(self, query, params=None):
        try:
            self.cur.execute(query, params or ())
            return self.cur.fetchall()
        except mariadb.Error as e:
            print(f"Error executing SELECT query: {e}")
            return None

    def insert(self, query, params):
        try:
            self.cur.execute(query, params)
            self.conn.commit()
            return self.cur.lastrowid
        except mariadb.Error as e:
            print(f"Error executing INSERT query: {e}")
            self.conn.rollback()
            return None

    def update(self, query, params):
        try:
            self.cur.execute(query, params)
            self.conn.commit()
            return self.cur.rowcount
        except mariadb.Error as e:
            print(f"Error executing UPDATE query: {e}")
            self.conn.rollback()
            return None

    def delete(self, query, params):
        try:
            self.cur.execute(query, params)
            self.conn.commit()
            return self.cur.rowcount
        except mariadb.Error as e:
            print(f"Error executing DELETE query: {e}")
            self.conn.rollback()
            return None
