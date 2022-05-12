from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/rohan/<string:n>")
def rohan(n):
    sum = 0
    order=n
    copy_n= int(order) 
    sum = int(order)+ 10
    result = {
        "Number ":copy_n,
        "After + 10 ": sum,
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
    app.run(debug=True)
