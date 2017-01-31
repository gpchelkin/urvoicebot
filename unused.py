# iterate over chunks until you find the first one with sound
# def detect_leading_silence(sound):
#     trim_ms = 0
#     while sound[trim_ms:trim_ms + SILENCE_LEN].dBFS < SILENCE_THRESHOLD:
#         trim_ms += SILENCE_LEN
#     return trim_ms

# start_trim = detect_leading_silence(audio)
# end_trim = len(audio) - detect_leading_silence(audio.reverse())
# letters[letter] = audio[start_trim:end_trim]

# nonsilent_ranges = silence.detect_nonsilent(audio, min_silence_len=SILENCE_LEN, silence_thresh=SILENCE_THRESHOLD)
# audio_range = max(nonsilent_ranges, key=lambda p: p[1]-p[0])
# letters[letter] = audio[audio_range[0]-50:audio_range[1]+50]



# db[user_id]["sounds"][sound][index] = effects.strip_silence(audio,
#                       silence_len=SILENCE_LEN,
#                       silence_thresh=SILENCE_THRESHOLD,
#                       padding=KEEP_SILENCE)


from pydub import AudioSegment
alphabet = "А, Б, b, В, v, Г, g, Д, d, Ж, З, z, И, Й, К, k, Л, " \
           "l, М, m, Н, n, О, П, p, Р, r, С, s, Т, t, У, Ф, f, " \
           "Х, h, Ц, Ч, Ш, Щ, Ы, Э".split(", ")
for sound in alphabet:
    AudioSegment.silent(duration=50).export("gpchelkin2/"+sound+".ogg", format="ogg")
