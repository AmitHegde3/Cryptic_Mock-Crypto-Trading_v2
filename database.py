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
    result = conn.execute(text("select wallet,ac_id from account WHERE email=:x"),{'x':emailf})

    for r in result.all():
      test_val = list(r)[0]
      id = list(r)[1]
      
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
      return True,id
      
    else:
      return False,0
    
#----------------------------------------------------------------- Add sell function here ------------------------------------
def sell(data,amt_coin):
  
  with engine.connect() as conn:
    # First get the wallet balance....Just pesudo code for now...
    # print("\n\nEmail:",emailf)
    # test = "hegdeamit21@gmail.com"
    result = conn.execute(text("select wallet,ac_id from account WHERE email=:x"),{'x':emailf})

    for r in result.all():
      test_val = list(r)[0]
      id = list(r)[1]
      
    print("\n\nVal: ",test_val)
    # print("\n\nType : ",type(result.all()))  it's a list
    prev_val= int(test_val)
    
    check = conn.execute(text("select sum(amount_of_coin) from my_coins where ac_id =:x"),{'x':id})

    for c in check.all():
      remain_amt = list(c)[0]

    if(remain_amt >= amt_coin):
      query = text(
        "UPDATE account SET wallet=:new_val WHERE email=:email")
      conn.execute(
        query, dict(new_val = prev_val + data,
                    email = emailf
                   ))
     
      conn.commit()
      return True,id,0
    else:
      return False,0,remain_amt
      
  
#----------------------------------------------------------------- Add sell function here ------------------------------------

#----------------------------------------------------------------- Add coin function ------------------------------------

def add_coin(id,name,price,amt):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO my_coins(ac_id,c_name,bought_price,amount_of_coin) values(:i,:x,:y,:z)")
    conn.execute(
      query, dict(
                  i = id,
                  x=name,
                  y = price,
                  z = amt
                 ))
   
    conn.commit()
    print("\n\n---- My Coins updated -----\n\n")
#----------------------------------------------------------------- Add coin function ------------------------------------

#----------------------------------------------------------------- IDIOT(ME) works here don't touch this section....Women dare touch this section ------------------------------------


#Working----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def validate(data):
#   global emailf
#   emailf = data.get('email')
#   passwordf = data.get('password') 
#   with engine.connect() as conn:
#     print("\n\n---------------Connection Established!---------------\n\n")
#     query = text("SELECT email, password FROM account WHERE email=:email")
#     result = conn.execute(query, {"email": emailf})
#     print('\n\nhooooooooooooooooooooooooo')
#     user = result.fetchone()
#     if user:
#       user_email, user_password = user
#       if user_password == passwordf:
#         return 'Login Successful!'
        
#       else:
#         return None
#     print("User retrieved!\n")


# def fetch_user_data(emailf):
#   with engine.connect() as conn:
#     print("\n\n---------------Connection to print names---------------\n\n")
#     query = text("SELECT name,email,wallet,acc_id FROM account WHERE email=:email")
#     result = conn.execute(query, {"email": emailf})
    
#     user_data = result.fetchone()
#     if user_data:
#       name,email,wallet,acc_id = user_data
#       return {"name": name, "email": email,"wallet":wallet}
#     else:
#       return None

# def validate(data):
#   global emailf
#   emailf = data.get('email')
#   passwordf = data.get('password') 
#   with engine.connect() as conn:
#     print("\n\n---------------Connection Established!---------------\n\n")
#     query = text("SELECT email, password FROM account WHERE email=:email")
#     result = conn.execute(query, {"email": emailf})
#     print('\n\nhooooooooooooooooooooooooo')
#     user = result.fetchone()
#     if user:
#       user_email, user_password = user
#       if user_password == passwordf:
#         return 'Login Successful!'
        
#       else:
#         return None
#     print("User retrieved!\n")

# def fetch_user_data(emailf):
#   with engine.connect() as conn:
#     print("\n\n---------------Connection to print names---------------\n\n")
#     query = text("SELECT ac_id,name,email,wallet FROM account WHERE email=:email")
#     result = conn.execute(query, {"email": emailf})
#     user_data = result.fetchone()
#     if user_data:
#       ac_id,name,email,wallet = user_data
#       query = text("SELECT ac_id,c_name,bought_price,amount_of_coin,id FROM my_coins WHERE ac_id=:ac_id")
#       result = conn.execute(query, {"ac_id": ac_id})
#       my_coins_data = result.fetchone()

#       if my_coins_data:
#         ac_id,c_name,bought_price,amount_of_coin,id =my_coins_data
#         return {"name": name, "email": email ,"wallet":wallet ,"ac_id":ac_id ,"c_name":c_name ,"bought_price":bought_price ,"amount_of_coin":amount_of_coin ,"id":id}


#     return{"name": name, "email": email ,"wallet":wallet ,"ac_id":ac_id}

def validate(data):
  global emailf
  emailf = data.get('email')
  passwordf = data.get('password') 
  with engine.connect() as conn:
    print("\n\n---------------Connection Established!---------------\n\n")
    query = text("SELECT email, password FROM account WHERE email=:email")
    result = conn.execute(query, {"email": emailf})
    print('\n\nhooooooooooooooooooooooooo')
    user = result.fetchone()
    if user:
      
      user_email, user_password = user
      if user_password == passwordf:
        return 'Login Successful!'
        
      else:
        return None
    print("User retrieved!\n")

def fetch_user_data(emailf):
  with engine.connect() as conn:
    print("\n\n---------------Connection to print names---------------\n\n")
    query = text("SELECT ac_id,name,email,wallet FROM account WHERE email=:email")
    result = conn.execute(query, {"email": emailf})
    user_data = result.fetchone()
    if user_data:
      ac_id,name,email,wallet = user_data
      query = text("SELECT * FROM my_coins WHERE ac_id=:ac_id  ORDER BY id ASC")
      result1 = conn.execute(query, {"ac_id": ac_id})
      # my_coins_data = result.fetchall()
      my_coins_data = []
      for row in result1:
        # ac_id,c_name,bought_price,amount_of_coin,id =result[i]
        result1_list = list(row)
        result1_list = {}
        result1_list["ac_id"] = list(row)[0]
        result1_list["c_name"] = list(row)[1]
        result1_list["bought_price"] = list(row)[2]
        result1_list["amount_of_coin"] = list(row)[3]
        result1_list["id"] = list(row)[4]

        my_coins_data.append(result1_list)
        
      return {"name": name, "email": email ,"wallet":wallet ,"ac_id":ac_id ,"transactions": my_coins_data,}


    return{"name": name, "email": email ,"wallet":wallet ,"ac_id":ac_id}


        
#Fucking Finally!!!! @idiothegde done. atlastttttttttttttttt......