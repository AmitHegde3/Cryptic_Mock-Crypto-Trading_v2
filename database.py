from sqlalchemy import create_engine, text, Column, String
import os
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
emailf = ''
#Do not use " " in seceret
my_secret = os.environ['DB_CONNECTION_STRING']
#this info is senstive never share it in github!!
engine = create_engine(my_secret)

#----------------------------------------------------------------- God(ME) works here don't touch this section --------------------------------------------
with engine.connect() as conn:
  print("\n\n---------------Connection Established!----------------\n\n")
  result = conn.execute(text("select * from account"))

  li = []
  for row in result.all():
    result_dicts = {}
    result_dicts["id"] = list(row)[0]
    result_dicts["title"] = list(row)[1]
    result_dicts["time"] = list(row)[2]
    result_dicts["slaray"] = list(row)[3]
    # print(list(row)[0])
    li.append(result_dicts)

  # print(li)



def add_user(data):
  
  with engine.connect() as conn:
    query = text(
      "INSERT INTO account(email,password,name,age,country) values(:email,:password,:name,:age,:country)")
    conn.execute(
      query, dict(email=data['email'],
                  password=data['password'],
                  name=data['name'],
                  age = data['age'],
                  country = data['country']
                 ))
   
    conn.commit()
    print("\n\n---- USER ADDED -----\n\n")

def buy(data):
  
  with engine.connect() as conn:
    # First get the wallet balance....Just pesudo code for now...
    # print("\n\nEmail:",emailf)
    # test = "hegdeamit21@gmail.com"
    result = conn.execute(text("select wallet from account WHERE email=:x"),{'x':emailf})

    for r in result.all():
      test_val = list(r)[0]
      
    print("\n\nVal: ",test_val)
    # print("\n\nType : ",type(result.all()))  it's a list
    prev_val= int(test_val)
    
    if(prev_val >= data):
      query = text(
        "UPDATE account SET wallet=:new_val WHERE email=:email")
      conn.execute(
        query, dict(new_val = prev_val - data,
                    email = emailf
                   ))
     
      conn.commit()
      return True
      
    else:
      return False
    
    
#----------------------------------------------------------------- IDIOT(ME) works here don't touch this section....Women dare touch this section ------------------------------------


def validate(data):
  global emailf
  emailf = data.get('email')
  passwordf = data.get('password') 
  with engine.connect() as conn:
    print("\n\n---------------Connection Established!---------------\n\n")
    query = text("SELECT email, password FROM account WHERE email=:email")
    result = conn.execute(query, {"email": emailf})
    user = result.fetchone()
    
    if user:
      user_email, user_password = user
      if user_password == passwordf:
        return 'Login Successful'
      else:
        return "Invalid password"
    print("User retrieved!\n")

#Fucking Finally!!!! @idiothegde done. atlastttttttttttttttt......