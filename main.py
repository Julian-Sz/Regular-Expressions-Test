import re


def get_email_answers(path):
    for line in path:
        clear = line.strip()
        if re.match(r".*\s.*\t(Antw.+)\t.*Uhr", clear):
            subject = re.findall(r".*\s.*\t(Antw.+)\t.*Uhr", clear)
            print(subject)


def get_sizes(path):
    for line in path:
        clear = line.strip()
        if re.match(r".*\s([0-9][0-9]\s[MKG]B)", clear):
            size = re.findall(r".*([0-9][0-9]\s[MKG]B)", clear)
            print(size)
        elif re.match(r".*\s([0-9][0-9][0-9]\s[MKG]B)", clear):
            size = re.findall(r".*([0-9][0-9][0-9]\s[MKG]B)", clear)
            print(size)
        elif re.match(r".*\s([0-9]\s[MKG]B)", clear):
            size = re.findall(r".*([0-9]\s[MKG]B)", clear)
            print(size)
        elif re.match(r".*(.\.[0-9][0-9]\s[MKG]B)", clear):
            size = re.findall(r".*(.\.[0-9][0-9]\s[MKG]B)", clear)
            print(size)


xfile = open(r"C:\Users\julia\Documents\RegEX-Test.txt", "r")
get_sizes(xfile)
xfile.seek(0)
print("\n---------------------------------------------------------------\n")
get_email_answers(xfile)
