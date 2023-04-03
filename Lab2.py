import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

bejaia = pd.read_csv('Bejaia_Region.csv', header=None, skipinitialspace=True, skiprows=1,
                     names = ['Day', 'Month', 'Year', 'Temperature', 'RH', 'Ws', 'Rain',
                              'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes'])
sidi = pd.read_csv('Sidi-Bel_Abbes_Region.csv', header = None, skipinitialspace = True, skiprows=1,
                   names = ['Day', 'Month', 'Year', 'Temperature', 'RH', 'Ws', 'Rain', 
                            'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes'])
print("Information about Bejaia_Region.csv")
bejaia.info()
print("Information about Sidi-Bel_Abbes_Region.csv")
sidi.info()
print("Statistic data about Bejaia_Region.csv")
print(bejaia.describe())
print("Statistic data about Sidi-Bel_Abbes_Region.csv")
print(sidi.describe())
print("Unique wind values in Bejaia_Region.csv")
print(bejaia['Ws'].unique())
print("Unique wind values in Sidi-Bel_Abbes_Region.csv")
print(sidi['Ws'].unique())
df1 = pd.DataFrame(bejaia)
df2 = pd.DataFrame(sidi)
print('Number of samples in Bejaia Region: ' + str(len(df1.index)))
print('Number of samples in Sidi-Bel Abbes Region: ' + str(len(df2.index)))
choice = input("Enter task number from 2 to 9 to print out specific graph: ")
if(choice == '2'):
    #Task Two
    plt.plot(df1.index, bejaia['Temperature'], color = 'blue', marker = 'o', linestyle = 'solid')
    plt.title('Temperature Change per Day in Bejaia Region')
    plt.xlabel('Per Day')
    plt.ylabel('Temperature in Celsius')
    plt.show()
if(choice == '3'):
    #Task Three
    plt.scatter(sidi['Temperature'], sidi['FWI'], color = 'green')
    plt.title('Relationship with Temperature and Fire Weather Index in Sidi-Bel Abbes Region')
    plt.xlabel('Temperature in Celsius')
    plt.ylabel('Fire Weather Index')
    plt.show()
if(choice == '4'):
    #Task Four
    totalJune = bejaia['RH'][bejaia['Month'] == 6]
    averageJune = 0
    for num in totalJune:
        averageJune += num
    averageJune /= len(totalJune)
    
    totalJuly = bejaia['RH'][bejaia['Month'] == 7]
    averageJuly = 0
    for num in totalJuly:
        averageJuly += num
    averageJuly /= len(totalJuly)
    
    totalAug = bejaia['RH'][bejaia['Month'] == 8]
    averageAug = 0
    for num in totalAug:
        averageAug += num
    averageAug /= len(totalAug)
    
    totalSept = bejaia['RH'][bejaia['Month'] == 9]
    averageSept = 0
    for num in totalSept:
        averageSept += num
    averageSept /= len(totalSept)
    
    plt.hist(averageJune, label = 'June')
    plt.hist(averageJuly, label = 'July')
    plt.hist(averageAug, label = 'August')
    plt.hist(averageSept, label = 'September')
    plt.xlabel('Average Humidity')
    plt.title('Average Humidity in Each Month in Bejaia Region')
    plt.legend(loc=9)
    plt.show()
if(choice == '5'):
    #Task Five
    totalJune = bejaia['Rain'][bejaia['Month'] == 6]
    averageJune = 0
    for num in totalJune:
        averageJune += num
    averageJune /= len(totalJune)
    
    totalJuly = bejaia['Rain'][bejaia['Month'] == 7]
    averageJuly = 0
    for num in totalJuly:
        averageJuly += num
    averageJuly /= len(totalJuly)
    
    totalAug = bejaia['Rain'][bejaia['Month'] == 8]
    averageAug = 0
    for num in totalAug:
        averageAug += num
    averageAug /= len(totalAug)
    
    totalSept = bejaia['Rain'][bejaia['Month'] == 9]
    averageSept = 0
    for num in totalSept:
        averageSept += num
    averageSept /= len(totalSept)
    
    rainAverages = [averageJune, averageJuly, averageAug, averageSept]
    months = ['June', 'July', 'August', 'September']
    plt.bar(range(len(months)), rainAverages)
    plt.xticks(range(len(months)), months)
    plt.xlabel('Months')
    plt.ylabel('Average Rainfall')
    plt.title('Average Rainfall per Month in Bejaia Region')
    plt.show()
if(choice == '6'):
    #Task Six
    sidi['Ws'][sidi['Month'] == 6].hist(bins=5)
    plt.title('Average Wind Speeds throughout Month of June 2012 in Sidi-Bel Abbes Region Region')
    plt.xlabel('Average Wind Speed')
    plt.ylabel('Number of Days')
    plt.show()
if(choice == '7'):
    #Task Seven
    tempTemperature = sidi['Temperature'][sidi['Month'] == 7]
    temperatureSorted = sorted(tempTemperature)
    tempHumidity = sidi['RH'][sidi['Month'] == 7]
    humiditySorted = sorted(tempHumidity)
    plt.plot(temperatureSorted, humiditySorted, color = 'red', marker = 'o')
    plt.xlabel('Temperature in Celsius')
    plt.ylabel('Relative Humidity')
    plt.title('Comparison Between Temperature and Relative Humidity in Sidi-Bel Abbes Region in July 2012')
if(choice == '8'):
    #Task Eight
    data = Counter(min(point // 10 * 10, 90) for point in bejaia['RH'])
    plt.bar([x for x in data.keys()], data.values(), 5)
    plt.axis([0, 100, 0, 40])
    plt.xticks([10 * i for i in range(11)])
    plt.xlabel('Decile')
    plt.ylabel('Number of Days')
    plt.title('Distribution of Relative Humidity in Bejaia Region')
    plt.show()
if(choice == '9'):
    #Task Nine
    print('In Progress')
    '''
    juneTemp = bejaia['Temperature'][bejaia['Month'] == 6]
    print(juneTemp)
    juneNoFire = bejaia['Temperature'][bejaia['Classes'] == 'not fire']
    print(juneNoFire)
    juneNoFireAverage = 0
    if(juneTemp.key() == juneNoFire.key()):
        juneNoFireAverage = juneTemp.values()
    juneNoFireAverage /= len(juneNoFire) 
    print(juneNoFireAverage)
    '''
    
    
    
    
    
    
    
    
    
    