import matplotlib.pyplot as plt

counts = [('trump', 488), ('the', 441), ("to", 357), ('hillary', 292), ('is', 255), \
('a', 233), ('clinton', 225), ('of', 183), ('donald', 158), ('for', 152), \
('in', 149), ('this', 146), ('and', 137),('on', 112),('you', 112),('with', 104),\
('i', 86),('are', 83),('he', 82),('&amp', 80)]

words = [x[0] for x in counts]
values = [int(x[1]) for x in counts]

mybar = plt.bar(range(len(words)), values, color='green', alpha=0.4, align='center')
plt.xticks(range(len(words)), words)

plt.xlabel('Word')
plt.ylabel('Word Count')
plt.title('Word Count Chart')
plt.legend()

plt.show()
