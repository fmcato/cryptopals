from crypto_pals import score_ascii_text
from crypto_pals import xor_byte


message = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

scores = {}
for i in range(0, 256):
    decrypted = xor_byte(bytes.fromhex(message), i)
    score = score_ascii_text(decrypted)
    if score >= 0:
        scores[decrypted.decode('ascii')] = score

print(sorted(scores, key=scores.get, reverse=True)[0])
