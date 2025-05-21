# matrix = [[1,2,3,4],[6,7,8,9],[11,12,13,14],["dave","bob"]]
# # print(matrix)  
# # print(matrix[3][1])
# fruit = ["apple", "pineapple", "mango", "peach", "orange"]
# # print(fruit[2])
# print(len(fruit))
# # looping through 2 dimensional list
# for i in range(0, len(matrix)):
#     for j in range(0, len(matrix)):
#        print(matrix[i][j])
#     print("\n")

rows = int(input("How many rows do you want?:"))
columns = int(input("How many columns do you want?:"))
matr1x = []
for i in range(rows):
    temp = []
    for j in range(columns):
        x = int(input("Enter your element - "))
        temp.append(x)
    matr1x.append(temp)
    
for i in range(rows):
    for j in range(columns):
        print(matr1x[i][j], end = " ")
    print("\n")