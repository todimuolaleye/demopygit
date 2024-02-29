import csv
from collections import Counter
def count_word_frequencies(file_name):
    word_counter = Counter()

    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            words =[word.strip().lower() for word in row[0].split(',')]
            word_freq.update(words)
    return word_counter


if __name__ == "__main__":
    file_name = "input1.csv"
    frequencies = count_word_frequencies(file_name)
    for word, count in frequencies.items():
        print(f"{word} {frequencies[word]}")
