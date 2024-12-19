def countChar(file_contents):
    letterdictonary = {}
    wordslowercase = file_contents.lower()
    for char in wordslowercase:
        if char not in letterdictonary:
            letterdictonary[char] = 1
        else:
            letterdictonary[char] += 1
    print(letterdictonary)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        wordcount = len(file_contents.split())
        print(wordcount)
        countChar(file_contents)


main()
