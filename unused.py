# https://stackoverflow.com/a/29550200/2490759
# iterate over chunks until you find the first one with sound
def detect_leading_silence(sound):
    trim_ms = 0
    assert chunk_size > 0  # to avoid infinite loop
    while sound[trim_ms:trim_ms + SILENCE_LENGTH].dBFS < SILENCE_THRESHOLD and trim_ms < len(sound):
        trim_ms += SILENCE_LENGTH
    return trim_ms


start_trim = detect_leading_silence(audio)
end_trim = len(audio) - detect_leading_silence(audio.reverse())
trimmed_sound = audio[start_trim:end_trim]

###################3

nonsilent_ranges = silence.detect_nonsilent(audio, min_silence_len=SILENCE_LEN, silence_thresh=SILENCE_THRESHOLD)
audio_range = max(nonsilent_ranges, key=lambda p: p[1]-p[0])
letters[letter] = audio[audio_range[0]-50:audio_range[1]+50]
