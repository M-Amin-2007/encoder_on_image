"""to execute and see the programs result run this file with:
'python run.py'"""

from encoding import encode, decode

opperation = None
while opperation not in ("e", "d"):
    opperation = input(
        "if you want to encode press 'e' and if you want to decode press 'd': (e/d)"
    ).strip()

if opperation == "e":
    msg = input("write the message you want to encode: ")
    adress = input("paste the adress of the image that will have the message: ")
    print("\n", encode(msg, adress))
else:
    adress = input("paste the adress of the image you want to decode it: ")
    print(decode(adress))
