s = input().strip().lower()

print('pangram' if all(chr(c) in s for c in range(ord('a'),ord('z')+1)) else 'not pangram')
    