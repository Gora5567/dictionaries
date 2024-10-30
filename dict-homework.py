from helpers import *


def task1():
    person = {
        "name": "Иван",
        "age": 30,
        "city": "Киев"
    }
    print(person["name"])


def task2():
    computer = {
        "processor": "AMD Ryzen 5 5600X",
        "ram": "32GB",
        "storage": "1TB SSD",
        "gpu": "NVIDIA GeForce RTX 3060",
        "os": "Ubuntu 20.04"
    }
    print(computer)


for f in {task1, task2}:
    run(f)
