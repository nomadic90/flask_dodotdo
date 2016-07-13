import pyaudio
import time
import js2py

WIDTH = 2
CHANNELS = 2
RATE = 48000

# js part

context = js2py.EvalJs({'python_sum':sum})
js_code = '''
var io = require('socket.io')(server) 
function connection(){
	var namespace = '/test';
	var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

	socket.on('connected', function(msg){
		console.log(msg.data);
	});
}

'''
context.execute(js_code)
print context.add()


		# socket.on('speak', function(stream){
		# 	emit('listen', {'data' : stream})
		# });

		# socket.on('broadcast', function(stream){

		# });

		# function socketio(stream) {
		# 	try{
		# 		var namespace = '/test';
		# 		var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

		# 		socket.on('connected', function(msg){
		#     		console.log(msg.data);
		#     	});
				
		# 	}catch(e){
		# 		console.log(e);
		# 	}
		# }


p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)


stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()