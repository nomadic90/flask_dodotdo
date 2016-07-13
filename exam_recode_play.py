from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None

outputWav = None

@app.route('/')
def index():
	return render_template('index1.html')
	# return render_template('good_example_getusermedia_audio.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('connected', {'data': 'Connected'})
    print 'connected\n'

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)

@socketio.on('speak', namespace = '/test')
def test_speak(chunk):

	emit('broadcast', {'data': chunk['data']})

@socketio.on('my event', namespace = '/test')
def test_msg(message):
	emit('my response', {'data' : message['data']})
	print message


if __name__ == '__main__':
    socketio.run(app, debug=True)
