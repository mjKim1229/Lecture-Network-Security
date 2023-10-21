from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

#RSA 키쌍 생성
keyPair = RSA.generate (2048)

#개인키 저장 
#Key => Byte 암호화  
#개인키이기 때문에, 비밀번호로 암호화 => 비밀번호를 알고 있는 사람만 사용 가능 
priKeyPEM= keyPair.export_key (passphrase="1234")

with open('Alice_private.pem', 'wb') as output_file:
    output_file.write(priKeyPEM)


#공개키 분리 
pubkey = keyPair.publickey( ) 

#공개키 저장 
#Key => Byte 
#공개키이기 때문에, 비밀번호로 암호화 하지 않음 => 누구나 사용 가능 
pubKeyPEM=pubkey.export_key()

with open('Alice_public.pem', 'wb') as output_file:
    output_file.write(pubKeyPEM)

