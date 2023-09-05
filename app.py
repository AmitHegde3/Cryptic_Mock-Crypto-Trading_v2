from flask import Flask, render_template, json, request, redirect, session,url_for
from database import *
from coin_api import coin



Coins = [
  {
    'coin_id': coin['BTC'][0], # ex : btc
    'name': coin['BTC'][1], # ex : bitcoin
    'price': coin['BTC'][2],
    'rate': coin['BTC'][3],
    
  },
  {
    'coin_id': coin['ETH'][0],
    'name': coin['ETH'][1],
    'price': coin['ETH'][2],
    'rate': coin['ETH'][3],
  },
  {
    'coin_id': coin['USDT'][0],
    'name': coin['USDT'][1],
    'price': coin['USDT'][2],
    'rate': coin['USDT'][3],
  },
  {
    'coin_id': coin['BNB'][0],
    'name': coin['BNB'][1],
    'price': coin['BNB'][2],
    'rate': coin['BNB'][3],
  },
]
app = Flask(__name__)

#----------------------------------------------------------------- God(ME) works here don't touch this section --------------------------------------------
@app.route("/")
def home_page():
  return render_template('index.html',)
  

@app.route("/about_us")
def about_us():
  return render_template('about_page.html')


@app.route("/trade_page")
def trade_page():
  return render_template('trade_page.html', coin=Coins,test=coin)


@app.route("/register", methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    new_data = request.form
    # Insert new_data to database
    add_user(new_data.to_dict())
    return 'USER ADDED !! You can go back and Login Now!'
    # 'USER ADDED !! You can go back and Login Now!', 
    # return jsonify(new_data)
    # return 'success'
  return render_template('register_page.html')


@app.route("/bought", methods=['GET', 'POST'])
def bought():
  if request.method == 'POST':
    bought_amt = request.form
    total_amt = int(bought_amt.to_dict()['buy_amt']) * int(coin['BTC'][2]) #total amount  = quantity * current price
    # print(total_amt)
    # print("\n\n",bought_amt)
    # print(type(bought_amt),"\n\n")
    # print("\n\n",bought_amt.to_dict()['buy_amt'],"\n\n")
  
    buy(total_amt)
    return 'Congratulation you have bought Bitcoin'
    # 'USER ADDED !! You can go back and Login Now!', 
    # return jsonify(new_data)
    # return 'success'

@app.route("/sold", methods=['GET', 'POST'])
def sold():
  if request.method == 'POST':
    sold_amt = request.form
    total_amt = int(sold_amt.to_dict()['sell_amt']) * int(coin['BTC'][2])
    sell(total_amt)
    return 'Congrats You have sold Bitcoin '
    # 'USER ADDED !! You can go back and Login Now!', 
    # return jsonify(new_data)
    # return 'success'

#----------------------------------------------------------------- God(ME) works here don't touch this section --------------------------------------------

@app.route("/dashboard",methods=['GET', 'POST'])

def dashboard():
  if request.method == 'POST':
    print("User retrieved!\n")
    data = request.form 
    validate(data.to_dict())
    return render_template('dashboard.html')
    
  return render_template('index.html') 



@app.route('/test')

def test():
  return render_template('test.html')
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
