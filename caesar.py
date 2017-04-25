Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Caesar cipher and decipher
def caesar(plainText, shift): 
        cipherText = ""
        for ch in plainText:
                ch = ch.lower()
                if ch == ' ':
                    cipherText += ' '
                if ch.isalpha():
                        stayInAlphabet = ord(ch) + shift 
                        if stayInAlphabet > ord('z'):
                                stayInAlphabet -= 26
                        finalLetter = chr(stayInAlphabet)
                        cipherText += finalLetter
        print "Shift:", shift, cipherText
        return cipherText

def decaesar(plainText, shift): 
        cipherText = ""
        for ch in plainText:
                ch = ch.lower()
                if ch == ' ':
                    cipherText += ' '
                if ch.isalpha():
                        stayInAlphabet = ord(ch) - shift
                        print stayInAlphabet
                        if stayInAlphabet < ord('a'):
                                diff = stayInAlphabet + shift - ord('a')
                                stayInAlphabet = diff + ord('a') + 26 - shift 
                        if stayInAlphabet > ord('z'):
                                stayInAlphabet -= 26                   
                        finalLetter = chr(stayInAlphabet)
                        cipherText += finalLetter
        print "Shift:", shift, cipherText
        return cipherText
