from collections import defaultdict

def file_string(file_name):
    with open(file_name) as f:
        return f.read()

def count_words(string):
    return len(string.strip().split())

def count_char(file_string):
    chars = defaultdict(int)
    lowered_string = file_string.lower()
    for char in lowered_string:
        chars[char] += 1 
    return chars

def sort_on(dict):
    return dict["count"]

def dict_into_list(dict):
    list = []
    for key, value in dict.items():
        if key.isalpha():
            list.append({"char": key, "count": value})
    list.sort(reverse=True, key=sort_on)
    return list

def report(list, total):
    report = "--- Begin report of books/frankenstein.txt --- \n"
    report += f"{total} words found in the document\n\n"
    for item in list:
        report += f"The '{item['char']}' character was found {item['count']} times\n"
    report += "--- End report ---"
    return report


def main():
    string = file_string("books/frankenstein.txt")
    count = count_words(string)
    chars = count_char(string)
    sorted_dict = dict_into_list(chars)
    finished_report = report(sorted_dict,count)
    print(finished_report)

main()
