# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry
circle = geometry.Circle(10)
insidePoint = geometry.Point(3,4)
outsidePoint = geometry.Point(15,15)

print(insidePoint in circle)
print(outsidePoint in circle)