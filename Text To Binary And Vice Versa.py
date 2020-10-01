import binascii, sys, time

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def to_exit():
    sys.exit("*"*60+"\nThanks For Using\n"+"*"*60+"")

print('\n',"*"*60,'\n'" [0]  Text To Binary"'\n'" [1]  Binary To Text"'\n'" [99] Exit "'\n',"*"*60)

option_input = input("Enter Your Choice : ")

if option_input == '0':
    input_for_binary = input("Enter Your Text Input : ")
    print("*"*60,'\n'"Text   : ",input_for_binary,'\n'"Binary : ",text_to_bits(input_for_binary)) 
    to_exit()
    time.sleep(10)
     
elif option_input == '1':
    input_for_text = input("Enter Your Binary Input : ")
    print("*"*60,'\n'"Binary   : ",input_for_text,'\n'"Text     : ",text_from_bits(input_for_text))
    to_exit()
    
elif option_input == '99':
    sys.exit("Bye")

else:
    print("*"*60 + "Invalid Input" + "*"*60)
    
time.sleep(1000000000000000000000000000000000000000000000000000)