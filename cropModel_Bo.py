

import random
import pylab as plt
class hectareCrop(object):
    '''Used to project yearly yield for a crop based on fertilizer and rainfall 
    inputs.
    '''
    def __init__(self, NFert, irrigation):
        
        self.NFert = NFert
        self.irrigation = irrigation
        #pass
        
    def rainfall(self):
        '''returns an annual rainfall amount based on normal probability distribution.
        Average rainfall during growth period is 50 cm and a standard deviation of 20 cm 
        return self.rainAmt
        '''
        mu, sigma = 50, 20
        rainAmt = random.gauss(mu,sigma)
        self.rainAmt = rainAmt
        return self.rainAmt
        #pass
        
    def Nloss(self):
        '''Loss of N based on amount of rainfall that occurred.  For every cm of rain,
        3.0% loss of N occurs.
        Runs self.rainfall() to get self.rainAmt, returns an int of NAmt remaining based
        on yearly rainfall.  Int returned is not a object variable and does not replace
        self.NAmt
        '''
        self.rainfall()
        NAmt = self.NFert - 0.0003 * self.rainAmt * self.NFert
        self.NAmt = int(NAmt)
        return self.NAmt
        
        #pass
       
        
    def cropYield(self):
        '''Predicts the yearly yield of a crop based on rainfall and fertilizer
        inputs.
        Average yield is 100 bushels per acre based on average rainfall and 200 kg/ha
        per year N fertility.  A very basic model was used to predict yield where
        yield = rainAmt + (0.25 * N amt in kg/ha).  Need to use NAmt after rainfall
        for calcualtion.  
        RETURN: self.yearYield wich is the yield in bushels per acre
        '''
        
        yearYield = self.rainfall() + (0.25 * self.Nloss())
        self.yearYield = yearYield
        return self.yearYield
        
        #pass
        
    def profit(self):
        '''Assume $7 dollar per bushel yield.  However, a loss of $10 for each cm below 
        50 cm.  If irrigation is True, rainfall is supplemented up to 50 cm if it is 
        below.  If rainfall is 50 cm or greater, no additional irrigation takes
        place.
        RETURN grossProfit, not an object attribute
    
        '''
        self.cropYield()
        if self.rainAmt < 50:
                grossProfit = self.yearYield * 7 - (50 - self.rainAmt) * 10
        else:
                grossProfit = self.yearYield * 7               
        return grossProfit

def modelYield(NFert, Irrigation= False, cycles = 10000):
    '''Model yield for 10,000 iterations and plot the yield in a histogram.
    '''
    crop0 = hectareCrop(NFert,False)
    i = 0
    yearYields = []
    while i <=cycles:
        crop0.cropYield()
        yearYields.append(crop0.yearYield) 
        i+=1
    plt.hist(yearYields)
    #pass
#modelYield(200)
 
def modelProfit(NFert, cycles=10000):
    '''Model profit for 10,000 iterations for both irrigated and non-irrigated.
    Plot the predictions in four (2x2) subplot windows - histogram and boxplot for
    each of the data sets.
    '''
    #pass
    yrprofit1 = []
    for x in range(10000):
        crop1 = hectareCrop(NFert, True)
        yrprofit1.append(crop1.profit())
    
    yrprofit2 = []
    for y in range(10000):
        crop2 = hectareCrop(NFert, False)
        yrprofit2.append(crop2.profit())
   
    plt.subplot(2,2,1)
    plt.title('Irrigated')    
    plt.hist(yrprofit1)
    plt.subplot(2,2,3)
    plt.boxplot(yrprofit1, 0, '')
    plt.subplot(2,2,2)
    plt.title('\nNon-Irrigated')    
    plt.hist(yrprofit2)
    
    plt.subplot(2,2,4)
    plt.boxplot(yrprofit2, 0, '')
    
    plt.show()
#Uncomment to run

modelProfit(200)
#Uncomment to run
random.seed(1)
print("Unit Test 1") 
crop1 = hectareCrop(200, False) 
money = crop1.profit() 
print money #answer is 783.29
print crop1.yearYield #answer is 111.899
print crop1.rainAmt #answer 62.149
print crop1.NFert #answer is 200
print crop1.irrigation #answer is False

print crop1.NAmt
# 
# 
print("Unit Test 2")
crop2 = hectareCrop(100, True) 
money = crop2.profit()
print money #521.258
print crop2.yearYield #74.465
print crop2.rainAmt #49.715
print crop2.NFert #100
print crop2.irrigation #True
# 
print crop2.NAmt

