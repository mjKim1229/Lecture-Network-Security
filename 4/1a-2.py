from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
#passphrase 입력받기
passPhrase = input("passphrase를 입력하세요:")


#개인키 읽기
with open('Alice_private.pem', 'rb') as file:
    privateKey = file.read()

#enc.txt읽기
with open('enc.txt', 'rb') as file:
    encTextData = file.read()

#개인키이기 때문에, passphrase를 알고 있는 a만 사용 가능하다. 
#개인키 생성 
keyPair= RSA.importKey(privateKey, passphrase=passPhrase )

#개인키로 복호화 
decryptor = PKCS1_OAEP.new( keyPair )
decrypted = decryptor.decrypt(encTextData)
print(decrypted)
