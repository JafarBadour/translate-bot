from googletrans import Translator
translator = Translator()
s = translator.translate('Mein kein',dest='ar' )
print(translator.detect('لله اكبر'))
print(s)
