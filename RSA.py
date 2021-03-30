import sys
import random as rand
class RSA :
    def __init__(self):
        print("Hello")
    def encrypt(self,msg):
        print("Encrypt")
    def decrypt(self,msg):
        print("Encrypt")
    def isPrime(number):
        for i in range(2,number):
            if number % i ==0:
                return False
        return True
    def genRandomList(self):
        data=[]
        while len<6:
            y=rand.randint(1024,65536)
            if isPrime(y):
                data.append(y)
                return data
if __name__=='__main__':
    rsa=RSA()
    rsa.encrypt()
