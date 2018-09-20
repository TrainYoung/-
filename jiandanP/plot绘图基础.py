from matplotlib import pyplot as plt

paramx = [1,2,3,4]
paramy = [1,4,9,16]

#plt.axis('equal')
plt.axis([0, 5, 0, 20])
plt.plot(paramx,paramy)
plt.show()