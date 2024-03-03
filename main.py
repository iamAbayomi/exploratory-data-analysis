#This program is built to analyse and visualise datasets
#ID: A00316019
from  module.user_functions import *


# Variables Declaration
lowest_value = 0
highest_value = 0
highest_total_average = 0
lowest_total_average = 0

# Note: For box plots, we need to collect values of each category into a list
numerical_col1_list = []
numerical_col2_list = []
categorical_list = []
categorical_values_dict = {}
categorical_values_total = {}
categorical_values_count = {}

heading = []



def readfile():
    filename = input("\n Please input the csv file directory or enter [d] to default file: ")

    if filename == "d":
        filename = "credit_card.csv"

    try:
        #opening the file
        with open(filename, encoding="utf-8", errors="ignore") as data_file:
            heading = data_file.readline().strip().split(',')
        
            print("\nThese are the indexes and columns of the file below. Select two" +
                " numerical columns and one categorical column to perform analysis on. \n")
        
            print("INDEX  COLUMNS")
            for header in heading:
                print(heading.index(header), " " , header)

            num1_index = int(input("Enter the index of the first numerical column: "))
            num2_index = int(input("Enter the index of the second numerical column: "))
            categorical_index = int(input("Enter the index of the categorical column: "))

            cis = ''
            num_var = input("\nSelect one of the numerical variable category you selected earlier to "+ 
                            " perform analysis with the sub category? \n"+
                                " [1] "+ heading[num1_index] + " [2] " + heading[num2_index]  + "? ")
            
            if int(num_var) == 1:
                num_var = num1_index
            else:
                num_var = num2_index    

            # processing subsequent lines
            for line in data_file:
                fields = line.strip().split(",")

             
                num1= int(fields[num1_index])
                num2 =int(fields[num2_index])
                category = fields[categorical_index]

                numerical_col1_list.append(num1)
                numerical_col2_list.append(num2)


                

            
                
                if category not in categorical_list: categorical_list.append(category)


                categorical_values_dict.setdefault(category, []).append(int(fields[num_var]))
                categorical_values_count[category] = categorical_values_count.get(category, 0) + 1
                categorical_values_total[category] = categorical_values_total.get(category,0) + int(num_var)

            

            highest_number = max(categorical_values_count, key=categorical_values_count.get)
            lowest_number = min(categorical_values_count, key=categorical_values_count.get)
            lowest_value =  min(categorical_values_total, key=categorical_values_total.get)
            highest_value = max(categorical_values_total, key=categorical_values_total.get)

    
        print("\nThe Statistical Analysis for the two values")
        printNumericalValues(numerical_col1_list, numerical_col2_list,  heading[num1_index], heading[num2_index])
        printNumericalValues(numerical_col2_list,numerical_col1_list, heading[num2_index], heading[num1_index])


        generateNumericalVisualization(numerical_col1_list, numerical_col2_list, heading, num1_index, num2_index)
        
        printStatiscalAnalysis(categorical_values_total, categorical_values_count, highest_number, lowest_number,lowest_value, highest_value)


        print(categorical_values_dict)

        generateCategoricalVisualization(categorical_values_count, categorical_values_total, categorical_values_dict)


    except FileNotFoundError:
        print("Unable to open the file",filename)





def main():
    readfile()

main()


