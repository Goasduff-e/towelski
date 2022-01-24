def fusion(T1, T2):
    """
    T1 : une liste triée
    T2 : une liste triée
    Retourne la fusion des 2 listes triée
    """
    result=[]
    i1 = i2 =0
    while i1 < len(T1) and i2<len (T2):
        if T1[i1] <= T2[i2] :
            result.append(T1[i1])
            i1 = i1 + 1
        elif T1[i1] >= T2[i2] :
            result.append(T1[i1])
            i2 = i2 + 1
    if T1[i1:]:
        result.extend(T2[i2])
    if T2[i2:]:
        result.extend(T1[i1])
    
    return result
    
print (fusion([1,3,4,7],[2,5,6,9,10,11,12]))