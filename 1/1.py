import matplotlib.pyplot as pyplot

year=[2010,2011,2012,2013,2014,2015,2016]
rice=[10,30,50,30,40,42,5]

pyplot.xlabel("Years")
pyplot.ylabel("Rice Production")
pyplot.title("Rice Production by Year")
pyplot.plot(year,rice)
pyplot.show()
