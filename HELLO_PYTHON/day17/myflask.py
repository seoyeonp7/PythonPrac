from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/chat2')
def chatting():
    return render_template('chat2.html')

@app.route('/')
@app.route('/allready')
def allready():
    return render_template('allready.html')


@socket_io.on("message")
def request(message):
    print("message : "+ message)
    mydict = dict()
    mydict['message'] = message
    send(mydict, broadcast=True)



if __name__ == '__main__':
    socket_io.run(app, debug=True,host="0.0.0.0", port=9999)