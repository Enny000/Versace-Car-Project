import pandas as pd
import matplotlib.pyplot as plt


def main_menu():
    flag = True

    while flag:

        print("#################################################")
        print("############## Versere Cars Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Total Sales Analysis")
        print("### 2. New car sales ")
        print("### 3. Used car sales")
        print("### 4. Sales by person")
        print("### 5. Exit")

        choice = input('Enter your number selection here: ')

        try:
            response = int(choice)
            if response < 1 or response > 5:
                raise ValueError()
        except ValueError:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    return choice

def total_menu ():
    flag = True

    while flag:

        print("#################################################")
        print("############## Total Sales ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. All sales by model")   
        print("### 2. Custom selection") 
        print("### 3. Go Back")

        choice = input('Enter your number selection here: ')

        try:
            response = int(choice)
            if response < 1 or response > 2:
                raise ValueError()
        except ValueError:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False
    return choice      

def convert_total_menu_coice(total_menu_choice):
    
    if total_menu_choice == "1":
        total_choice = "All"
    elif total_menu_choice == "2":
        total_choice = "Model"
    else:
        return
    
    return total_choice

def get_total_data(total_choice):
    
    df = pd.read_csv("Task4a_data (2).csv")

    if total_choice == "All":
        extract = df.groupby(['Date','Car Model'], sort=True)['Value'].sum()
        total = df['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    else:
        flag = True

        while flag:

            print("########### Please select a model #############")
            print("### 1. Ranger")
            print("### 2. Model D Premium Plus")
            print("### 3. Compass")
            print("### 4. Mercury")
            print("### 5. Outback")
            print("### 6. Go Back")
            
            choice = input('Enter your number selection here: ')

            try:
                choice = int(choice)
                if choice < 1 or choice > 6:
                    raise ValueError()
            except ValueError:
                print("Sorry, you did not enter a valid option")
                flag = True
            else:    
                print('Choice accepted!')
                flag = False

        if choice == 6:
            return
        
        models = ["Ranger", "Model D Premium Plus", "Compass", "Mercury", "Outback"]   

        custom_choice = models[choice -1]

        extract = df.loc[df['Car Model'] == custom_choice]
        total = extract['Value'].sum()
        print("The total value of sales for your selection is {}".format(total))

    return extract


def new_car_sales():
    df = pd.read_csv("Task4a_data (2).csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    new_cars = df.loc[df['New/Used'] == "New"]
    new_cars = new_cars.groupby('Date')['Value'].sum().reset_index()

    # you may want to practice this with a few more csvs
    plt.figure(figsize=(10, 6))
    plt.bar(new_cars['Date'], new_cars['Value'])
    plt.title("New Car Sales VS Time")
    plt.xlabel("Date")
    plt.ylabel("Sales (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    
    print(new_cars)

def used_car_sales():
    df = pd.read_csv("Task4a_data (2).csv")
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    used_cars = df.loc[df['New/Used'] == "Used"]
    used_cars = used_cars.groupby('Date')['Value'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.bar(used_cars['Date'], used_cars['Value'])
    plt.title("Used Car Sales VS Time")
    plt.xlabel("Date")
    plt.ylabel("Sales (£)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    print(used_cars)

def diffrent_salesperson():
    flag = True
    
    while flag:
        print("########### Please select a Salesperson #############")
        print("### 1. Christopher Clark")
        print("### 2. Michael Garcia")
        print("### 3. Sarah Jones")
        print("### 4. David Johnson")
        print("### 5. Go Back")
        
        choice = input('Enter your number selection here: ')

        try:
            choice = int(choice)
            if choice < 1 or choice > 5:
                raise ValueError()
        except ValueError:
            print("Sorry, you did not enter a valid option")
            flag = True
        else:    
            print('Choice accepted!')
            flag = False

    if choice == 5:
        return

    employees = ["Christopher Clark", "Michael Garcia", "Sarah Jones", "David Johnson"]   

    custom_employees = employees[choice -1]

    df = pd.read_csv("Task4a_data (2).csv") 

    extract = df.loc[df['Salesperson'] == custom_employees]
    total = extract['Value' : 'Salesperson'].sum()
    print(extract , total)
        

def main():
    while True:
        main_menu_choice = main_menu()

        if main_menu_choice == "1":
            total_menu_choice = total_menu()
            total_choice = convert_total_menu_coice(total_menu_choice)
            if not total_choice:
                continue
            print(get_total_data(total_choice))
        elif main_menu_choice == "2":
            new_car_sales()
        elif main_menu_choice == "3":
            used_car_sales()
        elif main_menu_choice == "4":
            diffrent_salesperson()
        elif main_menu_choice == "5":
            break
        else:
            print("Invalid selection")


if __name__ == "__main__":
    main()