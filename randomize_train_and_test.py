import random

train = open('prepared-spreadsheets/07_train.csv', 'r')
test = open('prepared-spreadsheets/08_test.csv', 'r')
train_lines = train.readlines()
test_lines = test.readlines()

train.close()
test.close()

random.shuffle(train_lines)
random.shuffle(test_lines)

train = open('prepared-spreadsheets/07_train.csv', 'w')
test = open('prepared-spreadsheets/08_test.csv', 'w')
train.writelines([line for line in train_lines])
test.writelines([line for line in test_lines])

train.close()
test.close()