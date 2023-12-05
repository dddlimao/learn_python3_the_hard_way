"""
运行方法

python ex23.py utf-8 strict

这里strict是error参数的一个值，其他可选值如下：

"strict"：默认选项，如果遇到编码错误会抛出 UnicodeDecodeError 或 UnicodeEncodeError 异常。

"ignore"：忽略遇到的编码错误，直接跳过。

"replace"：将无法解码或编码的字符替换为 Unicode 替换字符（通常是 U+FFFD）。

"backslashreplace"：将无法解码或编码的字符替换为 Python 转义序列，比如 \xNN 或 \uNNNN。

"xmlcharrefreplace"：将无法解码或编码的字符替换为 XML 实体引用，比如 &#NN;。

"namereplace"：将无法解码或编码的字符替换为 Unicode 名称转义，比如 \N{...}。

"""



import sys

script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    # 作用是去除变量 line 中的首尾空白字符（比如空格、制表符、换行符等）
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<====>", cooked_string)


languages = open("ex23_languages.txt", encoding="utf-8")

main(languages, encoding, error)
