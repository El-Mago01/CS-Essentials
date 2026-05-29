import string

def encrypt_it(char_nr: int, char_range:tuple, key:int):
      while abs(key) > (char_range[1] - char_range[0]):
          if key < 0:
              key += char_range[1] - char_range[0]
          else:
              key -= char_range[1] - char_range[0]
      new_char = char_nr + key
      try:
          if new_char > char_range[1]:
              new_char = char_range[0] + (new_char - char_range[1]) - 1
          elif new_char < char_range[0]:
              new_char = char_range[1] - (char_range[0] - new_char) + 1
          chr(new_char)
      except ValueError:
          print(char_nr, char_range, key)
          new_char = 35
      return chr(new_char)


def encrypt_char(char :str, key:int):
    a_z_range = (97, 122)
    A_Z_range = (65, 90)
    char_nr = ord(char)
    if char in string.punctuation or char == " ":
        return char

    if char.isupper():
        return encrypt_it(char_nr, A_Z_range, key)
    else:
        return encrypt_it(char_nr, a_z_range, key)


def encrypt_caesar(text:str, key:int):
    encrypted_text = ''
    for text_index in range(0, len(text)):
        # print(text_index, text[text_index], "key:", key )
        encrypted_text += encrypt_char(text[text_index], key)
    # print(encrypted_text)
    return encrypted_text


def decrypt_caesar(ciphertext, key):
    return encrypt_caesar(ciphertext, -key)

def main():
    to_encrypt_list = ['aa', 'aazz', 'AZCX', "IwonISawiZox!", "Veni; Vidi; Vici"]
    key = -2
    for to_encrypt in to_encrypt_list:
        print("===========================================")
        crypted = encrypt_caesar(to_encrypt, key)
        print(f"The text to encrypt : {to_encrypt}")
        print(f"The encrypted text : {crypted}")
        print("Decrypting the text back: ",end='')
        decrypted = decrypt_caesar(crypted, key)
        print(decrypted)


if __name__ == "__main__":
    main()
