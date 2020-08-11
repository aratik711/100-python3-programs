"""

Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints: Use zlib.compress() and zlib.decompress() to compress and decompress a string.

"""
import zlib
s = b'hello world!hello world!hello world!hello world!'
compressed = zlib.compress(s)
print (compressed)
print (zlib.decompress(compressed))