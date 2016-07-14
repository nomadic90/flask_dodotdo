# Dodotdo : HW, Make realtime voice chat server

## Overview

Get to know about **Flask** is first priority for this homework and using socket to implement realtime data transmission. For make that I also build client part.

### Detail approach to this HW

1. **Pyaudio** which can implement microphone and record the sound and send the stream to the server and then server will emit the stream to everyone who is connected to the server, **But** this was not appropriate because I was thinking about record the sound in webpage which is local host so in the webpage record through microphone needs other method to implement. In the **Server** part I used socketio package for realtime data transmission. Figure is that really work was not proven because of keeping fail in the building client part.

	ㄴ **pyaudio** is python audio package which can capture audio and speaker in python code which is not useful for this HW.

2. Next day I tried to know about javascript method to use microphone which is **getUserMedia()**, but microphone in my Mac did not response without knowing the reason so I gave up using that even thougn in the tutorial part camera was working but microphone did not working at all. In the server part I was trying to send the chunk of stream because in the webpage it is impossible to send the stream during recording status. And in the server part, it will gather the chunk as a one stream and emit it to all as a stream also.

	ㄴ **getUserMedia()** is method that make access to the microphone and camera on the device but has a limitation on supporting problem that Safari in OSX and Internet Explorer can not use this method.

3. Next day I am currently working on building **Python client**, but get to know how socket works in just with python was difficult so I am figuring out how can i include javascript into the python client to connect to the server with socket which is event driven. In building python client, **js2py** package assume to be a candidate to solve this project but translator counldn't solve it because I failed to include header file from outside but translator didn't work well.

	ㄴ **js2py** is translator which exactly translate the javascript to python but drawback was impossible to include header files. Maybe I just failed to use this package correctly but it maybe not that useful for any project.


4. Finally success in capturing the microphone and play it. In the server part, received Blob file emited to every client. In the client part, recorded stream from microphone converted to blob type and passed to the **flask server**. And get the blob file from server and assign to **audio**'s src to play the blob file.

	ㄴ **SocketIo** is the main package building this project. Its purpose is create realtime transmission of data between web application and server.
	
5. Blob data in javascript turned out to be just referencing the microphone so throw blob to the server is not appropriate method for this HW. To throw the data from the microphone from the client is the most important thing. I didn't make that but creat buffer that receives data from microphone and emit the data to the server will help to make HW done successfully. I'm currently trying receiving buffer from blob or stream from microphone.