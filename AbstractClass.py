from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def roi(self):
        pass
class SBI(Bank):
    def roi(self):
        print("The rate of interest in SBI is 10%")
class CanaraBank(Bank):
    def roi(self):
        print("The rate of interest in Canara is 11%")

sbi=SBI()
canara=CanaraBank()
sbi.roi()
canara.roi()

