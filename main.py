class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Robot.population += 1

    def __del__(self):
        print('{0} уничтожается!'.format(self.name))

        Robot.population -= 1
        if Robot.population == 0:
            print('{0} был последным.'.format(self.name))
        else:
            print('Осталось {0:d} Работаюших роботов.'.format(
                Robot.population))

    def SayHi(self):
        print('hello my creator {0}'.format(self.name))

    def HowMany():
        print('у нас {0:d} роботов.'.format(Robot.population))
    HowMany = staticmethod(HowMany)


droid1 = Robot('R2-D2')
droid1.SayHi()
Robot.HowMany()
droid2 = Robot('C-3PO')
droid2.SayHi()
Robot.HowMany()
print("\nЗдесь роботы могут проделать какую-то работу.\n")
print("Роботы закончили свою работу. Давайте уничтожим их.")
del droid1
del droid2
