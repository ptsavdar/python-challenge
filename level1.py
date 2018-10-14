def shift_letters_in_str(base, base_enc, msg):
    trantab = str.maketrans(base, base_enc)

    print(msg.translate(trantab))

shift_letters_in_str("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab", "map")
