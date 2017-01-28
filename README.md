# urvoicebot
Text-to-Speech with your own voice.

- [pydub](https://github.com/jiaaro/pydub) для работы с аудио, умеет ogg (формат голосовых сообщений Telegram)
- [API](https://github.com/jiaaro/pydub/blob/master/API.markdown)
- [pydub.silence](https://github.com/jiaaro/pydub/blob/master/pydub/silence.py)

## Выбираем, наверное, первый
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [telepot](https://github.com/nickoala/telepot)
- [aiotg](https://github.com/szastupov/aiotg)

## Bot API
- https://core.telegram.org/bots/api
- https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter7.html

## Фонетика
- http://tutrus.com/fonetika/zvuki-i-bukvy
- http://tutrus.com/fonetika/foneticheskaya-shpargalka

### Алгоритм
- гласные буквы "е, ё, ю, я" после согласных заменяются на "Ь + гласный звук (а, о, у, и, ы, э)"
  - `"СгМгл" -> "СгЬТгл"`
  - `привет -> прьивьэт`
- гласные буквы "е, ё, ю, я" после пробелов, гласных, Ь и Ъ заменяются на "Й + гласный звук (а, о, у, и, ы, э)"
  - `ёж -> йож`
  - `вьюга -> вьйуга`
  - `подъезд -> подъйэзд`
- "согласная буква + Ъ"  заменяется на "символ мягкого согласного звука (оригинал)"
  - `подъйэзд -> подйэзд`
- "согласная буква + Ь"  заменяется на "символ мягкого согласного звука (транслит)"
  - `прьивьэт -> пrиvэт`
