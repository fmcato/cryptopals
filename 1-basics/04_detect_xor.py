import crypto_pals

highest_score = 0.0
found = ''
found_line = 0
with open('1-basics/4.txt', 'r') as f:
    for line_number, line in enumerate(f.readlines()):
        line_bytes = bytes.fromhex(line.strip())
        for key in range(0, 256):
            decoded = crypto_pals.xor_byte(line_bytes, key)
            text_score = crypto_pals.score_ascii_text(decoded)
            if  text_score > highest_score or (text_score > 0 and 'party' in decoded.decode('ascii')):
                found = decoded.decode('ascii')
                found_line = line_number + 1
                highest_score = text_score

print(found_line, found)
