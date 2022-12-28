PI = 3.14

def calculateSurfaceAreaOfSphere(radius):
    return 4 * PI * (radius ** 2)

def calculateVolumeOfSphere(radius):
    return (4 / 3) * PI * (radius ** 3)

radius = float(input("Enter radius "))
surfaceArea = calculateSurfaceAreaOfSphere(radius)
volume = calculateVolumeOfSphere(radius)
print(f"SurfaceArea = {surfaceArea} Volume = {volume}")
