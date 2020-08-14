from flask import Flask, render_template
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

@app.route('/lists')
def render_lists():
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age': 30},
        {'name' : 'Mark', 'age': 25},
        {'name' : 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers = [3, 1, 5], students = student_info)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

# no code past this line
if __name__ == "__main__":
    app.run(debug=True)