"""
元字符使正则表达式比普通的字符串方法更强大。
元字符允许您创建正则表达式来表示像“一个或多个元音的重复”这样的概念。
如果要创建与文字元字符（例如“$”）匹配的正则表达式，则元字符的存在会造成问题。你可以通过在它们前面加一个反斜杠来转义元字符。
但是，这可能会导致问题，因为反斜杠在正常的 Python 字符串中也有一个转义的功能。
这可能意味着需要连续放置三或四个反斜杠来完成所有的转义。
---
为了避免这种情况，你可以使用一个原始字符串，这是一个前面带 "r" 的普通字符串。
在上一课中我们看到了原始字符串的使用。

我们将看到的第一个元字符是 . （点）。
它匹配任何字符，但不匹配新的行。
"""
import re

pattern = r"gr.y"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "blue"):
    print("Match 3")

"""
接下来的两个元字符是 ^ 和 $ 。
这两个分别匹配字符串的开始和结束。
"""
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("Match 1")
if re.match(pattern, "gray"):
    print("Match 2")
if re.match(pattern, "stingray"):
    print("Match 3")
