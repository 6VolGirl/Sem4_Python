import re


def checkBraсketsWihtRe(s:str) -> bool:
    """
    Проверяет форму строки, чтобы скобки закрывались правильно.
    """
    pattern = r'\(\)|\[\]|\{\}'
    while re.search(pattern, s):
        s = re.sub(pattern, '', s)

    return len(s)==0




def checkBraсkets(s:str) -> bool:
    """
    Проверяет форму строки, чтобы скобки закрывались правильно.
    """
    brakcets_dic = {')': '(', '}': '{', ']': '['}

    stack = []
    for char in s:
        if char in brakcets_dic.values():
            stack.append(char)            #добавляем в конец
        elif char in brakcets_dic.keys():
            if stack and stack[-1] == brakcets_dic[char]:   #Проверяем не пуст ли stack и скобку
                stack.pop()
            else :
                return False
        else:
            print("There are others symbols")
    return (not stack)


s = "{()[]}"
print(checkBraсkets(s))

s = "{{}([()]))"
print(checkBraсkets(s))

s = "{{}([()]))"
print(checkBraсkets(s))