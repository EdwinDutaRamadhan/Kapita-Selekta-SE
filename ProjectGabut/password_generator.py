import random
subjek = ["1","2","3","4","5","6","7","8","9",
'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


def generatePassword(obj):
    randPassword = ""
    randLength = random.randint(16,32)
    
    for i in range(0, randLength):
        j = random.randint(0,60)
        # print(obj[j])
        randPassword += obj[j]
        i+=1
        print(obj[j])
        
    return randPassword

if __name__ == '__main__':
    print(generatePassword(subjek))
