from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
import base64

# 공개키 읽기
with open('public.der', 'rb') as file:
    pubKeyData = file.read()
    pubKey = RSA.import_key(pubKeyData)

# 1.txt 읽기
with open('1.txt', 'r') as file:
    textData = file.read()

msg = textData.encode('utf-8')

# sig.txt 읽기
with open('sig.txt', 'rb') as file:
    sigText = file.read()

# Base64 디코딩
sigBytes = base64.b64decode(sigText)

h = SHA.new()
h.update(msg)

verifier = PKCS1_PSS.new(pubKey)

if verifier.verify(h, sigBytes):
    print("The signature is authentic.")
else:
    print("The signature is not authentic.")

