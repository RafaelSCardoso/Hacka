import random

filtered_csv = open('spreadsheets/03_filtered.csv', 'r')

positive_csv = open('prepared-spreadsheets/01_positive.csv', 'w')
positive80_csv = open('prepared-spreadsheets/02_positive_training.csv', 'w')
positive20_csv = open('prepared-spreadsheets/03_positive_testing.csv', 'w')

negative_csv = open('prepared-spreadsheets/04_negative.csv', 'w')
negative80_csv = open('prepared-spreadsheets/05_negative_training.csv', 'w')
negative20_csv = open('prepared-spreadsheets/06_negative_testing.csv', 'w')

train_csv = open('prepared-spreadsheets/07_train.csv', 'w')
test_csv = open('prepared-spreadsheets/08_test.csv', 'w')

lines = filtered_csv.readlines()
positiveLines = []
negativeLines = []

for line in lines:
    if line[0] == '1':
        positive_csv.write(line)
        positiveLines.append(line)
    else:
        negative_csv.write(line)
        negativeLines.append(line)


# Shuffle local arrays to add to test and training data
random.shuffle(positiveLines)
random.shuffle(negativeLines)

# Feed test and training positive file
llen = len(positiveLines)
min = llen * 0.8
for index in range(llen):
    if index < min:
        positive80_csv.write(positiveLines[index])
        train_csv.write(positiveLines[index])
    else:
        positive20_csv.write(positiveLines[index])
        test_csv.write(positiveLines[index])

# Feed test and training negative file
llen = len(negativeLines)
min = llen * 0.8
for index in range(llen):
    if index < min:
        negative80_csv.write(negativeLines[index])
        train_csv.write(negativeLines[index])
    else:
        negative20_csv.write(negativeLines[index])
        test_csv.write(negativeLines[index])

# Close all files
filtered_csv.close()
positive_csv.close()
positive80_csv.close()
positive20_csv.close()
negative_csv.close()
negative80_csv.close()
negative20_csv.close()
train_csv.close()
test_csv.close()
