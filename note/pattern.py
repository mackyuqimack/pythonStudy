"""
为了避免在处理正则表达式时出现混淆，我们使用原始字符串 r"expression"。
原始字符串不会转义任何东西，这使得使用正则表达式更容易。

re.search 函数在字符串中的任何位置找到匹配的模式。
re.findall 函数返回一个与模式匹配的所有子串的列表。
"""
import re

pattern = r"spam"
# if re.match(pattern, "spamspamspam"):
#     print("Match")
# else:
#     print("No match")

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No match")

# 函数 re.finditer 和 re.findall 类似，不过它返回一个迭代器，而不是一个列表。
print(re.findall(pattern, "eggspamsausagespam"))

"""
正则表达式搜索使用多个方法返回一个对象，提供有关它的详细信息。
这些方法包括返回匹配的字符串的组，返回第一个匹配的开始和结束位置的开始和结束，以及将第一个匹配的开始和结束位置作为元组返回的跨度。
"""
pattern_two = r"pam"
match = re.search(pattern_two, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

"""
搜索和替换
使用正则表达式的最重要的 re 方法是 sub。
语法：
re.sub(pattern, repl, string, max=0)
此方法用 repl 替换字符串中所有出现的模式，除非提供 max限定修改数量。
sub 方法返回修改后的字符串。
"""
str = "My name is Loen. Hi Loen."
pattern = r"Loen"
newstr = re.sub(pattern, "Amy", str)
print(newstr)
