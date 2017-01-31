import glob
import os
import random
import re
import shelve
import time

from pydub import AudioSegment, silence, effects

SILENCE_THRESHOLD = -35  # -16 dB
SILENCE_LEN = 20  # 1000 ms
KEEP_SILENCE = 5  # 100 ms
alphabet = "А, Б, b, В, v, Г, g, Д, d, Ж, З, z, И, Й, К, k, Л, " \
           "l, М, m, Н, n, О, П, p, Р, r, С, s, Т, t, У, Ф, f, " \
           "Х, h, Ц, Ч, Ш, Щ, Ы, Э".split(", ")
alphabet.extend([" ", ".", ",", "-", "?", "!", "\n"])
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

db = shelve.open('db', writeback=True)

def initialize(user_id):
    db[user_id] = {}
    db[user_id]["sounds"] = {}

    for sound in alphabet:
        db[user_id]["sounds"][sound] = {}
    db[user_id]["sounds"]["-"][0] = AudioSegment.silent(duration=150)
    db[user_id]["sounds"][" "][0] = AudioSegment.silent(duration=250)
    db[user_id]["sounds"][","][0] = AudioSegment.silent(duration=320)
    db[user_id]["sounds"]["."][0] = AudioSegment.silent(duration=420)
    db[user_id]["sounds"]["?"][0] = AudioSegment.silent(duration=450)
    db[user_id]["sounds"]["!"][0] = AudioSegment.silent(duration=420)
    db[user_id]["sounds"]["\n"][0] = AudioSegment.silent(duration=420)

    os.chdir(user_id)
    for filename in glob.glob("*.ogg"):
        sound = filename[0]
        audio = AudioSegment.from_ogg(filename)
        index = len(db[user_id]["sounds"][sound])
        chunks = silence.split_on_silence(audio,
                                          min_silence_len=SILENCE_LEN,
                                          silence_thresh=SILENCE_THRESHOLD,
                                          keep_silence=KEEP_SILENCE)
        if chunks:
            save = max(chunks, key=lambda p: p.max_dBFS)
            # db[user_id]["sounds"][sound][index] = effects.normalize(save)
            db[user_id]["sounds"][sound][index] = save
        else:
            print(sound, "not saved")

    os.chdir("..")



def transcribe(input_string=""):
    string = input_string.upper()

    string = re.sub(r'ЬИ', r'ЬЙИ', string)
    string = re.sub(r'([ЖЦШ])И', r'\1Ы', string)
    string = re.sub(r'([БВГДЖЗКЛМНПРСТФХЦШ])([ЕЁЮЯИ])', repl=lambda p: p.group(1) + 'Ь' + replacement[p.group(2)],
                    string=string)
    string = re.sub(r'([ЙЧЩ])([ЕЁЮЯИ])', repl=lambda p: p.group(1) + replacement[p.group(2)], string=string)
    string = re.sub(r'([\sАОУЫЭЯЁЮИЕЪЬ])([ЕЁЮЯ])', repl=lambda p: p.group(1) + 'Й' + replacement[p.group(2)],
                    string=string)
    string = re.sub(r'([БВГДЖЗЙКЛМНПРСТФХЦЧШЩ])Ъ', r'\1', string)
    string = re.sub(r'([ЙЖЦЧШЩ])Ь', r'\1', string)
    string = re.sub(r'([БВГДЗКЛМНПРСТФХ])Ь', repl=lambda p: replacement[p.group(1)], string=string)
    string = re.sub(r'[ЬЪ]', r'', string)
    print(string)
    return string


def vocalize(user_id, string):
    audio = AudioSegment.silent(duration=250)
    transcribed_string = transcribe(" " + string)
    for sound in transcribed_string:
        audio += random.choice(list(db[user_id]["sounds"][sound].values())) if len(
            db[user_id]["sounds"][sound].values()) else AudioSegment.silent(duration=50)
    # audio = effects.normalize(audio)
    # audio = effects.compress_dynamic_range(audio)
    return audio


user_id = "gpchelkin"

time1 = time.clock()
if user_id in db:
    del db[user_id]
initialize(user_id)
string = open("string_test.txt").read()
if not os.path.exists("result"):
    os.mkdir("result")
print(string)
vocalize(user_id, string).export("result/" + string[:32] + ".ogg", format="ogg")
time2 = time.clock()
print(time2-time1)

db.close()