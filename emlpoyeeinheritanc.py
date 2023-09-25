class employee:
    def __int__(self,name,empID):
        self.name=name
        self.empID=empID
    def setdata(self):
        self.name=input("enter employee name:\n")
        self.empID=int(input("enter employee ID:\n"))
    
class salary(employee):
    def __int__(self,basicsalary,netsalary,da,ta,hra,esi,pf):
        self.basicsalary=basicsalary
        self.netsalary=netsalary
        self.da=da
        self.ta=ta
        self.hra=hra
        self.esi=esi
        self.pf=pf
    def setsalaryes(self):
        self.basicsalary=int(input("enter salary:\n"))
        self.pf=self.basicsalary*2/100
        self.ta=self.basicsalary*3/100
        self.da=self.basicsalary*4/100
        self.esi=self.basicsalary*5/100
        self.hra=self.basicsalary*1.5/100
        self.netsalary = self.basicsalary+self.da+self.ta+self.hra-(self.esi+self.pf)
    def show(self):
        print("employee name={}".format(self.name))
        print("employee ID={0}".format(self.empID))
        print("salary={0}".format(self.basicsalary))
        print("net-salary={0}".format(self.netsalary))
ma=salary()
ma.setdata()
ma.setsalaryes()
ma.show()


        


        