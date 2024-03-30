def encryption(message,shift):
    result=" "
    for i in range(len(message)):
        char=message[i]
        if char==" ":
            result+=" "
        elif(char.isupper()):
            result+=chr((ord(char)+shift-65)%26+65)
        elif(char.islower()):
            result+=chr((ord(char)+shift-97)%26+97)
    return result
def decrypt(message,shift):
    return encryption(message, -shift)
message=input("Enter message to encrypt:")
shift=int(input("Entern Shift Value:"))

enc_msg=encryption(message,shift)
dec_msg=decrypt(enc_msg,shift)
print("encrypted text =",enc_msg)
print("Decrypted text =",dec_msg)