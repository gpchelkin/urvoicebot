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
- "Ъ" заменяется на пробел
  - `"Ъ" -> "_"`
  - `подъезд -> под_езд`
- мягкие гласные после согласных заменяются на "Ь + твердый гласный"
  - `"СгМгл" -> "СгЬТгл"`
  - `привет -> прьивьэт`
- мягкие гласные после пробелов и после Ь заменяются на "Й + твердый гласный"
  - `ёж -> йож`
  - `вьюга -> вьйуга`
  - `под_езд -> под_йэзд`
- все сочетания "согласный + Ь"  заменяются на символы мягкого согласного
  - `прьивьэт -> пrиvэт`
