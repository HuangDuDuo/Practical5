#No show!!
Lan = {'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5}
print (Lan)
import matplotlib
import matplotlib.pyplot as plt
language = list(Lan.keys())
values = list(Lan.values())
plt.bar(language,values)
plt.title('Programming language popularity')
plt.xlabel('Language')
plt.ylabel('Users (percentage)')
plt.show()
a = input("Input language:")
print ("The percentage of developers who use", a, "is", Lan[a], ".")
