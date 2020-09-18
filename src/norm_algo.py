# read a way to file
file_way = "D:/test/test1.txt"
# read substitution set
substitutions = []
with open(file_way, "r") as file:
    n = int(readline())
    for i in range(n):
        substitutions.append(readline())
    k = int(readline())
    for i in range(k):
        words.append(readline())
print(substitutions, sep="\n")
print(words, sep="\n")

# turn into
# s = s.split(" ")
