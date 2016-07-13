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
@app.route('/test1/')
def test1():
	return render_template('test1.html')

@app.route('/test2')
def test2():
	return render_template('test2.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('connected', {'data': 'Connected'}, broadcast = True)
    print 'connected\n'

@socketio.on('connect', namespace='/test1/test')
def test_connect1():
    emit('connected #1', {'data': 'Connected #1'}, broadcast = True)
    print 'connected\n'

@socketio.on('connect', namespace='/test2/test')
def test_connect2():
    emit('connected #2', {'data': 'Connected #2'}, broadcast = True)
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

@socketio.on('speak_to_#1', namespace = '/test1/test')
def sp2one(chunk):
	emit('listen1', {'data': chunk['data']},  broadcast = True)

@socketio.on('speak_to_#2', namespace = '/test2/test')
def sp2two(chunk):
	emit('listen2', {'data': chunk['data']},  broadcast = True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
