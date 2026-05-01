# info = {
# "key" : "value",
# "name" :"Pragya",
# "learning" : "coding",
# "age" : 35,
# "is_adult" : True,
# "marks" : 95.2,

# }
# print(info)


# info = {
# "name" :"Pragya",
# "Subjects" : ["Python", "C", "Java"],
# "topic" : ("dict", "set"),
# "age" : 26,
# "is_adult" : True,
# "marks" : 94.2,
# }
# print(info["name"])
# print(info["Subjects"])
# print(info["age"])



# nested dictionary
# student = {

# "name" : "piyush dubey",
# "subject" : {
#     "phy" : 68,
#     "chem" : 89,
#     "math" : 95,

# }
# }
# print(student)



# dic.keys, .values,.items,.gets

# student = {

# "name" : "piyush dubey",
# "subject" : {
#     "phy" : 68,
#     "chem" : 89,
#     "math" : 95,

# }
# }
# student.update({"city" : "gorakhpur", "age" : 12})
# print(student)



# Set

# Set is the collection of unordered items
# Each element in the set must be unique & immutable.

# collection = { 1, 2, 3, 4 , "Hello this is Pragya ,"}
# print(collection)
# print(type(collection))


# REmove

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)

# collection.remove(2)
# print(collection)


# Clear

# collection = set()
# collection.add(1)
# collection.add((2, 1, 3))
# collection.add("Pragya")

# collection.clear()

# print(len(collection))


# Pop

# collection = {"hello", "Pragya", "World", "Coding"}

# print(collection.pop())
# print(collection.pop())

# Set Method

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# print(set1.union(set2))
# print(set1)
# print(set2)


# Intersection

# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.intersection(set2))


# Pratices
# dictionary = {
#     "cat" : "a small animal",
#     "table" : ["apiece of furniture", "list of fact & figures"]

# }
# print(dictionary)



# subjects = {
#     "python", "java", "c++", "python", "javascript", "java",
#     "python", "java", "c++", "c"
# }
# print(len(subjects))



marks ={}

x = int (input("enter physics :"))
marks.update({"physics" : x})

x = int (input("enter physics :" ))
marks.update({"maths" : x})

x = int (input("enter physics : "))
marks.update({"chemistry" : x})

print(marks)