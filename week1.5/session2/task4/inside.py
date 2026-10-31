# Week 1.5, Session 2: Task 4

# Add a program here that demonstrates use of the __contains__()
# method that you implemented in the Circle class
import geometry
circle = geometry.Circle(10)
insidePoint = geometry.Point(3,4)
<<<<<<< HEAD
outsidePoint = geometry.Point(6,7)

print(circle.__contains__(insidePoint))
print(circle.__contains__(outsidePoint))
=======
outsidePoint = geometry.Point(15,15)

print(insidePoint in circle)
print(outsidePoint in circle)
>>>>>>> fc6179bab88ac50d107a4c4a74e7f4ac7ea5ea67
