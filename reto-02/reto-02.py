def decrypt_message(encrypted_message) -> str:
    # Instruction that´s used to get a Unicode char from an ASCII value of a character: chr(97)
    decrypted_message = ""
    
    ascii_code_a = 97
    ascii_code_z = 122
    ascii_character = ""
    
    for character in encrypted_message:

        if(character == ' '):
            decrypted_message = decrypted_message + " "
            continue

        ascii_character = ascii_character + character
        ascii_character_as_number = int(ascii_character)
        if (ascii_character_as_number < ascii_code_a):
            continue

        if (ascii_character_as_number > ascii_code_z):
            raise ValueError('Caracter que no deberías mandaros Midu')

        decrypted_message = decrypted_message + chr(ascii_character_as_number)
        ascii_character = ""

    return decrypted_message

if __name__ == "__main__":
    encrypted_text = "11610497110107115 102111114 11210897121105110103 9911110010110998101114 11210810197115101 11510497114101"
    decrypted_text = decrypt_message(encrypted_text)

    print(f"{decrypted_text}")