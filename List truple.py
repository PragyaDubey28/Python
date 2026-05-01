# marks = [94.2, 84.6, 95.6, 54.6, 38.9] 
# print(marks)
# print(type(marks))
# print(len(marks))
# print(marks[0])
# print(marks[1])


# student = ["Pragya", 95.2, 18, "Gorakhpur"]
# print(student[0])
# student[0] = "Piyush"
# print(student)

# list
#list.append
# list = [2, 3 , 1]
# list.append(4)
# print(list)

#list.sort

# list = [8, 3, 5, 1]
# print(list.sort())
# print(list)

#list.sort(reverse=True)

# list = [8, 3, 5, 1]
# print(list.sort(reverse=True))
# print(list)



# list = ["a", "b", "c", "d"]
# print(list.sort)
# print(list.sort(reverse=True))
# print(list)

#list.reverse

# list = [8, 3, 5, 1]
# print(list.reverse())
# print(list)

#list.insert


# list = [2, 1, 3]
# list.insert(1, 5)
# print(list)
 
# list = [5, 8, 2, 3]
# list.insert(2, 6)
# print(list)

#list.remove

# list = [2, 1, 3, 1]
# list.pop(2)
# print(list)

# Tuples

# tup = (2, 1, 3, 1)
# print(tup[0])
# print(tup[2])

# index method

# tup = (1, 2, 3, 4)
# print(tup.index(2))

# count method

# tup = (1, 2, 3, 4, 2)
# print(tup.count(2))



# practice

# ex1- WAP to ask the user to enter names of their 3 favorite movies & store them in a list
# movies = []
# mov1 = input("enter 1st movies: ")
# mov2 = input("enter 2nd movies: ")
# mov3 = input("enter 3rd movies: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("NOT palindrone")

# ex3- WAP to count the number of students with the "A" grade in the following tuple

# grade = ("C","D","A","A","B","B","A")
# print(grade.count("A"))

# ex4- Store the above value in a list & sort them from "A" to "D"

list = ["C","D","A","A","B","B","A"]
list.sort()
print(list)