from matplotlib import pyplot as plt
"""
this is second trial
this is written in the nano unix editor 
simple  plot
"""

year = [1990,2000, 2009,2013,2015,2017]
gdp = [12,33,45,56,76,88]
# plt.plot (year,gdp, marker = 'o', linestyle='dashed')
# plt.xlabel("year")
# plt.ylabel("gdp")
# plt.title("gdp across year")
 plt.show()


"""
bar chart
"""

movies = ["Annie","pandas","Ben-Hur","Casablanca","Gandhi"]
num_oscars = [5,11,3,8,10]


# bars are by default width 0.8, so we'll add 0.1 to the left 
#coordinates 
# so that each bar is centered

xs = [index for index,_ in enumerate(movies)]


#plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xs,num_oscars)
plt.title("Oscar Wards Numbers")
plt.ylabel("numbers of awards")
plt.xticks([i for i,_ in enumerate(movies)], movies)
plt.show()
