def str_reverse(s):
    return s[::-1]
def substr(s,x,y):
    if(y>x):
        return s[int(x):int(y)]
    else:
        return 0