#!/usr/bin/env python3

# Print out shortcuts for all emojis that Google Hangout recognizes.

codepoints = {
  "!:)": "1f643", "!:-)": "1f643", "(=^..^=)": "1f638", "(=^.^=)": "1f638",
  "(N)": "1f44e", "(OK)": "1f44c", "(Y)": "1f44d", "(]:{": "1f473", "(n)":
  "1f44e", "(ok)": "1f44c", "(y)": "1f44d", "-<@%": "1f41d", "-_-": "1f611",
  ":''(": "1f62d", ":''D": "1f602", ":'(": "1f622", ":(": "1f61e", ":(:)":
  "1f437", ":(|)": "1f435", ":)": "1f642", ":)X": "1f917", ":*": "1f617", ":,":
  "1f60f", ":-(": "1f61e", ":-)": "1f642", ":-)X": "1f917", ":-*": "1f617",
  ":-,": "1f60f", ":-/": "1f615", ":-D": "1f600", ":-O": "1f62e", ":-P":
  "1f61b", ":-S": "1f616", ":-\\": "1f615", ":-o": "1f62e", ":-p": "1f61b",
  ":-s": "1f616", ":-|": "1f610", ":/": "1f615", ":3": "1f638", ":C": "2639",
  ":D": "1f600", ":O": "1f62e", ":P": "1f61b", ":S": "1f616", ":X)": "1f638",
  ":\\": "1f615", ":o": "1f62e", ":p": "1f61b", ":s": "1f616", ":|": "1f610",
  ";)": "1f609", ";*": "1f618", ";-)": "1f609", ";-*": "1f618", ";-P": "1f61c",
  ";-p": "1f61c", ";P": "1f61c", ";_;": "1f622", ";p": "1f61c", "</3": "1f494",
  "<3": "2764", "<\\3": "1f494", "='(": "1f622", "=(": "1f61e", "=)": "1f60a",
  "=*": "1f61a", "=/": "1f615", "=D": "1f604", "=O": "1f62e", "=P": "1f61b",
  "=\\": "1f615", "=^_^=": "1f638", "=o": "1f62e", "=p": "1f61b", "=|":
  "1f610", ">.<": "1f623", ">:(": "1f621", ">:(X": "1f645", ">:-(": "1f621",
  ">:D<": "1f917", ">=(": "1f621", ">_<": "1f623", "B-)": "1f60e", "D:":
  "1f626", "O.O": "1f632", "O:)": "1f607", "O:-)": "1f607", "O=)": "1f607",
  "O_o": "1f928", "T_T": "1f62d", "V.v.V": "1f980", "X(": "1f635", "X-(":
  "1f635", "X-O": "1f635", "X-o": "1f635", "\\m/": "1f918", "\\o": "1f64b",
  "^_^": "1f601", "^_^;;": "1f605", "o.o": "1f62e", "o/": "1f64b", "o_O":
  "1f928", "o_o;": "1f613", "u_u": "1f614", "xD": "1f606", "x_x": "1f635",
  "}:)": "1f608", "}:-)": "1f608", "}=)": "1f608", "~=[,,_,,]:3": "e000",
  "~@~": "1f4a9"
}

if __name__ == "__main__":
  print("| Ascii | Emoji |")
  print("| ----- | ----- |")

  for k, v in codepoints.items():
    k = k.replace('\\', r'\\')
    k = k.replace(r'|', r'\|')
    print("|{}|{}|".format(k, chr(int(v, 16))))
