class mobile1:
    def dp(self):
        print("inside display 4")


class mobile2(mobile1):
    def bc(self):
        print("inside back camera 15mp")
    def dp(self):
        super().dp()
        print("inside display 4")


class mobile3(mobile2):
    def fc(self):
        print("inside front camera 10mp")
    def dp(self):
        super().dp()
        print("inside display 5")


m3 = mobile3()
m3.fc()
m3.bc()
m3.dp()
print("----------")
m2 = mobile2()
m2.dp()
m2.bc()
print("--------")
m1 = mobile1()
m1.dp()

