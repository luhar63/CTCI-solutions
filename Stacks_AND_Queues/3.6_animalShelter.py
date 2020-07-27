"""
Animal Shelter
"""


"""
I have not used linked list. (just python list)

Time Complexity: O(N)
Space Complexity: O(N)
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def setOrder(self, order=0):
        self.order = order

    def getOrder(self):
        return self.order

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class AnimalQueue:
    def __init__(self):
        self.dogQueue = []
        self.catQueue = []
        self.order = 0

    def enqueue(self, animal):
        animal.setOrder(self.order)
        self.order += 1
        if isinstance(animal, Dog):
            self.dogQueue.append(animal)
        else:
            self.catQueue.append(animal)

    def dequeueAny(self):
        dog = self.dogQueue[0]
        cat = self.catQueue[0]

        if cat.getOrder() < dog.getOrder():
            return self.catQueue.pop(0)
        else:
            return self.dogQueue.pop(0)

    def dequeueDogs(self):
        return self.dogQueue.pop(0)

    def dequeueCats(self):
        return self.catQueue.pop(0)


# driver function
if __name__ == "__main__":
    aq = AnimalQueue()
    aq.enqueue(Cat("Katty"))
    aq.enqueue(Dog("Android"))
    aq.enqueue(Cat("Leslie"))
    aq.enqueue(Dog("Chappy"))
    aq.enqueue(Dog("Bruno"))
    print(aq.dequeueAny())
    print(aq.dequeueCats())
    print(aq.dequeueDogs())
