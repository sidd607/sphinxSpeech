# sphinxSpeech
This project is a demo for using CMU Sphinx for live speech recognition in python and WebSpeech API of HTML5

The project contains two main file - liveRecognition.py and app.py

***
## live Speech Recognition using sphinx
sphinx is an open source speech recognition library written in Java and developed at Carnegie Mellon University. It uses hidden markov models for modelling speech. To run the demo, download the speech models from [English models](https://drive.google.com/folderview?id=0Bw00am7cLinWNWE4RnZuZkw5ODA&usp=sharing) and place the folder "pocketSphinx" and run the python script

```
$ python liveRecognition.py
```
once the script starts running yoc now start talking into the mic as long as you want and sphinx will convert your speech to text in real time.
for more details regarding Sphinx its installation visit [Sphinx](http://cmusphinx.sourceforge.net/)
***
## Speech Recognition using webSpeech API
Google has introduced its webSpeech API for speechk Recognition as part of HTML5 and is currently free to use. To Try out the the webSpeech demo run the flask server using
```
$ python app.py
```
Once the server is up and running you can try it out at */webSpeech*

## Portal for live speech recognition from browser using CMU Sphinx
I have tried to implement a portal like Google Now for speech recognition using HTML5 and CMU Sphinx at the backend. My approach was as follows.
