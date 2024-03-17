words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def typed():
    if type == "encode":
        ciphertext = ""
        for i in msg:
            pos = words.index(i)
            n_pos = pos+shift
            n_let = words[n_pos]
            ciphertext += n_let
        print(ciphertext)
    elif type == "decode":
        ciphertext = ""
        for i in msg:
            pos = words.index(i)
            n_pos = pos-shift
            n_let = words[n_pos]
            ciphertext += n_let
        print(ciphertext)


is_True = True
while is_True:
    type = input("Encode or decode")
    msg = input()
    shift = int(input())
    typed()
    result = input("yes or no")
    if result == "no":
        is_True = False

