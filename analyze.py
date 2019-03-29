from flask import *
app = Flask(__name__)

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/analyze', methods = ['POST'])
def getTopic():
    topic = request.form['topic']
    print("Your selected topic is '" + topic + "'")
    return redirect('/')

if __name__ == "__main__":
    app.run()
