import sys
mode = None

def usage():
    print('python3 sypher.py [sypher|decypher] key message')

if (len(sys.argv) =! 3):
    usage()
    sys.exit(0)

if (sys.argv[1] == "cypher"):
    key = int(sys.argv[2]) %26
elif (sys.argv[1] == "decypher"):
    key = -(int(sys.argv[2]) %26)
else:
    print(f"commande non supportée: {sys.argv[1]}")
    usage()
    sys.exit(0)

response = ''
for current_character in sys.argv[3]:
    dec = ord(current_character) + key
    if (dec > ord('z')):
        dec -= 26
    elif (dec < ord('a')):
        dec += 26
    response += chr(dec)

print(response)




















key = sys.argv[2]
msg = sys.argv[3]

def cypher(msg,key):
    res=""
    for lettre in msg:
        res+= chr((ord(lettre)+key))
    print(res)

def decypher(msg,key):
    res=""
    for lettre in msg:
        res+= chr((ord(lettre)-key))
    print(res)


if(sys.argv[1] == "cypher"):
    print(cypher(res))
elif(sys.argv[1] == "decypher"):
    print(decypher(res))
else:
    print(f"commande non supportée: {sys.argv[1]}")
    sys.exit(0)