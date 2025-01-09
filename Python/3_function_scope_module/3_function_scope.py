# 2つの文字列を引数とし、このどちらか一方の文字列が他方の文字列内に含まれる場合、
# True を返し、それ以外の場合、False を返す関数（isIn 関数）を書け。


# in
def isIn_using_in(str1, str2):
    return str1 in str2 or str2 in str1


# 使用例
print(isIn_using_in("hello", "world"))  # False
print(isIn_using_in("hello", "hello world"))  # True


# findメソッド
def isIn_using_find(str1, str2):
    return str1.find(str2) != -1 or str2.find(str1) != -1


# 使用例
print(isIn_using_find("hello", "world"))  # False
print(isIn_using_find("hello", "hello world"))  # True


# countメソッド
def isIn_using_count(str1, str2):
    return str1.count(str2) > 0 or str2.count(str1) > 0


# 使用例
print(isIn_using_count("hello", "world"))  # False
print(isIn_using_count("hello", "hello world"))  # True
