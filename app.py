from flask import Flask, render_template, jsonify,request
from database import add_user

Coins = [
  {
    'coin_id':'BTC',
    'name':'Bitcoin',
    'price':'2340000',
    'rate':'1.12%'
  },
  {
    'coin_id':'ETH',
    'name':'Etherum',
    'price':'146000',
    'rate':'5.56%'
  },
  {
    'coin_id':'DOGE',
    'name':'DOGE Coin',
    'price':'5.56 INR',
    'rate':'6.7%'
  },
  {
    'coin_id':'SHIB',
    'name':'SHIBHA INU',
    'price':'0.0045',
    'rate':'3.45%'
  }, 
]
app = Flask(__name__)

@app.route("/") 
def home_page():
  return render_template('index.html')

@app.route("/dashboard")
def dashboard():
  return render_template('dashboard.html')

@app.route("/about_us")
def about_us():
  return render_template('about_page.html')

@app.route("/trade_page")
def trade_page():
  return render_template('trade_page.html',coin=Coins)


@app.route("/register", methods=['GET','POST'])

def register():
  if request.method == 'POST':
    new_data = request.form
        # Insert new_data to database
    add_user(new_data.to_dict())
    return 'USER ADDED !! You can go back and Login Now!'
    # return jsonify(new_data)
    # return 'success'
    
  return render_template('register_page.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

