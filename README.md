# urvoicebot
Text-to-Speech with your own voice.

- [pydub](https://github.com/jiaaro/pydub) для работы с аудио, умеет ogg (формат голосовых сообщений Telegram)
- [API](https://github.com/jiaaro/pydub/blob/master/API.markdown)
- [pydub.silence](https://github.com/jiaaro/pydub/blob/master/pydub/silence.py)

## Telegram Bot API Libraries
- [_pyTelegramBotAPI_](https://github.com/eternnoir/pyTelegramBotAPI)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [telepot](https://github.com/nickoala/telepot)
- [aiotg](https://github.com/szastupov/aiotg)

### Bot API
- https://core.telegram.org/bots/api
- https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter7.html

## Фонетика
- http://tutrus.com/fonetika/zvuki-i-bukvy
- http://tutrus.com/fonetika/foneticheskaya-shpargalka

### 33 буквы:
- 10 гласных букв: `а, у, о, ы, и, э, я, ю, ё, е`
- 21 согласная буквы: `б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ`
- `Ъ, Ь`

### 42 звука:
- 6 гласных звуков: `а, о, у, и, ы, э`
- 36 согласных звуков: `б, б’, в, в’, г, г’, д, д’, ж, з, з’, й’, к, к’, л, л’, м, м’, н, н’, п, п’, р, р’, с, с’, т, т’, ф, ф’, х, х’, ц, ч’, ш, щ’`

### Алгоритм превращения строки в транскрипцию
- "гласная буква Я, Ё, Ю, И, Е после согласных" -> "Ь + гласный звук А, О, У, И, Э"
  - `"СгМгл" -> "СгЬТгл"`
  - `привет -> прьивьэт`
- "гласная буква Я, Ё, Ю, И, Е после пробелов, гласных, Ъ и Ь" -> "Й + гласный звук А, О, У, И, Э"
  - `ёж -> йож`
  - `вьюга -> вьйуга`
  - `подъезд -> подъйэзд`
- "гласная буква И после Ь" -> "Й + гласный звук И"
  - `чьи -> чьйи`
- "гласная буква И после Ж, Ш, Ц" -> "гласный звук Ы"
  - `цирк -> цырк`
- "согласная буква + Ъ"  -> "согласный твёрдый звук (оригинал)"
  - `подъйэзд -> подйэзд`
- "согласная буква + Ь"  -> "согласный мягкий звук (транслит)", если есть, иначе "согласный твёрдый звук (оригинал)"
  - `прьивьэт -> пrиvэт`
  - `тьишь -> tиш`
- удаляются все оставшиеся Ь и Ъ
