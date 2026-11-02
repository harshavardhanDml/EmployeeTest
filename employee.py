employees = {}
n = int(input("Enter the number of employees: "))
for n in range(n):
  name = input("Enter employee name: ")
  phone = input("Enter phone number: ")
  id=int(input("Enter id"))
  employees[name] = phone
  employees[name]=id

print("\n--- All Employees ---")
for name, phone,id in employees.items():
  print(f"Name: {name} | Phone: {phone}|id:{id}")
