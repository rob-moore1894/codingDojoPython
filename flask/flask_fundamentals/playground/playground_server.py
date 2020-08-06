from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This is the homepage..."

@app.route('/play')
def renderPlay():
    return render_template('index.html')

@app.route('/play/<int:number>')
def renderPlayTimes(number):
    return render_template('index.html', number=number, color="lightblue")

@app.route('/play/<int:number>/<color>')
def changeColor(number, color):
    return render_template('index.html', number=number, color=color)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

# no code past this line
if __name__ == "__main__":
    app.run(debug=True)