import os
# python file system
# rawx -> read, append, write, create

# read
f = open("names.txt")
json = open("data.json")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(json.read())

for name in f:
    print(name)

f.close()
json.close()


try:
    f = open("namesx.txt")
    print(f.read())
except:
    print("File doesnot exitst")
finally:
    f.close()


# append -> add to the end of the file and creates file if it doesnt already exist
f = open("names.txt", "a")
f.write("\nNantabba")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# write -> overwrites anything in the file and writes a file if it doesnot exist
f = open("test.txt", "w")
f.write("Hello")
f.close()

f = open("test.txt")
print(f.read())
f.close()

# x -> creates a file if it doesnot exists but also throws error if file exits
if not os.path.exists("newtest.txt"):
    f = open("newtest.txt", "x")
    f.close()
else:
    print("File already exists man")

# delete a file
# removw -> deletes a file if it already exists but throws error if file doesnt exist

if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("File doesnot exist man!")

# copying files from one file to another;

with open('names.txt') as f:
    content = f.read()

with open('newtest.txt', 'w') as f:
    f.write(content)
    f.close()
