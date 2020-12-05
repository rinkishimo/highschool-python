def bmi(m, h):
    return m / pow(h, 2)

print()
print('===== BMI =====')
h = float(input('Zadaj svoju hmotnost [kg]: '))
v = float(input('Zadaj svoju vysku [cm]: ')) / 100
index = round(bmi(h, v), 2)

print('Tvoje BMI je ' + str(index) )
print()