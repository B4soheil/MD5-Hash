print("""
|  _ \ / _ \| | | |_   _| ____|  _ \     / ___| / ___|
| |_) | | | | | | | | | |  _| | |_) |    \___ \| |    
|  _ <| |_| | |_| | | | | |___|  _ <      ___) | |___ 
|_| \_\___/ \___/  |_| |_____|_| \_\     |____/ \____|
.
.
.
.
.

""")
import hashlib

in_hash = input("Enter Your HASH MD5 : ")

wordlist = input("Enter Your File Name : ")

in_file = open(wordlist)

for word in in_file:
    encword = word.encode("uft-8")
    md5test = hashlib.md5(encword.strip()).hexdigest()

    if md5test == in_hash:
        print("Password found is " + word)
        break

