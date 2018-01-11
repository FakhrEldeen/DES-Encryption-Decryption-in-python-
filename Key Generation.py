#This Code written by Fakhr Eldeen Gamal 
#This is Key Generation Functions for DES Encryption Algorithm 



#Values of First Permutation Box 
PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43,
       35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54,
       46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

#Values of Second Permutation Box
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7,
       27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39,
       56, 34, 53, 46, 42, 50, 36, 29, 32]

#Rotation Values for each Iteration
Rotations = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# 3 strings to hold the final C's and D's and String to hold the 16-Keys of DES Rounds 
global C_final
global D_final
global Keys
Keys = []
C_final = []
D_final = []


# perform left circular shift for a list
def rotate(l, n):
    return l[n:] + l[:n]


# concatenate C's and D's into K
def concatenate(c, d):
    Key = []
    for i in range(0, len(c)):
        # print(i," ",c[i]+d[i])
        Key.append(c[i] + d[i])

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
    # temp = b[::-1]
    temp = b
    for i in range(0, len(PC1)):
        # 64-value in p-box as string is arranged in reverse order of bits first bit is of index 63 in len of 64
        out += temp[PC1[i] - 1]

    return out


# perform second permutation on the key using PC2
def second_permutation(b):
    out = ""
    final_key = []
    for j in range(0, len(b)):
        temp = b[j]
        for i in range(0, len(PC2)):
            # 64-value in p-box as string is arranged in reverse order of bits first bit is of index 63 in len of 64
            out += temp[PC2[i] - 1]
        final_key.append(out)
        out = ""

    return final_key


# perform shift left circular to C,D parts of the key using Rotations table
def shift(C, D):
    int_temp = [] # temp list to hold integers from converted string(C,D) to use rotate in list 

    [int_temp.append(int(d)) for d in C]  # convert C from string to list of booleans to rotate
    int_temp = rotate(int_temp, Rotations[0])

    C_final.append("".join(str(i) for i in int_temp))
    int_temp = []
    [int_temp.append(int(d)) for d in D]
    int_temp = rotate(int_temp, Rotations[0])
    D_final.append("".join(str(i) for i in int_temp))
    int_temp = []

    for i in range(1, len(Rotations) ):
        [int_temp.append(int(d)) for d in C_final[i-1]]  # convert C from string to list of booleans to rotate
        int_temp = rotate(int_temp, Rotations[i])
        # print(Rotations[i-1] , "  ", int_temp)
        C_final.append("".join(str(i) for i in int_temp))
        int_temp = []
        [int_temp.append(int(d)) for d in D_final[i -1]]
        int_temp = rotate(int_temp, Rotations[i])
        D_final.append("".join(str(i) for i in int_temp))
        int_temp = []

    return C_final, D_final


# print keys in hex format
def print_Keys(k):
    
    for i in range(0, len(k)):

        temp = int(k[i], 2)
        Keys.append(format(temp, '02x').upper().zfill(12))
        print(Keys[i])

       
# this function when it's called it Generates the 16-Key for DES Rounds using the functions above 
def key_generation():     
    x = input()
    K = convert_to_binary(x)
    K_plus = first_permutation(K)
    C, D = split(K_plus)
    c_f, d_f = shift(C, D)
    Key = concatenate(c_f, d_f)
    Key = second_permutation(Key)
    print_Keys(Key)
    
   

