from YarpTp import YarpTp
from time import sleep

car = YarpTp()

print("2 segundos")
car.Forward(tm=2.0)

print("velocidad 10")
car.Forward(speed=10)
sleep(2)

print("velocidad 30")
car.Forward(speed=30)
sleep(2)

print("velocidad 50")
car.Forward(speed=50)
sleep(2)

print("velocidad 70")
car.Forward(speed=70)
sleep(2)

print("velocidad 100")
car.Forward(speed=100)
sleep(2)

car.Stop()
car.GoodBye()