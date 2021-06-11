# Usage: python3 vocalize.py gpchelkin phrase.txt result2

import glob
import os
import sys
import random
import re
import shelve
import time

from pydub import AudioSegment, silence, effects

SILENCE_THRESHOLD = -35  # -16 dB
SILENCE_LENGTH = 20  # 1000 ms
KEEP_SILENCE = 5  # 100 ms
alphabet = "АБbВvГgДdЖЗzИЙКkЛlМmНnОПpРrСsТtУФfХhЦЧШЩЫЭ"
alphabet_extra = [" ", ".", ",", "-", "?", "!", "\n"]
replacement = {
    "Е": "Э",
    "Ё": "О",
    "Ю": "У",
    "Я": "А",
    "И": "И",
    "Б": "b",
    "В": "v",
    "Г": "g",
    "Д": "d",
    "З": "z",
    "К": "k",
    "Л": "l",
    "М": "m",
    "Н": "n",
    "П": "p",
    "Р": "r",
    "С": "s",
    "Т": "t",
    "Ф": "f",
    "Х": "h"
}


def initialize_user(db, user_id):
    db[user_id] = {}
    db[user_id]["sounds"] = {}

    db[user_id]["sounds"]["-"] = [AudioSegment.silent(duration=150)]
    db[user_id]["sounds"][" "] = [AudioSegment.silent(duration=250)]
    db[user_id]["sounds"][","] = [AudioSegment.silent(duration=320)]
    db[user_id]["sounds"]["."] = [AudioSegment.silent(duration=420)]
    db[user_id]["sounds"]["?"] = [AudioSegment.silent(duration=450)]
    db[user_id]["sounds"]["!"] = [AudioSegment.silent(duration=420)]
    db[user_id]["sounds"]["\n"] = [AudioSegment.silent(duration=420)]
    for sound in alphabet:
        db[user_id]["sounds"][sound] = []

    for filename in glob.glob("{dir}/*.ogg".format(dir=user_id)):
        # Get one sound: "user/У*.ogg" -> "У"
        sound = os.path.splitext(os.path.basename(filename))[0][0]
        audio = AudioSegment.from_ogg(filename)
        # saved = effects.strip_silence(audio,
        #                               silence_len=SILENCE_LEN,
        #                               silence_thresh=SILENCE_THRESHOLD,
        #                               padding=KEEP_SILENCE)
        chunks = silence.split_on_silence(audio,
                                          min_silence_len=SILENCE_LENGTH,
                                          silence_thresh=SILENCE_THRESHOLD,
                                          keep_silence=KEEP_SILENCE)
        if chunks:
            saved = max(chunks, key=lambda p: p.max_dBFS)
            # db[user_id]["sounds"][sound].append(effects.normalize(saved))
            db[user_id]["sounds"][sound].append(saved)
            db.sync()
            print(sound, "saved")
        else:
            print(sound, "not saved")


def transcribe(string=""):
    print(f'### String:\n{string}\n')

    string = string.upper()
    string = re.sub(r'ЬИ', r'ЬЙИ', string)
    string = re.sub(r'([ЖЦШ])И', r'\1Ы', string)
    string = re.sub(r'([БВГДЖЗКЛМНПРСТФХЦШ])([ЕЁЮЯИ])', repl=lambda p: p.group(1) + 'Ь' + replacement[p.group(2)],  string=string)
    string = re.sub(r'([ЙЧЩ])([ЕЁЮЯИ])',                repl=lambda p: p.group(1) + replacement[p.group(2)],        string=string)
    string = re.sub(r'([\sАОУЫЭЯЁЮИЕЪЬ])([ЕЁЮЯ])',      repl=lambda p: p.group(1) + 'Й' + replacement[p.group(2)],  string=string)
    string = re.sub(r'([БВГДЖЗЙКЛМНПРСТФХЦЧШЩ])Ъ', r'\1', string)
    string = re.sub(r'([ЙЖЦЧШЩ])Ь', r'\1', string)
    string = re.sub(r'([БВГДЗКЛМНПРСТФХ])Ь',            repl=lambda p: replacement[p.group(1)],                     string=string)
    string = re.sub(r'[ЬЪ]', r'', string)

    print(f'### Transcribed to:\n{string}\n')

    return string


def vocalize(db, user_id, string):
    audio = AudioSegment.silent(duration=500)
    transcribed_string = transcribe(string)
    for sound in transcribed_string:
        if sound in db[user_id]["sounds"] and len(db[user_id]["sounds"][sound]):
            audio += random.choice(db[user_id]["sounds"][sound])
        else:
            audio += AudioSegment.silent(duration=50)
    # audio = effects.normalize(audio)
    # audio = effects.compress_dynamic_range(audio)
    return audio


def main():
    user_id = sys.argv[1]
    phrase_arg = sys.argv[2]
    output_dir = sys.argv[3]

    time_start = time.time()

    db = shelve.open('db', writeback=True)
    if user_id not in db:
        initialize_user(db, user_id)
        print("Time: ", time.time() - time_start)
        time_start = time.time()

    if os.path.exists(phrase_arg):
        with open(phrase_arg) as f:
            phrase = f.read().strip()
    else:
        phrase = phrase_arg.strip()
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    vocalized = vocalize(db, user_id, phrase)
    vocalized.export(os.path.join(output_dir, phrase[:32] + ".ogg"), format="ogg")
    db.close()

    print("Time: ", time.time()-time_start)


if __name__ == '__main__':
    main()
