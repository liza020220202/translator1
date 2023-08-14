from googletrans import Translator
from pro import dzen
t = Translator()
print(t.translate(dzen, dest='ru').text)


