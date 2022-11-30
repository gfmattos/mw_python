from flask import Flask

app = Flask(__name__)

#1 HomePage

#1.1 Route

#1.2 Function
@app.route('/')
def homepage():
    return 'Thats my first site'

# Run Site
app.run()