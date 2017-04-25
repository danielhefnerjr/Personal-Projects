s = input().strip()

import re
for _ in range(100):
    s = re.sub(r'(.)\1','',s)
    
print(s or 'Empty String')