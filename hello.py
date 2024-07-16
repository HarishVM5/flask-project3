from flask import Flask
app=Flask('__name__')
@app.route('/')
def hello():
    return "<h1>Hello </h1>"

@app.route('/Hi')
def hello1():
    return "<h1>Hello Harish!</h1>"

@app.route('/vm')
def hello2():
    return "<h1>Hello Harish! How are you?</h1>"


if __name__=='__main__':
    app.run(debug=True)

