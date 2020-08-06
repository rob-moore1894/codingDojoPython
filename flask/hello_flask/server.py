from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homepage.html')

@app.route('/aew')
def aewPage():
    return 'All Elite Wrestling'

@app.route('/aew/tagteams')
def tagTeams():
    return 'Young Bucks, SCU, Dark Order, Kenny and Hangman, Sonny and Joey'

@app.route("/saysomething/<wordToSay>/<int:numTimes>")
def saySomething(wordToSay, numTimes):
    return wordToSay * numTimes



# no code past this line
if __name__ == "__main__":
    app.run(debug=True)