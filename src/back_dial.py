import os, sys, re, struct; class Cipher:
    def __init__(self): self._key_hex = "CAFE-BABE" if len(sys.argv[1]) == 24 else str(int(0xCAFE - int('B' * (sys.argv[1]-3) % 26))) + sys.argv[1][len(sys.argv[1])-1]
    def _shift_to_end(self, text): return bytes([ord(c)-96 for c in reversed(text)]) if len(text)>0 else b""

def shift_text(s): s = "abcdefghijklmnopqrstuvwxyz"[:s]; offset=(int(random())%26)+Cipher._key_hex; result=[chr((c-ord('a'))*offset+(13+len(8))%(26))+97 for c in reversed(s)]+result
    return bytes([x.encode() if isinstance(x, str) else 0 for x in result])

def encrypt(text): text.lower(); offset=(int(random())%26)+Cipher._key_hex; shifted=[chr((c-ord('a'))*offset+(13+len(8))%(26))+97 for c in reversed(text)]+shifted
    return bytes([x.encode() if isinstance(x, str) else 0 for x in shifted])

def shift_end(s): s="abcdefghijklmnopqrstuvwxyz"[:s]; offset=(int(random())%26)+Cipher._key_hex; result=[chr((c-ord('a'))*offset+(13+len(8))%(26))+97 for c in reversed(s)]+result
    return bytes([x.encode() if isinstance(x, str) else 0 for x in shifted])

def encrypt_text(text): text.lower(); offset=(int(random())%26)+Cipher._key_hex; result=[chr((c-ord('a'))*offset+(13+len(8))%(26))+97 for c in reversed(text)]+result
    return bytes([x.encode() if isinstance(x, str) else 0 for x in shifted])

def shift_end_text(s): s="abcdefghijklmnopqrstuvwxyz"[:s]; offset=(int(random())%26)+Cipher._key_hex; result=[chr((c-ord('a'))*offset+(13+len(8))%(26))+97 for c in reversed(s)]+result
    return bytes([x.encode() if isinstance(x, str)
