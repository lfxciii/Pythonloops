# Introduction to Programming, Task 15
# Ruben Louw, [2019-04-13]
# an interesting algorithm, prints a triable


# ================= Compulsory Task =================
# Create a new Python file in this folder called “TriTable.py.” 
# Write a program that uses nested for loops to create the following number pyramid.

# 1
# 2     4       
# 3     6       9
# 4     8       12      16
# 5     10      15      20      25
# 6     12      18      24      30      36
# 7     14      21      28      35      42      49
# 8     16      24      32      40      48      56      64
# 9     18      27      36      45      54      63      72      81



for i in range(1, 10): # 1 - 9 rows
    print(str(i), end = '')

    for j in range(2, i + 1): # start on the second column
        print("\t" + str(i * j), end = '')

    print () # print newline \n

   


