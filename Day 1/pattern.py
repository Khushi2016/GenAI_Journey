# ***
# ***
# ***

# for i in range(1,4):
#     for j in range(1,4):
#         print('*',end='')
#     print('')

# 123
# 123
# 123

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,end='')
#     print('')

# *      (1,2)
# **     (1,3)
# ***    (1.4)
# ****   (1,5)

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end='')
#     print('')

#  ****  (1,5)
#  ***   (1,4)
#  **    (1,3)
#  *     (1,2)

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print('')


# 4444
# 333
# 22
# 1

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print('')

#  1234
#  123
#  12
#  1

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(j,end='')
#     print('')

#  space 
#      *   s=4   (1,5)
#     **   s=3   (1,4)
#    ***   s=2   (1,3)
#   ****   s=1   (1,2)
#  *****   s=0   (1,1)

# for i in range(1,6):   #row
#     for s in range(1,6-i):
#         print(' ',end='')
#     for j in range(1,i+1):  #column
#         print('*',end='')
#     print('')

#     1
#    12
#   123
#  1234
# 12345

# for i in range(1,6):
#     for s in range(1,6-i):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     print('')

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

for i in range(1,6):  #row
    for s in range(1,6-i):
        print(' ',end='')
    for j in range(1,i+1):  #column
        print('* ',end='')
    print('')

