from gtts import gTTS
import os
mytext = 'Ashish is from Berhampur'
language = 'en'
myObj = gTTS(text=mytext, lang=language, slow=False)
myObj.save('welcomes.mp3')
os.system("mpg321 ashish.mp3")