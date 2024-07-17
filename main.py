def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        text = f.read()
        chars = get_chars_dict(text)
        word_count = len(text.split())
        file_name = get_file_name(book_path)
    print_report(chars, word_count, file_name)


def get_file_name(book_path: str):
    with open(book_path) as f:
        return f.name


def get_chars_dict(text: str):
    chars = {}
    for c in text:
        lower_text = c.lower()
        chars[lower_text] = chars.get(lower_text, 0) + 1
    return chars


def sort_dict(chars: dict):
    return sorted(chars.items(), key=lambda x: x[1], reverse=True)


def print_report(chars: dict, word_count: int, book_path: str):
    sorted_chars = sort_dict(chars)
    print(f"----- Report for {book_path} -----")
    print(f"Total words: {word_count} found in the document")
    for c, count in sorted_chars:
        if c.isalpha():
            print(f"The '{c}' character was found {count} times")
    print("----- END REPORT -----")


if __name__ == "__main__":
    main()
