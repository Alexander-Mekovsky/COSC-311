import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math

def mean(x):
    """calculate and return the mean of a numpy array"""
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return sum/len(x)

def median(x):
    """return the 'middle value' of the array x after sorting"""
    tmp = sorted(x)
    # use // for integer division (i.e. round down)
    return tmp[len(x) // 2] if len(x) % 2 == 1 else (tmp[len(x) // 2] + tmp[(len(x) // 2)-1]) / 2

def quantile(xs, q):
    """generalize the median to the q-percent quantile -- q is a float in range (0,1)"""
    tmp = sorted(xs)
    return tmp[ int(len(tmp) * q) ]

def center(xs):
    return np.array([x - mean(xs) for x in xs])

def var(xs):
    """return variance of x -- the average squared distance from the mean"""
    return mean([x**2 for x in center(xs)])
    # return sum([x**2 for x in center(xs)])/(len(xs) - 1)
    
def std(xs):
    return math.sqrt(var(xs))

def cov(xs, ys):
    """Take two lists of observations and compute their covariance"""
    assert len(xs) == len(ys)
    cx = center(xs)
    cy = center(ys)
    return mean([cx[i]*cy[i] for i in range(len(cx))])

def correlation(xs, ys):
    """Calculate the (Pearson) correlation coefficient"""
    return cov(xs,ys)/(std(xs)*std(ys))

#not fire = 0, fire = 1
bejaia = pd.read_csv('Bejaia_Region.csv', header=None, skipinitialspace=True, skiprows=1,
                     names = ['Day', 'Month', 'Year', 'Temperature', 'RH', 'Ws', 'Rain',
                              'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes'])
sidi = pd.read_csv('Sidi-Bel_Abbes_Region.csv', header = None, skipinitialspace = True, skiprows=1,
                   names = ['Day', 'Month', 'Year', 'Temperature', 'RH', 'Ws', 'Rain', 
                            'FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'Classes'])

choice = int(input("Input Lab Task Number: "))
while(choice > 0 | choice < 6):
    choice = int(input("Invalid input value. Please try again."))
    
if(choice == 1):
    tempNoFire = mean(list(filter(None, bejaia['Temperature'][bejaia['Classes'] == 0])))
    tempFire = mean(list(filter(None, bejaia['Temperature'][bejaia['Classes'] == 1])))
    humidNoFire = mean(list(filter(None, bejaia['RH'][bejaia['Classes'] == 0])))
    humidFire = mean(list(filter(None, bejaia['RH'][bejaia['Classes'] == 1])))
    windNoFire = mean(list(filter(None, bejaia['Ws'][bejaia['Classes'] == 0])))
    windFire = mean(list(filter(None, bejaia['Ws'][bejaia['Classes'] == 1])))
    rainNoFire = mean(list(filter(None, bejaia['Rain'][bejaia['Classes'] == 0])))
    rainFire = mean(list(filter(None, bejaia['Rain'][bejaia['Classes'] == 1])))
    print('Mean Temperature with no fire: ' + str(tempNoFire))
    print('Mean Temperature with fire: ' + str(tempFire))
    print('Mean Humidity with no fire: ' + str(humidNoFire))
    print('Mean Humidity with fire: ' + str(humidFire))
    print('Mean Wind with no fire: ' + str(windNoFire))
    print('Mean Wind with fire: ' + str(windFire))
    print('Mean Rain with no fire: ' + str(rainNoFire))
    print('Mean Rain with fire: ' + str(rainFire))
    attributes = {'Temperature With No Fire':tempNoFire, 'Temperature With Fire':tempFire, 'Humidity With No Fire':humidNoFire, 'Humidity With Fire':humidFire, 'Wind With No Fire':windNoFire, 'Wind With Fire':windFire, 'Rain With No Fire':rainNoFire, 'Rain With Fire':rainFire}
    plt.barh(list(attributes.keys()), list(attributes.values()))
    
elif(choice == 2):
    medFFMC = median(sidi['FFMC'])
    medDMC = median(sidi['DMC'])
    medDC = median(sidi['DC'])
    medISI = median(sidi['ISI'])
    print('Median value of FFMC: ' + str(medFFMC) + ', Median value of DMC: ' + str(medDMC) + ', Median Value of DC:' + str(medDC) + ', Median Value of ISI: ' + str(medISI))
    
elif(choice == 3):
    tempQuartile = (quantile(bejaia['Temperature'], 0.25), quantile(bejaia['Temperature'], 0.6), quantile(bejaia['Temperature'], 0.75))
    humidQuartile = (quantile(bejaia['RH'], 0.25), quantile(bejaia['RH'], 0.6), quantile(bejaia['RH'], 0.75))
    windQuartile = (quantile(bejaia['Ws'], 0.25), quantile(bejaia['Ws'], 0.6), quantile(bejaia['Ws'], 0.75))
    rainQuartile = (quantile(bejaia['Rain'], 0.25), quantile(bejaia['Rain'], 0.6), quantile(bejaia['Rain'], 0.75))
    print('Temperature: ' + str(tempQuartile) + ', Relative Humidity: ' + str(humidQuartile) + ', Wind: ' + str(windQuartile) + ', Rain: ' + str(rainQuartile))
    
elif(choice == 4):
    tempSD = std(sidi['Temperature'])
    tempSD = format(tempSD, '.5f')
    rainSD = std(sidi['Rain'])
    rainSD = format(rainSD, '.5f')
    buiSD = std(sidi['BUI'])
    buiSD = format(buiSD, '.5f')
    fwiSD = std(sidi['FWI'])
    fwiSD = format(fwiSD, '.5f')
    print('Temperature: ' + str(tempSD) + ', Rain: ' + str(rainSD) + ', BUI: ' + str(buiSD) + ', FWI: ' + str(fwiSD))
    
elif(choice == 5):
    tempCor = correlation(bejaia['RH'], bejaia['Temperature']) #Smallest negative correlation
    windCor = correlation(bejaia['RH'], bejaia['Ws'])
    rainCor = correlation(bejaia['RH'], bejaia['Rain']) #Largest positive correlation
    ffmcCor = correlation(bejaia['RH'], bejaia['FFMC'])
    dmcCor = correlation(bejaia['RH'], bejaia['DMC'])
    dcCor = correlation(bejaia['RH'], bejaia['DC'])
    isiCor = correlation(bejaia['RH'], bejaia['ISI'])
    buiCor = correlation(bejaia['RH'], bejaia['BUI'])
    fwiCor = correlation(bejaia['RH'], bejaia['FWI'])
    print('Temperature: ' + str(tempCor) + ', Wind: ' + str(windCor) + ', Rain: ' + str(rainCor) + ', FFMC: ' + str(ffmcCor) + ', DMC: ' + str(dmcCor))
    print('DC: ' + str(dcCor) + ', ISI: ' + str(isiCor) + ', BUI: ' + str(buiCor) + ', FWI: ' + str(fwiCor))
    
    
    
    
    
    
    
    
    
    
    