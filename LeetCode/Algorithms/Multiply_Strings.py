"""
:type num1: str
:type num2: str
:rtype: str
"""

num1 = '123'
num2 = '456'
rtn_sum = 0

i = 0
j = 0
l1 = len(num1) - 1
l2 = len(num2) - 1

while (j <= l2):
    cur_sum = 0
    q = 0

    i = 0
    while (i <= l1):
        sm = q + (int(num1[l1 - i]) * int(num2[l2 - j]))
        print(i, j, num1[l1 - i], num2[l2 - j])
        q = sm // 10

        if (i == l1):
            cur_sum = cur_sum + (sm * (10 ** i))
        else:
            cur_sum = cur_sum + (sm % 10) * (10 ** i)
        i = i + 1

    rtn_sum = rtn_sum + (cur_sum * (10 ** j))
    print(j, rtn_sum )
    j = j + 1

print(str(rtn_sum))

'''
class Solution:
    def multiply(self, num1, num2):

        product = [0] * (len(num1) + len(num2)) #placeholder for multiplication ndigit by mdigit result in n+m digits
        position = len(product)-1 # position within the placeholder

        for n1 in num1[::-1]:
            tempPos = position
            for n2 in num2[::-1]:
                product[tempPos] += int(n1) * int(n2) # ading the results of single multiplication
                product[tempPos-1] += product[tempPos]//10 # bring out carry number to the left array
                product[tempPos] %= 10 # remove the carry out from the current array
                tempPos -= 1 # first shifting the multplication to the end of the first integer
            position -= 1 # then once first integer is exhausted shifting the second integer and starting


        # once the second integer is exhausted we want to make sure we are not zero padding
        pointer = 0 # pointer moves through the digit array and locate where the zero padding finishes
        while pointer < len(product)-1 and product[pointer] == 0: # if we have zero before the numbers shift the pointer to the right
            pointer += 1

        return ''.join(map(str, product[pointer:])) # only report the digits to the right side of the pointer
'''

print('--neat solution---')

temp_prd = [0] * (len(num1) + len(num2))  # temp array filled with zeros
temp_idx = len(temp_prd) - 1

for m in num2[::-1]:
    curr_idx = temp_idx
    for n in num1[::-1]:
        temp_prd[curr_idx] += int(n) * int(m)
        temp_prd[curr_idx - 1] += temp_prd[curr_idx] // 10
        temp_prd[curr_idx] = temp_prd[curr_idx] % 10
        curr_idx -= 1
    temp_idx -= 1

ptr = 0  # pointer to the determine the begin of the product
while (ptr < len(temp_prd) and temp_prd[ptr] == 0):
    ptr += 1

# prd_str = ''.join(str(temp_prd[ptr:]))
print(''.join(str(temp_prd[ptr:])))

prd_str = ''.join(map(str, temp_prd[ptr:]))
print(''.join(map(str, temp_prd[ptr:])))
