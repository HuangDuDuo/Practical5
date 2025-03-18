
uk_countries = [57.11,3.13,1.91,5.45]
China_provinces = [65.77,41.88,45.28,61.27,85.15]
import matplotlib.pyplot as plt
labels1 = 'England', 'Wales', 'Northern Ireland', 'Scotland'
sizes = list(uk_countries)
plt.title('Population sizes of UK countries')
plt.pie(sizes,labels=labels1, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()

labels2 = 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'
sizes = list(China_provinces)
plt.title('Population sizes of China provinces')
plt.pie(sizes,labels=labels2, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()