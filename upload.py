import yaml
from pathlib import Path
import pymysql
import datetime


class baseObject:
    def __init__(self, config_path='config.yml'):
        self.fields = []
        self.data = []
        self.pk = None
        self.errors = []
        self.config_path = config_path
        self.config = yaml.safe_load(Path(self.config_path).read_text())
        #self.tn = self.config['tables'][type(self).__name__]
        #print(self.tn)
        self.conn = pymysql.connect(host=self.config['db']['host'], port=3306, user=self.config['db']['user'],
                                    passwd=self.config['db']['pw'], db=self.config['db']['db'], autocommit=True)


        self.cur = self.conn.cursor(pymysql.cursors.DictCursor)

        # print('self.field = ', self.fields)
        # print("self.data =", self.data)
        # print()

    def set(self, d):
        # print("data property of the object before set is")
        # print(self.data)
        self.data = []
        self.data.append(d)
        # print("data property of the object after set is")
        # print(self.data)

    def getFields(self, tn):
        self.fields = []
        sql = f"DESC `{tn}`"
        self.cur.execute(sql)
        for row in self.cur:
            if row['Extra'] == 'auto_increment':
                self.pk = row['Field']
            else:
                self.fields.append(row['Field'])
        # print(self.fields)

    def insert(self, n=0, table="workouts"):
        # print("data property of the object before insert is")
        # print(self.data)
        self.getFields(table)
        sql = f'INSERT INTO `{table}` ('
        vals = ''
        tokens = []
        for field in self.fields:
            if field in self.data[n].keys():
                tokens.append(self.data[n][field])
                sql += f'`{field}`,' + ' '
                vals += '%s, '
        sql = sql[0:-2]
        vals = vals[0:-2]
        sql += ') VALUES '
        sql += f'({vals});'
        # print(sql,tokens)
        self.cur.execute(sql, tokens)
        self.data[n][self.pk] = self.cur.lastrowid
        # print("data property of the object after insert is")
        # print(self.data)


    def getByField(self, value, fieldname, table, entry):
        data = []
        sql = f'''SELECT * FROM `{table}` WHERE `{fieldname}` = %s;'''
        self.cur.execute(sql,[value])
        for row in self.cur:
            self.id = row[entry]
        #print("data property of the object after getbyfield is")
        #print(self.data)
        return self.id











