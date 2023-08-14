from googletrans import Translator
from pro import dzen
t = Translator()
result = t.translate(dzen, dest='ru').text
print(result)


