# Dodotdo : HW, Make realtime voice chat server

## Overview

Get to know about **Flask** is first priority for this homework and using socket to implement realtime data transmission. For make that I also build client part.

### Detail approach to this HW

1. **Pyaudio** which can implement microphone and record the sound and send the stream to the server and then server will emit the stream to everyone who is connected to the server, **But** this was not appropriate because I was thinking about record the sound in webpage which is local host so in the webpage record through microphone needs other method to implement. In the **Server** part I used socketio package for realtime data transmission. Figure is that really work was not proven because of keeping fail in the building client part.

2. Next day I tried to know about javascript method to use microphone which is **getUserMedia()**, but microphone in my Mac did not response without knowing the reason so I gave up using that even thougn in the tutorial part camera was working but microphone did not working at all. In the server part I was trying to send the chunk of stream because in the webpage it is impossible to send the stream during recording status. And in the server part, it will gather the chunk as a one stream and emit it to all as a stream also.

3. Next day I am currently working on building **Python client**, but get to know how socket works in just with python was difficult so I am figuring out how can i include javascript into the python client to connect to the server with socket which is event driven.