import csv

# Iniatalization of the empty list for each column_names
data_dict = {
    "ages": [],
    "sexes": [],
    "bmis": [],
    "childrens": [],
    "smokers": [],
    "regions": [],
    "charges": []
}

ages = []
sexes = []
bmis = []
childrens = []
smokers = []
regions = []
charges = []

with open("insurance.csv", "r") as insurance_file:
    insurance_reader = csv.reader(insurance_file)
    column_names = next(insurance_reader)
    
    # print("This are the column names: " + str(column_names))
    # now that we have the information ['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']
    
    for insured_person in insurance_reader:
        ages.append(int(insured_person[0]))
        sexes.append(insured_person[1])
        bmis.append(float(insured_person[2]))
        childrens.append(int(insured_person[3]))
        smokers.append(insured_person[4])
        regions.append(insured_person[5])
        charges.append(float(insured_person[6]))

# Assign the lists to the dictionary
data_dict["ages"] = ages
data_dict["sexes"] = sexes
data_dict["bmis"] = bmis
data_dict["childrens"] = childrens
data_dict["smokers"] = smokers
data_dict["regions"] = regions
data_dict["charges"] = charges

# Function for calculating the length of any list
def len_of_list(list):
    total = len(list)
    return total

# Funtion for calculating the average value of a list
def avg_value(lst):
    list_len = len_of_list(lst)
    list_value = 0
    
    for value in lst:
        list_value += value
    
    list_value = list_value / list_len
    return list_value

# Print of the Average Values for each one of the Numerical values
avg_ages = round(avg_value(ages))
print("This is the average Age: "+ str(avg_ages))

avg_bmis = round(avg_value(bmis), 2)
print("This is the average BMI: "+ str(avg_bmis))

avg_children = round(avg_value(childrens))
print("This is the average Children an insured person has is: "+ str(avg_children))

avg_charges = round(avg_value(charges), 2)
print("This is the average Insurance Charge: "+ str(avg_charges))

# Function to find the values repeated in each list:
def repeated_values(value1, value2, list):
    value_1 = 0
    value_2 = 0
    for element in list:
        if value1 == element:
            value_1 += 1
        elif value2 == element:
            value_2 += 1
    return value_1, value_2
    
total_smoker, total_no_smoker = repeated_values("yes", "no", smokers)
print("The total amount of smokers is: " + str(total_smoker))
print("The total amount of non-smokers is: " + str(total_no_smoker))

total_males, total_females = repeated_values("male", "female", sexes)
print("The total amount of males insured is: " + str(total_males))
print("The total amount of females insured is: " + str(total_females))

# Function to create a dictionary with the value for each element:
def new_dictionary(list):
    dict = {}
    for element in list:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    return dict

region_dictionary = new_dictionary(regions)
print(region_dictionary)

smokers_dictionary = new_dictionary(smokers)
print(smokers_dictionary)

sexes_dictionary = new_dictionary(sexes)
print(sexes_dictionary)    

# Check for each one, how many insured person is above or below each value:
def diference_in_cost(list1, list2, value1_list1, value2_list1):
    total_1_from_value1 = 0
    len_total1 = 0
    total_2_from_value2 = 0
    len_total2 = 0
    
    for index, element in enumerate(list1):
        if element == value1_list1:
            total_1_from_value1 += list2[index]
            len_total1 += 1
        elif element == value2_list1:
            total_2_from_value2 += list2[index]
            len_total2 += 1
    diference = round((total_1_from_value1 /len_total1  - total_2_from_value2/len_total2), 2)
    return diference
    
diference_from_smokers_no_smokers = diference_in_cost(smokers, charges, "yes", "no")
print("If you are a smoker then you will probably be charged " + str(diference_from_smokers_no_smokers) + "$ more.")

# Function for creating an average age of people with one children
def average_age_one_children(ages, childrens):
    total_age_one_child = 0
    count_one_child = 0
    
    # creation of the zipped list, for childrens and ages:
    zipped_list = zip(ages, childrens)
    for age, children in zipped_list:
        if children == 1:
            total_age_one_child += age
            count_one_child += 1
    
    if count_one_child != 0:
        avg_age_one_children = round(total_age_one_child / count_one_child)
    else:
        avg_age_one_children = 0
    
    return avg_age_one_children, count_one_child

avg_age_one_child, count_one_child = average_age_one_children(ages, childrens)
print("Average age of people with one child:", avg_age_one_child)
print("Total number of people with one child:", count_one_child)
    



    
