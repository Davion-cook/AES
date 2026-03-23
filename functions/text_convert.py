def text_to_bytes(text):
    # AES needs exactly 16 characters (16 bytes)
    if len(text) != 16:
        raise ValueError("Message must be exactly 16 characters")
    
    # create an arry to store characters from string
    byte_list = []

    # Convert each character to its UTF-8 value
    for char in text:
        ascii_value = ord(char)
        byte_list.append(ascii_value)

    return byte_list


def bytes_to_text(byte_list):
    # Convert each UTF-8 value back to its character
    text = ""
    for byte in byte_list:
        text += chr(byte)
    return text
