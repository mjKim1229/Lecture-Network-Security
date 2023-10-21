from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA
import base64

#키쌍 생성 
from Crypto.PublicKey import RSA
key=RSA.generate(2048)

#공개키 DER인코딩 후 저장 
pubKey=key.publickey()
pubKeyDER= pubKey.export_key( format="DER" )

with open('public.der', 'wb') as output_file:
    output_file.write(pubKeyDER)


# 1.txt 읽기
with open('1.txt', 'rb') as file:
    textData = file.read()

#서명 
h= SHA.new( )
h.update ( msg )

#비밀키 (개인키 + 공개키)로 전자 서명 
#a만 알 수 있음 
#1과 다르게 굳이 개인키 저장 후 읽지 않음 
signer=PKCS1_PSS.new ( key )
sig=signer.sign ( h )
encodeSign = base64.b64encode(sig) 

with open('sig.txt', 'wb') as output_file:
    output_file.write(encodeSign)



