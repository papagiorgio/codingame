import sys
str = input()
u_str = [ord(c) for c in str]

binary = [f"{c:07b}" for c in u_str]
binary = "".join(binary)

ans=[]

curr = -1

for bit in binary:
    if bit == curr:
        ans.append("0")
    else:
        curr = bit
        ans.append(" 0 0" if bit=="1" else " 00 0")
        
print("".join(ans).strip())