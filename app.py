from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Variable partagée pour stocker la valeur
shared_value = 0


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('increment')
def handle_increment():
    global shared_value
    shared_value += 1
    emit('update_value', {'value': shared_value}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)
