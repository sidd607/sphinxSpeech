# sphinxSpeech
This project is a demo for using CMU Sphinx for live speech recognition in python and WebSpeech API of HTML5

The project contains two main file - liveRecognition.py and app.py

***
## live Speech Recognition using sphinx
sphinx is an open source speech recognition library written in Java and developed at Carnegie Mellon University. It uses hidden markov models for modelling speech. To run the demo, download the speech models from [English models](https://drive.google.com/folderview?id=0Bw00am7cLinWNWE4RnZuZkw5ODA&usp=sharing) and place the folder "pocketSphinx" and run the python script

```
$ python liveRecognition.py
```
once the script starts running you now start talking into the mic as long as you want and sphinx will convert your speech to text in real time.
for more details regarding Sphinx its installation visit [Sphinx](http://cmusphinx.sourceforge.net/)
***
## Speech Recognition using webSpeech API
Google has introduced its webSpeech API for speechk Recognition as part of HTML5 and is currently free to use. To Try out the the webSpeech demo run the flask server using
```
$ python app.py
```
Once the server is up and running you can try it out at */webSpeech*

## Portal for live speech recognition from browser using CMU Sphinx
*/sphinxDemo*

I have tried to implement a portal like Google Now for speech recognition using HTML5 and CMU Sphinx at the backend. My approach was as follows.

* First get the *getUserMedia()* of HTML working to access the mic and start recording sound.
* Recording an entire file and then sending it would be inefficient. So i created websockets to record voice in chunks of 1024 bytes and as a raw file to the server for processing.
* The above approach worked to the extent that I could get the voice data in chunks but was not able to process each chunk for live speech recognition.
* So I tried another approach. I send the voice data form the browser in chunks. The backend server recieves the chuns and starts building a .raw file, appending new each data it recieves to the existing .raw file to create a complete raw headerless media file for speech recognition.
* There was still some problem as I was not able to use Sphinx to transcribe the audio.
* There is a mismatch betweent the confuguration of the audio at which the browser records and the configuration required for sphinx. Sphinx requires a mono channel audio recorded at a sample rate of 16kHz. But the browser records a dual channel audio sampled at 44.1kHz.
* To try to resample the audio I habe written a couple of functions but they dont seem to work as efficiently as expected.
* Hence the *portal* for live speech recognition is not function. The only thing tha remains is resampling the audio to something Sphinx can decode.
