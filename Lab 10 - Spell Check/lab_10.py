import re


# Takes line of text and returns list of words
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():

    my_file = open("dictionary.txt")

    dictionary_list = []

    for line in my_file:
        line = line.strip()
        dictionary_list.append(line)

    my_file.close()

    print("--- Linear Search ---")

    # Opens alice file
    alice_file = open("AliceInWonderLand200.txt")

    for 




main()