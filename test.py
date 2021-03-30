import sys
import random as ra

class Crypt:
    def __init__(self, key):
        self.key=key
    def encrypt(self, msg):
        keylist= list(self.key)
        msglist=list(msg)
        keyLen =len(keylist)
        msgLen = len(msglist)
        cipherText = ['']*msgLen
        for i in range(msgLen):
            cipherText[i]=chr(ord(msglist[i]) ^ ord(keylist[i % keyLen]))
            return''.join(cipherText)
    def decrypt(self, msg):
        keyList=list(self.key)
        msgList=list(msg)
        keyLen=len(keyList)
        msglen=len(msgList)
        cipherText = ['']*msglen
        for i in range(msglen):
            cipherText[i]=chr(ord(msgList[i]) ^ ord(keyList[i % keyLen]))
            return''.join(cipherText)
if __name__ == "__miain__":
    print(sys.argv)
    if len(sys.argv) > 2:
        if sys.argv[1] =='-e':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3])) 
        elif sys.argv[1] =='-d':
            c = Crypt(sys.argv[2])
            print(c.encrypt(sys.argv[3])) 
    