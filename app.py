import os
from flask import request, Flask
from uuid import uuid4
import psycopg2

# from importlib import import_module
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# DB_STRING = 'postgresql+psycopg2://ucid:ucid@localhost:5432/ua_db_update'
# DB_STRING = config.DB_STRING
# engine = create_engine(DB_STRING, pool_pre_ping=True)
# session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))  # nopep8


# Create app
app = Flask(__name__)

conn = psycopg2.connect("dbname=ua_db_update user=ucid password=ucid")


def create_user(payload):
    name = payload.get('name')
    _id = str(uuid4())
    cur_name = 'insert'
    # cur = conn.cursor(cur_name, cursor_factory=psycopg2.extras.DictCursor)
    cur = conn.cursor(cur_name)
    sql = '''INSERT INTO user_details(user_id, user_name)
             VALUES(%s)'''

    # q = '''INSERT INTO user_details(user_id, user_name, likes, comments) VALUES (_id, name, 0,0);'''
    # cur.execute(sql, (vendor_name,))
    # cur.execute(sql.format(_id, name, 0, 0))
    # cur.execute(sql, (_id, name))
    cur.execute(sql, (_id, name))
    return True



@app.route('/new_user', methods=['POST'])
def submit():
    try:
        payload = request.get_json()
    except Exception as e:
        msg = "Bad Request. Error while decoding json: {}".format(e)
        return (msg)
    if create_user(payload):
        return "User inserted"
    return "Insertion task failed"



if __name__ == '__main__':
    app.run(debug=True, port = 5005)
