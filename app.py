#1. Ensure you have initialised a virtual environment 'virtualenv .'
#2. Ensure flask is installed by running 'pip install flask'.
#3. Run the app from command line with 'flask run'.

from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/')
def my_func():

    user = "Matt"

    return render_template('index.html', title="Index", username=user)

@app.route('/list')
def another_route():
    
    names = ["Adam", "Alan", "Chris", "Gav", "John", "Matt", "Sean", "Steve", "Stuart"]
    
    return render_template('list.html', title="List", names=names)

app.run()