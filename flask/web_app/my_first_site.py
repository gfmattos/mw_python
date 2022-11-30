from flask import Flask, render_template

app = Flask(__name__)

# HomePage
@app.route('/')
def homepage():
    return render_template('homepage.html')

# Contacts
@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

# Users
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

# Run Site
if __name__ == '__main__':
    app.run(debug=True)