# read a way to file
file_way = "D:/test/test1.txt" #test block
# read substitutions and words
substitutions = []
words = []
with open(file_way, "r") as file:
    sub_count = int(file.readline())
    for i in range(sub_count):
        substitutions.append(file.readline())
    word_count = int(file.readline())
    for i in range(word_count):
        words.append(file.readline())
#bring a word and do this
while i < word_count:
    word = words[i]
    while k < sub_count:
        sub = substitutions[k]
        s = sub.split(" ")
        if word.find(s[0]) != -1:
            word.replace(s[0], s[1], 1)
            words[i] = word
            # breaking if 1 in s[2] else j = 0
        else
            k += 1
    i += 1
