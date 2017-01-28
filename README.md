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

### Алгоритм превращения строки в транскрипцию
- "гласная буква Я, Ё, Ю, И, Е после согласных" заменяются на "Ь + гласный звук А, О, У, И, Э"
  - `"СгМгл" -> "СгЬТгл"`
  - `привет -> прьивьэт`
- "гласная буква Я, Ё, Ю, И, Е после пробелов, гласных, Ъ (кроме И) и Ь (включая И)" заменяются на "Й + гласный звук А, О, У, И, Э"
  - `ёж -> йож`
  - `вьюга -> вьйуга`
  - `подъезд -> подъйэзд`
- "согласная буква + Ъ"  заменяется на "символ твёрдого согласного звука (оригинал)"
  - `подъйэзд -> подйэзд`
- "согласная буква + Ь"  заменяется на "символ мягкого согласного звука (транслит)", если он есть, иначе на "символ твёрдого согласного звука (оригинал)"
  - `прьивьэт -> пrиvэт`
- удаляются все оставшиеся Ь и Ъ
