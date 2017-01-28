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

### Буквы (33):
- Гласные буквы (10): `а, у, о, ы, и, э, я, ю, ё, е`
- Согласные буквы (21): `б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ`
- `Ъ, Ь`

### Звуки (42):
- Гласные звуки (6): `а, о, у, и, ы, э`
- Согласные звуки (36): `б, б’, в, в’, г, г’, д, д’, ж, з, з’, й’, к, к’, л, л’, м, м’, н, н’, п, п’, р, р’, с, с’, т, т’, ф, ф’, х, х’, ц, ч’, ш, щ’`

#### Перекодированные звуки (42):
`А, Б, b, В, v, Г, g, Д, d, Ж, З, z, И, Й, К, k, Л, l, М, m, Н, n, О, П, p, Р, r, С, s, Т, t, У, Ф, f, Х, h, Ц, Ч, Ш, Щ, Ы, Э`

### Алгоритм превращения строки в транскрипцию
- "гласная буква Е, Ё, Ю, Я, И после согласных" -> "Ь + гласный звук Э, О, У, А, И"
  - `"СгМгл" -> "СгЬТгл"`
  - `привет -> прьивьэт`
- "гласная буква Е, Ё, Ю, Я после пробелов, гласных, Ъ и Ь" -> "Й + гласный звук Э, О, У, А"
  - `ёж -> йож`
  - `вьюга -> вьйуга`
  - `подъезд -> подъйэзд`
- "гласная буква И после Ь" -> "Й + гласный звук И"
  - `чьи -> чьйи`
- "гласная буква И после Ж, Ш, Ц" -> "гласный звук Ы"
  - `цирк -> цырк`
- "согласная буква + Ъ"  -> "согласный твёрдый звук (тот же символ)"
  - `подъйэзд -> подйэзд`
- "согласная буква + Ь"  -> "согласный мягкий звук (транслит)", если есть, иначе "согласный твёрдый звук (оригинал)"
  - `прьивьэт -> пrиvэт`
  - `тьишь -> tиш`
- удаляются все оставшиеся Ь и Ъ
