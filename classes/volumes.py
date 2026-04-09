radius = int(input())
cube_volume = radius ** 3
sphere_volume = 4/3 * 3.1415 * radius ** 3

difference = cube_volume - sphere_volume
approximation = f'{difference:.3f}'