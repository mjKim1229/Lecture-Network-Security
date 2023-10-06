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


keyPair= RSA.importKey(privateKey, passphrase=passPhrase )

#복호화 
decryptor = PKCS1_OAEP.new( keyPair )
decrypted = decryptor.decrypt(encTextData)
print(decrypted)
