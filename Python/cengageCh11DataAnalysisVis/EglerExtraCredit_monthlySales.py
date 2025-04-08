import matplotlib.pyplot as plt
import stats

months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']
sales = [10050, 12000, 22000, 20000, 25000, 30000, 28000, 32000, 35000, 31000, 29000, 33000]


# create a line plot
def linePlot():
    xValues = list(range(1,13))
    plt.plot(xValues, sales, color = "blue", marker = 'o', mfc='red')
    plt.xticks(xValues)
    plt.title("Line plot of sales")
    plt.xlabel("Months")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.show()



# create a bar plot
def barPlot():
    colors = ['blue', 'green']
    plt.bar(months, sales, width=0.2, color=colors)
    plt.title("Months and Sales")
    plt.xlabel("months")
    plt.ylabel("sales")
    plt.show()



# create a scatter plot
def scatterPlot():
    positions = list(range(1, 13))
    
    plt.scatter(positions, sales, color = 'purple', marker = '.')
    plt.title("Scatter Plot")
    plt.xlabel("Position")
    plt.ylabel("Sales")
    plt.show()




def main():
    print("Choose a type of plot:")
    print("1. Line Plot")
    print("2. Bar Plot")
    print("3. Scatter Plot")

    userInput = int(input("Enter your choice: "))

    while userInput < 1 or userInput > 3:
        print("Invalid Entry")
        userInput = int(input("Enter your choice: "))

    if userInput == 1:
        linePlot()
    elif userInput == 2:
        barPlot()
    elif userInput == 3:
        scatterPlot()


if __name__ == '__main__':
    main()