def decrypt_message(encrypted_message) -> str:
    # Instruction that´s used to get a Unicode char from an ASCII value of a character: chr(97)
    decrypted_message = ""
    
    ascii_code_min = 32
    ascii_code_max = 128
    ascii_character = ""
    
    for character in encrypted_message:

        if(character == ' '):
            decrypted_message = decrypted_message + " "
            continue

        ascii_character = ascii_character + character
        ascii_character_as_number = int(ascii_character)
        if (ascii_character_as_number < ascii_code_min):
            continue

        if (ascii_character_as_number > ascii_code_max):
            raise ValueError('Caracter que no deberías mandaros Midu')

        decrypted_message = decrypted_message + chr(ascii_character_as_number)
        ascii_character = ""

    return decrypted_message

if __name__ == "__main__":
    # encrypted_text = "11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101"
    # decrypted_text = decrypt_message(encrypted_text)
    # print(f"{decrypted_text}")

    text1 = decrypt_message("73 107110111119 121111117 121111117 100111 110111116")
    text2 = decrypt_message("107110111119 109101 73 97109 1199711699104105110103")
    text3 = decrypt_message("121111117 73 97109 102111108108111119105110103 121111117")
    text4 = decrypt_message("68111 121111117 11997110116 116111 11210897121 8010897121")
    text5 = decrypt_message("119105116104 109101 79107 7610111639115 11210897121")
    text6 = decrypt_message("82117110 116104105115 9911110910997110100 11511798109105116")
    text7 = decrypt_message("116561181061045651505752561029911097108")

    print(text1)
    print(text2)
    print(text3)
    print(text4)
    print(text5)
    print(text6)
    print(text7)