from sqlalchemy import create_engine, text
import os

#Do not use " " in seceret
my_secret = os.environ['DB_CONNECTION_STRING']
#this info is senstive never share it in github!!
engine = create_engine(my_secret)

with engine.connect() as conn:
  print("\n\n---------------Connection Established!----------------\n\n")
  result = conn.execute(text("select * from todo"))

  li = []
  for row in result.all():
    result_dicts = {}
    result_dicts["id"] = list(row)[0]
    result_dicts["title"] = list(row)[1]
    result_dicts["time"] = list(row)[2]
    result_dicts["slaray"] = list(row)[3]
    # print(list(row)[0])
    li.append(result_dicts)

  print(li)

# def load_id(id):
#   with engine.conn() as conn:
#     result = conn.execute(text("select * from todo where id= :val"),val=id)
#     rows = result.all()
#     if(len(rows)==0):
#       return None
#     else:
#       return dict(rows[0])


def add_todo_db(data):
  
  with engine.connect() as conn:
    print("\n\nData is:\n\n", data)
    print("\n\n")
    query = text(
      "INSERT INTO todo(title,time,slaray) values(:title ,:time ,:salary)")
    conn.execute(
      query, dict(title=data['title'],
                  time=data['time'],
                  salary=data['salary']))
   
    conn.commit()
    print("\n\n----Updated DB-----\n\n")