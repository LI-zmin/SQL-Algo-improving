def oneEditAway(s1,s2):
    if len(s1)==len(s2):
        return oneEditReplace(s1,s2)
    elif len(s1)+1 == len(s2):
        return oneEditInsert(s1,s2)
    elif len(s1)-1 == len(s2):
        return oneEditInsert(s2,s1)    
    return False

def oneEditReplace(s1, s2):
    foundDiff = False
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            if foundDiff:
                return False
            else: foundDiff=True
    return True

def oneEditInsert(short, longer):
    foundDiff = False
    for i in range(len(short)):
        if short[i]!=longer[i]:
            if short[i]!=longer[i+1]:
                return False
    return True

s1 = 'pale'
s2 = 'ple'
print(oneEditAway(s1,s2))