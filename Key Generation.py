PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43,
       35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54,
       46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7,
       27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39,
       56, 34, 53, 46, 42, 50, 36, 29, 32]

Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

#2 strings to hold the final C's and D's
global C_final
global D_final
C_final =[]
D_final =[]

#perform left circular shift for a list
def rotate(l, n):
    return l[n:] + l[:n]

#concatenate C's and D's into K
def concatenate (c,d):
    Key = []
    for i in range(0,len(c)):
        Key.append(c[i]+d[i])

    return Key

# convert hex input into binary string
def convert_to_binary(x):
    try:
        decimal = int(x, 16)  # interpret the input as a base-16 number, a hexadecimal.
        b = "{0:b}".format(decimal)  # Convert to binary format to make permutation
        for i in range(len(b) + 1, 65):
            b = "0" + b

    except ValueError:
        print("You did not enter a hexadecimal number!")

    return b


# split the 56-bit key into C and D parts each 28-bit
def split(b):
    C, D = b[:int(len(b) / 2)], b[int(len(b) / 2):]
    return C, D


# perform first permutation on the key using PC1
def first_permutation(b):
    out = ""
    for i in range(0, len(PC1)):
         #64-value in p-box as string is arranged in reverse order of bits first bit is of index 63 in len of 64
        out += b[64-PC1[i]]

    return out

# perform second permutation on the key using PC2
def second_permutation(b):
    out = ""
    final_key =[]
    for j in range(0,len(b)):
        temp = b[j]
        for i in range(0, len(PC2)):
             #64-value in p-box as string is arranged in reverse order of bits first bit is of index 63 in len of 64
            out += temp[56-PC2[i]]
        final_key.append(out)
        out =""

    return final_key


# perform shift left circular to C,D parts of the key using Rotations table
def shift(C, D):
    C_final.append(C)
    D_final.append(D)
    int_temp =[]

    for i in range(1, len(Rotations)):
        [int_temp.append(int(d)) for d in C_final[i-1]] #convert C from string to list of booleans to rotate
        int_temp = rotate(int_temp , Rotations[i])
        C_final.append ("".join(str(i) for i in int_temp))
        int_temp =[]
        [int_temp.append(int(d)) for d in D_final[i-1]]
        int_temp = rotate(int_temp , Rotations[i])
        D_final.append ("".join(str(i) for i in int_temp))

    return C_final,D_final

#print keys in hex format
def print_Keys (k):
    for i in range (0,len(k)):
        print (format(k[0], '02x').upper())



x = input("Enter hex Value : \n")
K = convert_to_binary(x)
K_plus = first_permutation(K)
print (len(K_plus))

C, D = split(K_plus)
print (len(C))

c_f ,d_f = shift(C,D)
print(len(c_f[0]))
Key = concatenate(c_f,d_f)
print (len(Key[0]))
Key = second_permutation(Key)

print_Keys(Key[0])

#
# print (K[64-PC1[7]])