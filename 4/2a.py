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
with open('1.txt', 'r') as file:
    textData = file.read()

msg = textData.encode('utf-8')

#서명 
h= SHA.new( )
h.update ( msg )

signer=PKCS1_PSS.new ( key )
sig=signer.sign ( h )
encodeSign = base64.b64encode(sig) 

with open('sig.txt', 'wb') as output_file:
    output_file.write(encodeSign)


#print(encodeSign) 

