from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', height=8, width = 8, color1 = "red", color2 = "black")

@app.route('/<int:height>')
def heightOfBoard(height):
    return render_template('index.html', height=height, width = 8, color1 = "red", color2 = "black")

@app.route('/<int:width>/<int:height>/')
def widthAndHeightOfBoard(width, height):
    return render_template('index.html', width = width, height = height, color1 = "red", color2 = "black")

@app.route('/<int:width>/<int:height>/<color1>/<color2>')
def changeColors(width, height, color1, color2):
    return render_template('index.html', width = width, height = height, color1 = color1, color2 = color2)

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry! No response. Try again."

# no code past this line
if __name__ == "__main__":
    app.run(debug=True)