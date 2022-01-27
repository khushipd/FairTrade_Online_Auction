from flask import Flask, jsonify, request, session, redirect
import bcrypt 
import uuid

from werkzeug.utils import redirect

class User:

    def start_session(self,user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200
    
    def signup(self):
        print(request.form)

# Create the user object

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('Fullname'),
            "email": request.form.get('E-mail'),
            "contact no.": request.form.get('Contact No.'),
            "username": request.form.get('Username'),
            "password": request.form.get('Password'),
        }

        # Encrypt the password
        
        user['password'] = bcrypt.hashpw((user['password']).encode('utf-8'),bcrypt.gensalt())
        
        from app import db


        # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        session.clear()
        return redirect('/')

    
    
    def login(self):
        from app import db
        user = db.users.find_one({
            "username": request.form.get('Username')
        })
        
        new_pass = bcrypt.hashpw(request.form.get('Password').encode('utf-8'),bcrypt.gensalt())
        
        if user and (bcrypt.checkpw(request.form.get('Password').encode('utf-8'), user['password'])):
            return self.start_session(user)

        
        return jsonify({"error":"Invalid Login Credentials"}), 401

class Product: 
    def my_auction(self):
        print(request.form)

        # from app import db
        product = {
            "_id": uuid.uuid4().hex,
            "Productname": request.form.get('productname'),
            "Description": request.form.get('description'),
            "End_date": request.form.get('end_date'),
            "Starting_price": request.form.get('starting_price'),
            "Img": request.form.get('img'),
        }
        return jsonify({"success": "Sussessful"}), 200
