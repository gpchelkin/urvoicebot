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
- Гласные буквы (10): `А, У, О, Ы, И, Э, Я, Ю, Ё, Е`
- Согласные буквы (21): `Б, В, Г, Д, Ж, З, Й, К, Л, М, Н, П, Р, С, Т, Ф, Х, Ц, Ч, Ш, Щ`
- `Ъ, Ь`

### Звуки (42):
- Гласные звуки (6): `А, О, У, И, Ы, Э`
- Согласные звуки (36): `Б, Б’, В, В’, Г, Г’, Д, Д’, Ж, З, З’, Й’, К, К’, Л, Л’, М, М’, Н, Н’, П, П’, Р, Р’, С, С’, Т, Т’, Ф, Ф’, Х, Х’, Ц, Ч’, Ш, Щ’`

#### Перекодированные звуки (42):
`А, Б, b, В, v, Г, g, Д, d, Ж, З, z, И, Й, К, k, Л, l, М, m, Н, n, О, П, p, Р, r, С, s, Т, t, У, Ф, f, Х, h, Ц, Ч, Ш, Щ, Ы, Э`

### Алгоритм превращения строки в транскрипцию
1. "Ь + И" -> "Ь + Й + И"
  - `чьи -> чьйи`
- "Ж, Ц, Ш (всегда твердые) + И" -> "Ж, Ц, Ш + Ы"
  - `цирк -> цырк`
- "согласная кроме Й, Ч, Щ (кроме всегда мягких) + Е, Ё, Ю, Я, И" -> "согласная + Ь + Э, О, У, А, И"
  - `привет -> прьивьэт`
- "пробел, гласная, Ъ, Ь + Е, Ё, Ю, Я" -> "пробел, гласная, Ъ, Ь + Й + Э, О, У, А"
  - `ёж -> йож`
  - `вьюга -> вьйуга`
  - `подъезд -> подъйэзд`
- "согласная + Ъ"  -> "согласный (тот же символ)"
  - `подъйэзд -> подйэзд`
- "Й, Ж, Ц, Ч, Ш, Щ (всегда твердые и всегда мягкие) + Ь"  -> "Й, Ж, Ц, Ч, Ш, Щ (тот же символ)"
  - `тьишь -> tиш`
  - `чьйи -> чйи`
- "согласная кроме Й, Ж, Ц, Ч, Ш, Щ (всегда твердых и всегда мягких) + Ь"  -> "согласный мягкий (транслит)"
  - `прьивьэт -> пrиvэт`
- удалить все оставшиеся "Ь, Ъ"
