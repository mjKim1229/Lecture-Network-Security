from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#RSA 생성
keyPair = RSA.generate (2048)

#개인키 
priKeyPEM= keyPair.export_key (passphrase="1234")
#print(priKeyPEM)

with open('Alice_private.pem', 'wb') as output_file:
    output_file.write(priKeyPEM)


#공개키 생성
pubkey = keyPair.publickey( ) 
pubKeyPEM=pubkey.export_key()
#print(pubKeyPEM)

with open('Alice_public.pem', 'wb') as output_file:
    output_file.write(pubKeyPEM)

