# Week 12 HW

# Problem 3

import urllib.request

url = "https://gist.github.com/phillipj/4944029"

destination_filename = "alicewonderland.txt"

urllib.request.urlretrieve(url, destination_filename)

with open(destination_filename, "r") as file: 
    text = file.read()

words = text.lower().split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1


sorted_words = sorted(word_counts.items())


output_filename = "alice_words.txt"
with open(output_filename, 'w') as file:
    file.write("Word Count\n")
    for word, count in sorted_words:
        file.write("{}\n".format(word, count))

with open(output_filename, "r") as file:
    for line in file:
        print(line, end = '')











