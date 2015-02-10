from flask import render_template, request, jsonify, redirect
from app import app
import urllib2
import json

def fetchJson(query):
    answer = json.load(urllib2.urlopen("http://downey-n1.cs.northwestern.edu:8080/wikifier/wiki/title/suggest/"+query))
    return answer

@app.route('/')
@app.route('/index')
def index():

    return render_template("index.html")


@app.route('/temp', methods=['POST'])
def temp():

    jsonResult = request.get_json();

    if jsonResult is not None: 
        queryString = jsonResult["query"];    
        optionId = jsonResult["option"];
        posts = fetchJson(queryString)["response"];
        result ='queryString: '+queryString+'<br>'+'optionId: '+optionId;      
        for post in posts:
            result = result + '<p><b>titleId</b>: '+post["title"]+ ', <b>title</b>: '+post['title']+'</p>';
        return jsonify({"success":True, "result":result})
    return jsonify({"success":False})
