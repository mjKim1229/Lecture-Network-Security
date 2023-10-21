from Crypto.Hash import HMAC

# 사용자로부터 키 입력 받기
key = input("키를 입력하세요: ").encode()

# 1.txt 파일 읽기
with open('1.txt', 'rb') as file:
    message = file.read()
    print("1.txt에서 읽은 값",message)

# HMAC 생성
h = HMAC.new(key)
h.update(message)
mac = h.digest()

# HMAC 값을 출력
print("생성된 HMAC:", mac)

# 1.txt 파일에 HMAC을 붙여서 H.txt로 저장
with open('H.txt', 'wb') as output_file:
    output_file.write(message + mac)

