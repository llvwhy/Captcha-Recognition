from util import read_CSV
import conf

# load mappings.txt
dict1 = read_CSV("mappings.txt")
dict2 = read_CSV("raw_mappings.txt")

# Calculate the accuracy.
correct = 0
for i in range(conf.TEST_NUMBER):
    if dict1[i] == dict2[i]:
        correct += 1
    else:
        print("Number:",i,"False:",dict1[i],"True:",dict2[i])
print("Accuracy:",correct / conf.TEST_NUMBER)
