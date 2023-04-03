import matplotlib.pyplot as plt

wordCounts = {}
with open('SciencePaper.txt', 'r', errors = 'ignore') as file:
    for line in file:
        newWord = line.upper().replace(',', '').replace('-', '').replace(':', '')\
        .replace(';', '').replace('(', '').replace(')', '').replace('/', '')\
        .replace('!', '').replace('?', '').replace('.', '').split()
        for word in newWord:
            try:
                wordCounts[word] += 1
            except:
                wordCounts[word] = 1
sortedWordCounts = sorted(wordCounts.items(), key = lambda x:x[1], reverse = True)
dictionaryCount = len(sortedWordCounts)
print('Number of different words in article: ' + str(dictionaryCount))
print('\n')
print('The 10 words which appear the most frequently: ')
i = 0
while(i < 10):
    print(sortedWordCounts[i])
    i += 1
print('\n')
print('Number of times the word "Summerfelt" appears: ' + str(wordCounts['SUMMERFELT']))
print('Number of times the word "wastewater" appears: ' + str(wordCounts['WASTEWATER']))
print('Number of times the word "greenhouse" appears: ' + str(wordCounts['GREENHOUSE']))
print('Number of times the word "salmon" appears: ' + str(wordCounts['SALMON']))
print('\n')
print('Words which appeared once: ')
for key, value in wordCounts.items():
    if(value == 1):
        print(key, end = ' ')
print('\n')
print('Words which appeared twice: ')
for key, value in wordCounts.items():
    if(value == 2):
        print(key, end = ' ')
print('\n')
print('Words which appeared five times: ')
for key, value in wordCounts.items():
    if(value == 5):
        print(key, end = ' ')
print('\n')
print('Words which appeared ten times: ')
for key, value in wordCounts.items():
    if(value == 10):
        print(key, end = ' ')
print('\n')
reverseWordCounts = {}
for word,count in wordCounts.items():
    try:
        reverseWordCounts[count].append(word)
    except:
       reverseWordCounts[count] = [word]
x = list(reverseWordCounts.keys())
y = [sum([len(word) for word in value]) / len(value) for value in reverseWordCounts.values()]
plt.bar(x,y)
plt.xlabel('Appearance Frequency')
plt.ylabel('Average Length of Words')
print('Bar graph printed')
        
        
        
        
        
        
        
        
        
        
        
        