from flask import Flask,render_template, session, redirect
from functools import wraps
from user.models import User, Product
import pymongo

app = Flask(__name__)
app.secret_key = b':\xe8\xcc\xb9\xbd\xeb\xb1f$\xaf\xec\xf6\x8eW\x92~'

#Database
client = pymongo.MongoClient('localhost',27017)
db = client.user_login_system



@app.route('/user/signup/',methods = ['POST'])
def signup():
    return User().signup()

@app.route('/user/signout/')
def signout():
    return User().signout()


@app.route('/user/login/', methods = ['POST'])
def login():
    return User().login()

@app.route('/user/my_auction/', methods = ['GET','POST' ])
def user_my_auction(): 
    return Product().my_auction()


@app.route('/myauctions/')
def my_auction():
    return render_template('myauctions.html')

@app.route('/sellhistory/')
def sell_history():
    return render_template('sell_history.html')

@app.route('/back/')
def my_auction_back():
    return render_template('First.html')

@app.route('/back_1/')
def sell_history_back():
    return render_template('myauctions.html')




@app.route('/buyproducts/')
def buy_product():
    return render_template('BuyProducts.html')

@app.route('/laptop/')
def laptop():
    return render_template('laptop.html')

@app.route('/ball/')
def ball():
    return render_template('ball.html')


@app.route('/back_2/')
def buy_product_back():
    return render_template('First.html')


@app.route('/bid_history/')
def bid_history():
    return render_template('bid_history.html')

@app.route('/back_4/')
def bid_history_back():
    return render_template('BuyProducts.html')

#Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
    return wrap

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard/')
@login_required
def dashboard():
    return render_template('First.html')




if __name__ == "__main__":
    app.run(debug=True)
