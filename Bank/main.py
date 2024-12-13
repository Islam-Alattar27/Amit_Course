from Bank import Bank 

b = Bank()

b.register("Islam", "123")
b.register("Eman", "321")

b.login("Islam", "123")
b.deposit("Islam",7000)
b.withdraw("Islam",2000)

b.info()