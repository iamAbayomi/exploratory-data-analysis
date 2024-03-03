import math
import matplotlib.pyplot as plt

# List of user defined functions.

def format_num(number):
    return '{:,}'.format(number)

def total(lists):
    """
    Function to get the total of the items in the lists.

    Parameters
    ----------
    lists: list
        The lists to find the total
    
    Returns
    -------
    total: int
        The total value in the lists.
    """
    return sum(lists)

def mean(lists):
    """
    Function to get the mean of the items in the lists.

    Parameters
    ----------
    lists: list
        The lists to find the mean
    
    Returns
    -------
    mean: int
        The mean of the lists.
    """
    return round(sum(lists)/len(lists),2)

def median(lists):
    """
    Function to get the median of the items in the lists.

    Parameters
    ----------
    lists: list
        The lists to find the median
    
    Returns
    -------
    median: int
        The median of the lists.
    """
    num = sorted(lists)
    middle_index = int(len(num)/2)
    if(len(num) % 2 != 0):
      return num[middle_index]
    else:
        return (num[middle_index-1] + num[middle_index])/ 2
       
def mode(lists):
    """
    Function to get the mode of the items in the lists.

    Parameters
    ----------
    lists: list
        The lists to find the mode
    
    Returns
    -------
    mode: int
        The mode of the lists.
    """
    sort_num = sorted(lists)
    unique_num = list(set(sort_num))
    unique_num_count = []
    #print(sort_num)
    for i in unique_num:
        unique_num_count.append(lists.count(i))
    mode_index = unique_num_count.index(max(unique_num_count))
    #print(max(unique_num_count))
    return unique_num[mode_index]

def maximum(lists):
    """
    Function to calculate the maximum value in a list
    
    Parameters
    ----------
    lists: list
        The list to find maximum value

    Returns
    -------
    max: int
        The maximum value in the list.
    """
    return max(lists)

def minimum(lists):
    """
    Function to calculate the minimum value in a list
    
    Parameters
    ----------
    lists: list
        The list to find minimum value

    Returns
    -------
    min: int
        The minimum value in the list.
    """
    return min(lists)

def ranges(lists):
    """
    Function to the range in a list
    
    Parameters
    ----------
    lists: list
        The list to find range

    Returns
    -------
    range: int
        The range in the list.
    """
    return maximum(lists) - minimum(lists)


def iqr(lists):
    """
    Function to calculate the interquartile-range in a list
    
    Parameters
    ----------
    lists: list
        The list to find interquartile-range value

    Returns
    -------
    iqr: int
        The interquartile-range in the list.
    """
    num = sorted(lists)
    mid_index = int(len(num)/2)
    if(len(num) % 2 ==0):
        #print("even",median(num[mid_index:]), " - ", median(num[:mid_index]))
        return median(num[mid_index:]) -  median(num[:mid_index]) 
    else:
        #print("old",median(num[mid_index+1:]), " - ", median(num[:mid_index]))
        return median(num[mid_index+1:]) -  median(num[:mid_index]) 


def standard_deviation(lists):
    """
    Function to calculate the standard deviation value in a list
    
    Parameters
    ----------
    lists: list
        The list to find the standard deviation.

    Returns
    -------
    std: int
        The standard deviation
    """
    squared_deviations = [(x - mean(lists)) ** 2 for x in lists]
    return round(math.sqrt(sum(squared_deviations) / (len(lists) - 1)),2)

def squared_deviations(lists):
    """
    Function to calculate the squared deviation value in a list
    
    Parameters
    ----------
    lists: list
        The list to find squared deviation value

    Returns
    -------
    sqr: int
        The squared deviation value of the list.
    """
    return [(x - mean(lists)) ** 2 for x in lists]

def correlation_coefficient(values1, values2):
    """
    Function to calculate the correlation cofficient value in a list
    
    Parameters
    ----------
    lists: list
        The list to find correlation cofficient value

    Returns
    -------
    correlation cofficient : int
        The correlation cofficient of the list.
    """
    mean1 = mean(values1)
    mean2 = mean(values2)

    std_deviation1 = standard_deviation(values1)
    std_deviation2 = standard_deviation(values2)

    covariance = sum((x - mean1) * (y - mean2) for x, y in zip(values1, values2))
    correlation = covariance / (std_deviation1 * std_deviation2 * (len(values1) - 1))

    return round(correlation, 2)

