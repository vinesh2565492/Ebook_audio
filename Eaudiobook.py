from gtts import gTTS
file=open("C:\\Users\\hp\\Desktop\\vinesh.txt", mode="r")
text=file.read()
language="en"
speech=gTTS(text=text, lang=language, slow=False)
speech.save("audio.mp3")

