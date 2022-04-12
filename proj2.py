import math

def egcd(a,b):
    # TODO: implement Extended Euclidean Algorithm and return the values r,s,t, and q from the row *before* r = 0

    
    r, r1 = a, b
    s, s1 = 1, 0
    t, t1 = 0, 1
    q, q1 = 0, 0
    
    while r1 > 0:
        q2 = r // r1
        r2 = r - q2 * r1 
        s2 = s - q2 * s1 
        t2 = t - q2 * t1
        q, q1 = q1, q2 
        r, r1 = r1, r2 
        s, s1 = s1, s2 
        t, t1 = t1, t2
        
   #print(r, s, t, q)
    return [r,s,t,q]
    



def find_d(k,e):
    return egcd(k,e)[2]

assert find_d(72,7) == 31
assert find_d(1449000,7907) == 643043


def keyset(p, q, e):
    # TODO: calculate and return n, e, and d
    
    k = (p - 1) * (q - 1)
    n = p * q
    d = find_d(k, e)
    return [n, e, d]

[n, e, d] = keyset(1381,1051,7907)
assert [n, e, d] == [1451431, 7907, 643043] 



M = 'hello there secret friend'
def encrypt(message, e, n):
    # TODO: encrypt the message character by character
    C = []
    
    for m in message:
        c = pow(ord(m), e, n)
        C.append(c)
        
    return C

cipher = encrypt(M, e, n)
assert cipher == [1041244, 739369, 892978, 892978, 799576, 304346, 1398703, 1041244, 739369, 38960, 739369, 304346, 642935, 739369, 1079616, 38960, 739369, 1398703, 304346, 360690, 38960, 722667, 739369, 462214, 282605]





def decrypt(cipher, d, n):
    # TODO: implement decrypt + decode
    M = []
    
    for c in cipher:
        m = pow(c, d, n)
        m = chr(m)
        M.append(m)
        
    decrypted_message = "".join(M)
    #print(decrypted_message)
    return decrypted_message

message = decrypt(cipher, d, n)
assert message == M




def naivefactors(n):
    # TODO: implement a function that factors a semi-prime into an array of primes
    # note: you may assume that n=p*q where p>1 and q>1
    from math import sqrt
    
    a = []
    
    for a in range(2, int(sqrt(n))):
        if (n % a == 0):
            return[a, int(n / a)]
        

assert naivefactors(21) == [3,7]
assert naivefactors(59444051) == [7703,7717]





[n, e] = [39217303, 7687]
C = [7473306,34860190,31360573,20968028,9070305,20827012,34743153,11419633,36622909,20827012,34743153,7882764,34860190,31360573,21566064,7163950,34860190,31360573,7163950,13366249,34860190,11419633,9070305,7163950,20827012,19210583,29100039,7882764,131312,12921995,131312,21521610,131312,31360573,34743153,4735271,7163950,9665260,7882764,34743153,29100039,7163950,131312,12921995,131312,9070305,13366249,7163950,20827012,19210583,19210583,34860190,21521610,10677701,36622909,7882764,21566064,29100039,21521610,131312,31360573,34743153,7467220,7163950,34743153,29100039,131312,9070305,131312,7163950,7882764,21566064,7163950,20827012,31360573,7163950,131312,31360573,18965078,4735271,7163950,9665260,7882764,34743153,29100039,7163950,131312,12921995,131312,9070305,13366249,7163950,131312,31360573,18965078,7163950,34743153,29100039,131312,9070305,131312,7163950,7882764,21566064,7163950,20827012,36622909,15592578,20827012,13366249,21566064,7163950,20827012,7163950,31360573,131312,15592578,7163950,8995063,131312,20968028,7882764,31360573,31360573,7882764,31360573,20968028,4735271,7163950,32047640,7882764,33864881,131312,7163950,19210583,34860190,31360573,34743153,7882764,31360573,11419633,20827012,36622909,36622909,13366249,7163950,21521610,34860190,12921995,131312,21566064,7163950,33864881,9070305,34860190,21521610,7163950,20827012,7163950,8995063,131312,20968028,7882764,31360573,31360573,7882764,31360573,20968028,4735271,4735271,4735271,7163950,34743153,34860190,7163950,20827012,31360573,7163950,131312,31360573,18965078,4735271,4735271,4735271,34743153,34860190,7163950,20827012,7163950,31360573,131312,15592578,7163950,8995063,131312,20968028,7882764,31360573,31360573,7882764,31360573,20968028,4735271]


# TODO: complete the mission
# TODO: complete the mission
result = naivefactors(n)

        
result2 = keyset(result[0], result[1], e)

message = decrypt(C, result2[2], result2[0])

print(message)
