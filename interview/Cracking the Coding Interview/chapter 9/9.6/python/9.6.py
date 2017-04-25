def parens(s,n,nopen,nclose):
    if nopen == n and nclose == n:
        print(s)
        return

    if nopen < n:
        parens(s+'(',n,nopen+1,nclose)

    if nclose < n and nclose < nopen:
        parens(s+')',n,nopen,nclose+1)


parens('',3,0,0)
parens('',2,0,0)