def median_skewness(lists):
    """
    Function to calculate the median skewness value in a list
    
    Parameters
    ----------
    lists: list
        The list to find median skewness value

    Returns
    -------
    median skewness: int
        The median skewness value of the list.
    """
    return (3 * (mean(lists)- median(lists))/ standard_deviation(lists))

def mode_skewness(lists):
    """
    Function to calculate the mode skewness value in a list
    
    Parameters
    ----------
    lists: list
        The list to find mode skewness value

    Returns
    -------
    mode skewness: int
        The mode skewness value in the list.
    """
    return ((mean(lists)- mode(lists))/ standard_deviation(lists))



# Histograms of each of the two numerical variables
def histogram(lists, title):
    """
    Function to plot the histogram using the lists values
    
    Parameters
    ----------
    lists: list
        The lists needed to plot the histogram
    title: string
        The title of the histogram
    """
    fig,ax = plt.subplots()
    # Set the title
    ax.set_title(title+ " Histogram")
    # Set the axis label
    ax.set_ylabel("Frequency")
    ax.set_xlabel(title)
    bins_list = [ i/2 for i in range(int(max(lists))*2+1)]
    ax.hist(lists,ec="black")
    plt.show()
    fig.savefig(title+ " Histogram.png")
# Plot a Bie chart showing the total/average of the values in each sub-category

def boxplots(list, title, showFilers= True):
    """
    Function to plot the boxplots using the lists values
    
    Parameters
    ----------
    lists: list
        The lists needed to plot the boxplots
    title: string
        The title of the boxplots
    showFilters: string
        The title of the boxplots
    """
    fig, ax = plt.subplots()
    ax.set_title("Box plot showing "+ title)
    ax.set_ylabel(title)
    ax.boxplot(list, showfliers=showFilers)
    plt.show()
    fig.savefig("Box plots showing " + title + ".png", bbox_inches = 'tight')
  

# Plot a Box plots of the values for each sub-category, done in a single visualisation.
def scatterplots(first_lists, second_lists):
    """                                                
    Function to plot the scatter plots using the lists values
    
    Parameters
    ----------
    firstlists: list
        The first lists needed to plot the scatter plots
    secondlists: list
        The second lists needed to plot the scatter plots
    """
    fig, ax = plt.subplots()

    # Set the title
    ax.set_title("Scatter Plots of Total Revolving Balance vs Total Transaction Amount")

    # set the labels on the axes
    ax.set_ylabel("Total Revolving Balance")
    ax.set_xlabel("Total Transaction Amount")
    
    # do a scatter plot
    ax.scatter(first_lists, second_lists)

    plt.show()
    # save the image
    fig.savefig("Scatter Plots of Total Revolving Balance vs Total Transaction Amount.png")

def piechart(data):
    """
    Function to plot the piechart using the lists values
    
    Parameters
    ----------
    data: list
        The data needed to plot the piechart
    """
    # fig, ax = plt.subplots(figsize=(10, 10))
    fig, ax = plt.subplots()
    ax.set_title("Pie Chart of Total Revolving Balance in each sub-category")
    ax.pie(data.values(), labels= data.keys(), autopct="%.0f%%")
    plt.show()
    fig.savefig("images/piechart of the education.png")


# bar chart of the two variables
# Bar chart showing the total of the values in each sub-category
def barchart(data):
    """
    Function to plot the barchart using the lists values
    
    Parameters
    ----------
    data: list
        The data needed to plot the barchart
    """
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_title('Bar chart showing the total of the values in each sub-category')
    ax.set_ylabel('Total Revolving Balance')
    ax.set_xlabel('Educational Level')
    y_pos = [ i for i in range(len(data))]    
    # set the labels on the axes
    ax.set_yticks(y_pos)
    ax.set_yticklabels(data.keys())

    for index, value in enumerate(data.values()):
        ax.text(value, index-0.25, str(value))

    ax.barh(y_pos, data.values())
    # ax.barh(data.keys(), data.values())
    fig.savefig('barchart of the total revolving balance.png')
    plt.show()


