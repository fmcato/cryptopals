import crypto_pals
text = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
key = "ICE"

print(crypto_pals.xor_repeating_key(text, key).hex())
