def sort_on(dict):
    return dict["num"]
def countChar(file_contents,wordcount):
    letterdictonary = {}
    letter_list = []
    wordslowercase = file_contents.lower()
    for char in wordslowercase:
        if char.isalpha():
            if char not in letterdictonary:
                letterdictonary[char] = 1
            else:
                letterdictonary[char] += 1
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{wordcount} words found in the document\n")
    for char in letterdictonary:
        if char.isalpha():
            letter_list.append({"char": char, "num": letterdictonary[char]})
    letter_list.sort(reverse=True, key=sort_on)
    for item in letter_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("--- End report ---")


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        wordcount = len(file_contents.split())
        countChar(file_contents,wordcount)


main()
