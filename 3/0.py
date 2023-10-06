from Crypto.Hash import SHA384
from bitstring import BitArray


i=0
while True:
        b= i.to_bytes(5, 'big')
        h=SHA384.new(b)
        hash=h.digest()

        c=BitArray( hash)
        print (hash[0:3], c.bin[:24])

        if hash[0:3] == bytes(3) :
                c=BitArray(hash)
                print ("found", i, c.bin[:8])
                break

        i+=1
