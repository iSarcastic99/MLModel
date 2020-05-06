 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:26:22 2020

@author: rahulss
"""
from flask import Flask, request, jsonify
from ratingUpd import addRate

app = Flask(__name__)

@app.route("/rating/add", methods=['POST'])
        
def addRating():
    jobID = request.form['jobID']
    userID = request.form['userID']
    rating = request.form['rating']
    print(userID," ",jobID," ",rating)
    status = addRate(userID, jobID, rating)

    return status
    
    # Running the server in localhost:5000 
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
