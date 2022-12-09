# Chatbot for AI Project at SPGS

This repository contains a ChatBot that is part of a CS project class
at [SPGS](https://spgs.org/). The ChatBot is supposed to be a simple
demo for students to interact and play with.

### Installation

- (Optional) Install Ubuntu dependencies:

```
sudo apt install mpg123
sudo apt install portaudio19-dev
```

then comment out the following lines (127-143) to avoid error messages
in `/usr/share/alsa/alsa.conf`:

```
#pcm.front cards.pcm.front
#pcm.rear cards.pcm.rear
#pcm.center_lfe cards.pcm.center_lfe
#pcm.side cards.pcm.side
#pcm.surround21 cards.pcm.surround21
#pcm.surround40 cards.pcm.surround40
#pcm.surround41 cards.pcm.surround41
#pcm.surround50 cards.pcm.surround50
#pcm.surround51 cards.pcm.surround51
#pcm.surround71 cards.pcm.surround71
#pcm.iec958 cards.pcm.iec958
#pcm.spdif iec958
#pcm.hdmi cards.pcm.hdmi
#pcm.dmix cards.pcm.dmix
#pcm.dsnoop cards.pcm.dsnoop
#pcm.modem cards.pcm.modem
#pcm.phoneline cards.pcm.phoneline
```

- Install dependencies:

```
pip install numpy gTTS pyaudio SpeechRecognition
pip install torch torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```
