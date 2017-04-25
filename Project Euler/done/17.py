ones = ['one','two','three','four','five','six','seven','eight','nine']
tens = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
l = 0
for i in range(1,1001):
    s = str(i)

    if i == 1000:
        l += len('onethousand')
        break

    if i > 10:
        if 11 <= int(s[-2:]) <= 19:
            l += len(teens[i%100-11])
        else:
            l += len(ones[int(s[-1])-1]) if s[-1] != '0' else 0
            l += len(tens[int(s[-2])-1]) if s[-2] != '0' else 0

        if i >= 100:
            l += len(ones[int(s[0])-1]) + len('hundred')
            if i % 100 > 0:
                l += len('and')
    else:
        l += len(ones[int(s[0])-1])
    
def c(i):
    l = 0
    s = str(i)

    if i == 1000:
        l += len('onethousand')
        return l

    if i > 10:
        if 11 <= int(s[-2:]) <= 19:
            l += len(teens[i%100-11])
        else:
            l += len(ones[int(s[-1])-1]) if s[-1] != '0' else 0
            l += len(tens[int(s[-2])-1]) if s[-2] != '0' else 0

        if i >= 100:
            l += len(ones[int(s[0])-1]) + len('hundred')
            if i % 100 > 0:
                l += len('and')
    else:
        l += len(ones[int(s[0])-1])

    return l
