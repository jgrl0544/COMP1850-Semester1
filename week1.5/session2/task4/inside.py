# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry
circle = geometry.Circle(10)
insidePoint = geometry.Point(3,4)
outsidePoint = geometry.Point(6,7)

print(circle.__contains__(insidePoint))
print(circle.__contains__(outsidePoint))