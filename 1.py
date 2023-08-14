from googletrans import Translator
from pro import dzen
t = Translator()
r = t.translate(dzen, dest='ru')
print(t)

