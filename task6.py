# 1
lst = ([30, 75, 9, 97, 50, -4, 70, 59])
print(lst[3])
lst.remove(-4)
lst.sort(reverse=False)
print(lst)
print(lst[:4])

# 2
main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python",1]]
count = 0
for sublist in main_lst:
    if sublist[0] == "python":
        count +=1

print(count)

# 3
my_lst = ["I", "LOvE", "GAZa", "sKy", "GEEks"]
a = my_lst[0] + " " + my_lst[1] + " " + my_lst[2] + " " + my_lst[3] + " " + my_lst[4]
print(a)

# 4
my_lst = [12, 3.8, "GSG", ["sKy", "zak"]]
print(my_lst[:])

# 5
my_lst = ["GSG", "zakaria", 19, 9.8, "Omar"]
my_lst[2] = "omar"
my_lst[-1] = 19
print(my_lst)

# 6
nums = [33, 5.9, 6, -43, 9, 7, 39, 0, -40]
print(sum(nums))

# 7
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
print(tuple1 + (9,))

# 8
tuple1 = (4, 'python', 'GSG', [8, 3, 1])
tuple2 = ('Java', 'C++', 7.8)
tuple3 = tuple1 + tuple2
print(tuple3)

# the end of task 6