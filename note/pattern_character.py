"""
字符类提供了一种只匹配特定字符集中的一个的方法。
通过将匹配的字符放在方括号内来创建字符类。
"""
import re

pattern = r"[aeiou]"
if re.search(pattern, "grey"):
    print("Match 1")
if re.search(pattern, "qwertyuiop"):
    print("Match 2")
if re.search(pattern, "rhythm myths"):
    print("Match 3")

"""
字符类也可以匹配字符的范围。
一些例子:
[a-z] 匹配任何小写字母字符。
[G-P] 匹配从 G 到 P 的任何大写字符。
[0-9] 匹配任何数字。
一个字符类可以包含多个范围。例如，[A-Za-z] 匹配任何一个字母。
"""
pattern = r"[A-Z][A-Z][0-9]"
if re.search(pattern, "LS8"):
    print("Match 1")
if re.search(pattern, "E3"):
    print("Match 2")
if re.search(pattern, "1ab"):
    print("Match 3")

"""
在字符类的开头放置一个 ^ 来反转它, 这使得它匹配除包含的字符之外的任何字符。
其他元字符（如 $ 和 .）在字符类中没有意义。
元字符 ^ 没有意义，除非它是一个字符类中的第一个字符。
"""
# 模式[^A-Z]匹配不包括大写字母的所有字符。
pattern = r"[^A-Z]"
if re.search(pattern, "this is all quiet"):
    print("Match 1")
if re.search(pattern, "AbCdEfG123"):
    print("Match 2")
if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
