import employee

def main():
    empName = input("Enter the new employee name >> ")
    empID = input("Enter the employee ID >> ")
    empShift = input("Enter the shift number (1 for day, 2 for night) >> ")
    empPay = float(input("Enter the employee pay >> "))

    prodWorker = employee.ProductionWorker(empName, empID, 
                                           empShift, empPay)
    
    print(prodWorker)


if __name__ == "__main__":
    main()