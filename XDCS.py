import string

with open("XDCS.inp","r") as file_input :
    s1,s2,s3 = file_input.read().splitlines()
    file_input.close()

letters = string.ascii_uppercase
largest_s1,largest_s2,largest_s3 = 0,0,0
for char in s1 :
    if char in letters : largest_s1 = letters.index(char) + 11
    else : 
        if int(char) > largest_s1 : largest_s1 = int(char)

for char in str(s2) :
    if char in letters : largest_s2 = letters.index(char) + 11
    else :
        if int(char) > largest_s2 : largest_s2 = int(char)
            
for char in s3 :
    if char in letters : largest_s3 = letters.index(char) + 11
    else :
        if int(char) > largest_s3 : largest_s3 = int(char)
answer = max(largest_s1,largest_s2,largest_s3) + 1
#print("{} {} {}".format(s1,s2,s3))
#print("{} {} {}".format(largest_s1,largest_s2,largest_s3))
#print(answer)
with open("XDCS.out","w") as file_output :
    file_output.writelines(str(answer))
    file_output.close()