# open and read the file
file = open('sample.txt', 'r')
text = file.read()
# split text into individual words
words = text.split()
# create an empty dictionary
word_count = {}
# count how many times each word appears in the text
for word in words:
 if word in word_count:
   word_count[word] += 1
 else:
   word_count[word] = 1
# close the file
file.close()
# sort the words by frequency
sorted_words = sorted(word_count.items(), key=lambda kv: kv[1], reverse=True)
# open a new file to write the report
file = open('report.txt', 'w')
# write the words and their frequency to the report
for word in sorted_words:
 file.write(word[0] + ': ' + str(word[1]) + '\n')
# close the file
file.close()
# print a success message
print('Report saved to report.txt')