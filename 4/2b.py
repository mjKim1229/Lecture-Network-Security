from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
import base64

# 공개키 읽기
with open('public.der', 'rb') as file:
    pubKeyData = file.read()
    pubKey = RSA.import_key(pubKeyData)

# 1.txt 읽기
with open('1.txt', 'rb') as file:
    textData = file.read()

# sig.txt 읽기
with open('sig.txt', 'rb') as file:
    sigText = file.read()

# Base64 디코딩
sigBytes = base64.b64decode(sigText)

#1.txt 값 hash 
h = SHA.new()
h.update(textData)

#공개키로 검증 객체 생성 
verifier = PKCS1_PSS.new(pubKey)

#1.txt에서 hash한 값과 
#sig.txt에서 읽은 1.txt를 전자서명한 값을 verify 
if verifier.verify(h, sigBytes):
    print("The signature is authentic.")
else:
    print("The signature is not authentic.")

