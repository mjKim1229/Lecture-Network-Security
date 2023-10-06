from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# RSA 생성
keyPair = RSA.generate(2048)

# 개인 키를 바이트로 저장
priKeyPEM = keyPair.export_key(passphrase="1234", pkcs=8)

# 개인 키를 파일에 저장
with open('Alice_private.pem', 'wb') as output_file:
    output_file.write(priKeyPEM)

# 공개 키 생성
pubkey = keyPair.publickey()

# 공개 키를 바이트로 저장
pubKeyPEM = pubkey.export_key()

# 공개 키를 파일에 저장
with open('Alice_public.pem', 'wb') as output_file:
    output_file.write(pubKeyPEM)

# 암호화할 텍스트 데이터 읽기
with open('1.txt', 'r') as file:
    textData = file.read()

# 문자열을 바이트로 인코딩
textDataBytes = textData.encode('utf-8')

# 공개 키를 로드하여 암호화
with open('Alice_public.pem', 'rb') as file:
    pubkey_data = file.read()
    pubkey = RSA.import_key(pubkey_data)
    encryptor = PKCS1_OAEP.new(pubkey)
    encData = encryptor.encrypt(textDataBytes)

# 암호화된 데이터를 파일에 저장
with open('enc.txt', 'wb') as output_file:
    output_file.write(encData)

