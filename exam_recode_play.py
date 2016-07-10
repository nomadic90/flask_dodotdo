import pyaudio
import time
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None

WIDTH = 2
CHANNELS = 2
RATE = 48000

p = pyaudio.PyAudio()

@app.route('/')
def index():
    return render_template('index1.html', async_mode=socketio.async_mode)

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('connected', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected', request.sid)

@socketio.on('speak', namespace = '/test')
def test_speak(stream):
	emit('playback', {'play_stream':stream})

@socketio.on('my event', namespace = '/test')
def test_msg(message):
	emit('my response', {'data' : message['data']})


if __name__ == '__main__':
    socketio.run(app, debug=True)


# stream = p.open(format=p.get_format_from_width(WIDTH),
#                 channels=CHANNELS,
#                 rate=RATE,
#                 input=True,
#                 output=True,
#                 stream_callback=callback)

# stream.start_stream()

# while stream.is_active():
#     time.sleep(0.1)

# stream.stop_stream()
# stream.close()

# p.terminate()