class mobile1:
    def dp(self):
        print("inside display 3")


class mobile2(mobile1):
    def dp(self):
        print("inside display 4")


class mobile3(mobile1):
    def dp(self):
        print("inside display 5")


m3 = mobile3()
m3.dp()
