def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        chars = get_chars_dict(text)
        word_count = text.split()
        file_name = get_file_name()
    print_report(chars, word_count, file_name)


def word_count(text):
    return len(text.split())


def get_file_name():
    return "books/frankenstein.txt"


def get_chars_dict(text):
    chars = {}
    for c in text:
        lower_text = c.lower()
        chars[lower_text] = chars.get(lower_text, 0) + 1
    return chars


def sort_dict(chars: dict):
    return sorted(chars.items(), key=lambda x: x[1], reverse=True)


def print_report(chars, word_count, file_name):
    sorted_chars = sort_dict(chars)
    file_name = get_file_name()
    print(f"----- Report for {file_name} -----")
    print(f"Total words: {len(word_count)} found in the document")
    for c, count in sorted_chars:
        if c.isalpha():
            print(f"The '{c}' character was found {count} times")
    print("----- END REPORT -----")


if __name__ == "__main__":
    main()
