from flask import Flask, render_template, jsonify,request

app = Flask(__name__)

@app.route("/") 
def home_page():
  return render_template('index.html')

@app.route("/")
def test():
  return render_template('index.html')

@app.route("/about_us")
def about_us():
  return render_template('about_page.html')

@app.route("/trade_page")
def trade_page():
  return render_template('trade_page.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

