import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10)
sin = np.sin(x)
tan = np.tan(x)
cos = np.cos(x)


plt.figure(figsize=(15,10))
plt.subplot(2,3,(1,2))
plt.plot(x,sin,color='blue')
plt.xlabel('x')
plt.ylabel('sinus')


plt.subplot(2,3,3)
plt.plot(x,cos,color='red')
plt.xlabel('x')
plt.ylabel('cosinus')
plt.grid=True


plt.subplot(2,3,(4,6))
plt.plot(x,tan,color='green')
plt.xlabel('x')
plt.ylabel('tan')

plt.savefig("figure.png")