#!/usr/bin/python3

lst = [bytes.fromhex(x) for x in input().split()]
out_bytes = lst[0]
for pad_bytes in lst[1:]:
    out_bytes = [(a ^ b) for a,b in zip(out_bytes, pad_bytes)]
print(''.join([chr(x) for x in out_bytes]))


