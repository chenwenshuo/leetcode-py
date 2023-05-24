s = ''
with open('C:/Users/chenws3/study/leetcode-py/leetcode/editor/study/text.txt') as ob:

    for line in ob.readlines():
        s += line

with open('text1.txt','a') as ob:
    ob.write(s)
