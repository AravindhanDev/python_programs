def calculateMomentum(m, c):
    return m * (c ** 2)

mass = float(input("Enter mass of the object: "))
velocity = float(input("Enter velocity of the object: "))
momentum = calculateMomentum(mass, velocity)
print(momentum)
