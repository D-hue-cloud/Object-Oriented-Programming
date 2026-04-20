class Parrot:
    species="African Grey Parrot"

    def __init__(self,name,age):
        self.name=name
        self.age=age
Polly=Parrot("Polly",14)
Einstein=Parrot("Einstein", 36)

print("Polly is a {}".format(Polly.species))
print("Einstein is also a {}".format(Einstein.species))

print("{} is {} years old".format(Polly.name,Polly.age))
print("{} is {} years old".format(Einstein.name,Einstein.age))