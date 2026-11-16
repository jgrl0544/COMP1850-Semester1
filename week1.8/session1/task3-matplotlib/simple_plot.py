
import matplotlib.pyplot as plt  # import library

x = [ k for k in range(1000) ]  # create a range for the data
#y = [ k*k for k in x ]      # create a simple function y=x^2

y = [k for k in x]
#y = [(1/(k+1)) for k in x]

plt.xkcd()

smile = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,1,0,0,0],
    [0,0,0,1,1,1,1,1,0,0,0]
]

plt.imshow(smile)

#plt.plot(x,y)  # create a 2d plot



plt.xlabel('x')
plt.ylabel('y=x')  # annotate

plt.title("This is a title.")
plt.show()  # display

# Test the example as is on the slides
# - Modify the data and the range
# - Plot in different ways
# Read matplotlib documentation
# - Test some other plotting functions
