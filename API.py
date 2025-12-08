from flask import Flask, request, jsonify
import pymysql
import time
import unittest
import upload
from datetime import datetime, timedelta
import yaml


app = Flask(__name__)
with open("config.yml") as f:
    config = yaml.safe_load(f)
# config = 'config.yml'
conn = pymysql.connect(host=config['db']['host'], port=3306, user=config['db']['user'],
                            passwd=config['db']['pw'], db=config['db']['db'], autocommit=True)
cur = conn.cursor(pymysql.cursors.DictCursor)
table1 = "users"
table2 = "workouts"
table3 = "splits"
table4 = "strokes"
table5 = "workout"
table6 = "useige"
table7 = "club"
workid = 0
date_today = datetime.now().date()



@app.route('/')
def home():
    print('test')
    return 'test'

@app.route('/getData', methods=['GET'])
def getData():
    start_time = time.time()

    key = request.args.get('key')
    key_final = key


    # Run SQL
    sql = f"SELECT * FROM `{table6}` WHERE `userID` = %s ORDER BY timed DESC LIMIT 10;"
    cur.execute(sql, (key,))
    keycheck = cur.fetchall()
    if len(keycheck) == 0:
        return "wrong key"



    sql = f"SELECT * FROM `{table6}` WHERE `userID` = %s ORDER BY timed DESC LIMIT 10;"
    cur.execute(sql, (key,))
    data_usage = cur.fetchall()
    # print(sql)
    # print(key)
    if len(data_usage) >= 1:
        last_id = data_usage[0]["lastID"]


    else:
        last_id = 0



    # sql = f"SELECT * FROM `{table6}` WHERE `userID` = %s ORDER BY timed DESC LIMIT 10;"
    # cur.execute(sql, (key,))
    # data_use = cur.fetchall()
    # print(date_today)
    # print(data_usage[9]["date_time"])
    if len(data_usage) >= 10 and date_today == data_usage[9]["date_time"]:
        return "to many uses"






    sql = f"SELECT * FROM `{table1}` WHERE `partner_id` = %s ORDER BY `user_id`;"
    cur.execute(sql, (key,))
    data_users = cur.fetchall()
    amount = 0
    data_publish = {
        "rowers": []
    }

    for row in data_users:
        rower = {
            "name": row["name"],
            "workouts": []
        }
        amount += 1
        # data_publish["rowers"].append(row["name"])
        user_id = row["user_id"]
        sql = f"SELECT id FROM `{table5}` WHERE `user_id` = %s ORDER BY `id`;"
        cur.execute(sql, (user_id,))
        data_workedout = cur.fetchall()
        # data_publish["rowers"]["workouts"] = []


        for row in data_workedout:
            workout = {
                "workout": [],
                "strokes": []
            }
            # data_publish["rowers"]["workouts"].append(row)
            work_id = row["id"]
            sql = f"SELECT * FROM `{table2}` WHERE `id` = %s and id > %s ORDER BY `id`;"
            cur.execute(sql, (work_id, last_id))
            data_workout = cur.fetchall()
            rower["workouts"].append(data_workout)



            sql = f"SELECT * FROM `{table3}` WHERE `id` = %s and id > %s group by `id`, `Splitnr`;"
            cur.execute(sql, (work_id, last_id))
            data_splits = cur.fetchall()
            workout["workout"].extend(data_splits)


            sql = f"SELECT * FROM `{table4}` WHERE `id` = %s and id > %s order by `id`, `strokenr`;"
            cur.execute(sql, (work_id, last_id))
            data_strokes = cur.fetchall()
            workout["strokes"].extend(data_strokes)

        rower["workouts"].append(workout)

        for key, value in row.items():
            if isinstance(value, bytes):
                row[key] = value.decode('utf-8', errors='replace')
        data_publish["rowers"].append(rower)
    time_run = time.time() - start_time
    data_use = {

        "userID": key_final,
        "time_run": time_run,
        "lastID": work_id,
        "amount_of_data": amount,
        "date_time": date_today,
    }
    u_stroke = upload.baseObject()
    u_stroke.set(data_use)
    u_stroke.insert(table="useige")

    return jsonify(data_publish)





if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)
print(app.url_map)
