import re


class Regex:
    def __init__(self, regex_str, str):
        self.str = str
        self.regex_str = regex_str
        self.reg_list = re.findall(regex_str, str)

    def __iter__(self):
        self.match_number = 0
        return self

    def __next__(self):
        if self.match_number < len(self.reg_list):
            self.match_number += 1
            return self.reg_list[self.match_number - 1]
        else:
            raise StopIteration


def main():
    reg = Regex(r'\d+', 'ab22cx345xb19')
    i = iter(reg)

    for s in i:
        print(s)


if __name__ == "__main__":
    main()
