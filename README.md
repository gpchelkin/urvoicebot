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

## Фонетика
http://tutrus.com/fonetika/zvuki-i-bukvy
http://tutrus.com/fonetika/foneticheskaya-shpargalka

- "Ь перед гласным" заменяется на пробел
- "Ъ" заменяется на пробел
- мягкие гласные после согласных заменяются на "Ь + твердый гласный"
- `привет -> прьивьэт`
- мягкие двузвучные гласные после пробелов и после Ь и Ъ заменяются на "Й + твердый гласный"
- `ёж -> йож`
- `вьюга -> вьйуга`
- все сочетания "согласный + Ь"  заменяются на символы мягкого согласного
- `прьивьэт -> пrиvэт`
