from sqlalchemy import create_engine, text, Column, String
import os
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

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
    result = conn.execute(text("select wallet from account WHERE email=:email"),dict(email=globalemail))
    prev_val= int(result.all()[0])
    query = text(
      "UPDATE account SET wallet=:new_val WHERE email=:email)
    conn.execute(
      query, dict(new_val = prev_val - data,
                  email = globalemail
                 ))
   
    conn.commit()
    print("\n\n---- USER ADDED -----\n\n")
    
#----------------------------------------------------------------- IDIOT(ME) works here don't touch this section....Women dare touch this section -------------------------------------
# def validate(data):
#   emailf = data.get('email')
#   passwordf = data.get('password') 
#   with engine.connect() as conn:
#     print("\n\n---------------Connection Established!---------------\n\n")
#     query = text(""SELECT email, password FROM account WHERE email = :email"")
#     result = conn.execute(query, {"email1": data['email'], "password1": data['password']})
#     #conn.execute(query, dict(email=data['email'],
#                   #password=data['password']))
#     if email==email1 and password == password1 :
#       print("User retrieved!\n")
#     # print(list(row)[0])

def validate(data):
    with engine.connect() as conn:
        print("\n\n---------------Connection Established!---------------\n\n")
        
        query = text("SELECT email, password FROM account WHERE email = :email1 AND password = :password1")
        
        result = conn.execute(query, {"email1": data['email'], "password1": data['password']})
        
        account = result.fetchone()
        
        if account:
            email_result = account.index(['email'])
            password_result = account.index(['password'])
            
            # Check if the email and password match
            if email_result == data['email'] and password_result == data['password']:
                print("User retrieved and email/password match!\n")
            else:
                print("User retrieved, but email/password do not match!\n")
        else:
            print("User not found in the database!\n")




    # with engine.connect() as conn:
  
    #   print("User retrieved!\n")
    #   if request.method == 'POST'and 'email' in request.form and 'password' in request.form:
    #     email = request.form['email']
    #     password = request.form['password']
    #     result = conn.execute(
    #       'SELECT :email,:password FROM accounts WHERE email = %s AND password = %s', (
    #         email,
    #         password,
    #       ))
    #     account = result.fetchone()
    #     print("User retrieved!\n")
    #     if account:
    #       session['loggedin'] = True
    #       session['id'] = account['id']  # Corrected field name to 'id'
    #       session['email'] = account['email']  # Corrected field to'email'
   
    #       result = conn.execute('SELECT * FROM accounts WHERE id = %s',
    #                           (session['id'], ))
    #       account = result.fetchone()
    #   conn.commit()
    #   print("User retrieved!\n")
  

# trying differnt method