# A Box plots of the values for each sub-category, done in a single visualisation
def boxplotfordict(data):
    """
    Function to plot the boxplots using the lists values
    
    Parameters
    ----------
    boxplotfordict: list
        The lists needed to plot the boxplots
    """
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_title('Box Plot of Total Reloving Balance by Education Level')
    ax.set_label("Number of Category Values")
    ax.set_xlabel('Educational Level')
    ax.set_ylabel('Total Revolving Balance')
    ax.boxplot(data.values(), labels=data.keys())
    plt.show()
    fig.savefig('boxplot of the each value in education level.png')



def formatPieChart(value):
    for i in value:
        print(i, ":", format_num(value[i]))


def printNumericalValues(first_list, second_list, first_list_name="", second_list_name= ""): 
    # Total
    print(first_list_name)
    print("Number of Values:", len(first_list))
    print("Total:", total(first_list))
    print("Mean:", mean(first_list))
    print("Median:", median(first_list))
    print("Mode:", mode(first_list))
    print("Maximum:", maximum(first_list))
    print("Minimum:", minimum(first_list))
    print("Range:", ranges(first_list))
    print("Interquatile Range:", iqr(first_list))
    print("Standard Deviation:", standard_deviation(first_list))
    print("Median Skewness:", round(median_skewness(first_list),2) )
    print("Mode Skewness:", round(mode_skewness(first_list),2))
    print("Correlation between "+ first_list_name+" and " + second_list_name+": ", 
          correlation_coefficient(first_list,second_list))
    print("\n",)


def printStatiscalAnalysis(categorical_values_total,categorical_values_count, highest_number, lowest_number, highest_value, lowest_value):
    print("\nThe Analysis by category")
    print("Number of Educational Level:",len(categorical_values_total.keys()))
    print("Educational Level with the highest frequency is: " + highest_number  
            + " (" + format_num(categorical_values_count[highest_number]) + ")")
    print("Educational Level with the lowest frequency is: " +  lowest_number 
            + " (" + format_num(categorical_values_count[lowest_number] ) + ")")
    print("Educational Level with the highest total revolving balance is: " 
            + highest_value  + " (" + format_num(categorical_values_total[highest_value])+ ")")
    print("Educational Level with the lowest total revolving balance is:  "
            +  lowest_value  + " (" + format_num(categorical_values_total[lowest_value] ) + ")" + "\n")


def generateNumericalVisualization(numerical_col1_list, numerical_col2_list, heading, num1_index, num2_index):
    vis= ''
    cis=''

    while vis != 'q':
        vis = input("Select the visualization you want to peform? \n [H] Histogram, [B] Box plot, [S] Scatter plot , [Q] Quit? ")
        vis = vis.lower()
        if vis == "h":
            histogram(numerical_col1_list, heading[num1_index]) 
            histogram(numerical_col2_list, heading[num2_index])
        elif vis == "b":
            boxplots(numerical_col1_list, heading[num1_index]) 
            boxplots(numerical_col2_list, heading[num2_index])

            boxplots(numerical_col1_list, heading[num1_index], False) 
            boxplots(numerical_col2_list, heading[num2_index], False)
        elif vis == "s":
            scatterplots(numerical_col1_list, numerical_col2_list)


def generateCategoricalVisualization(categorical_values_count, categorical_values_total, categorical_values_dict):
    cis= ''
    while  cis != 'q':
            cis = input("Select the visualization you want to peform? \n [P] Pie Chart, [Bar] Bar Chart, [Box] Box Plots [Q] Quit? ")
            cis = cis.lower()
            if cis == "p":
                piechart(categorical_values_count)
            elif cis == "bar":
                barchart(categorical_values_total)
            elif cis == "box":
                boxplotfordict(categorical_values_dict)

