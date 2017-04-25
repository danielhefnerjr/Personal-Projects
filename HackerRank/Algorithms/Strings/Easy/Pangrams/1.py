s = input().strip().lower()

print('not pangram' if False in [chr(c) in s for c in range(ord('a'),ord('z')+1)] else 'pangram')
    