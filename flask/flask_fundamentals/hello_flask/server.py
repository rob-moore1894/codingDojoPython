from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def sayHi(name):
    return(f"Hi, {name}")

@app.route('/repeat/<int:number>/<phrase>')
def repeat(number,phrase):
    return phrase * number

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

# no code past this line
if __name__ == "__main__":
    app.run(debug=True)