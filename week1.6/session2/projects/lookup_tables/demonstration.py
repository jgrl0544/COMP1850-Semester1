from image import Image
from LUT import InverterLUT

inverter = InverterLUT(16)
image = Image.read("/workspaces/COMP1850-Semester1/week1.6/session2/images/feep.pgm")
inverter.apply(image).write_pgm("/workspaces/COMP1850-Semester1/week1.6/session2/images/feepInverted.pgm")

inverter = InverterLUT(255)
image = Image.create(10, 10, 50, 255)
inverter.apply(image).write_pgm("/workspaces/COMP1850-Semester1/week1.6/session2/images/invertDemonstration.pgm")
image.write_pgm("/workspaces/COMP1850-Semester1/week1.6/session2/images/invertDemonstrationNormal.pgm")
