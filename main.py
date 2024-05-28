import csv

# Initialization of the empty dictionary for each column
data_dict = {
    "ages": [],
    "sexes": [],
    "bmis": [],
    "childrens": [],
    "smokers": [],
    "regions": [],
    "charges": []
}

# Open the CSV file using DictReader
with open("insurance.csv", "r") as insurance_file:
    insurance_reader = csv.DictReader(insurance_file)
    
    for row in insurance_reader:
        data_dict["ages"].append(int(row["age"]))
        data_dict["sexes"].append(row["sex"])
        data_dict["bmis"].append(float(row["bmi"]))
        data_dict["childrens"].append(int(row["children"]))
        data_dict["smokers"].append(row["smoker"])
        data_dict["regions"].append(row["region"])
        data_dict["charges"].append(float(row["charges"]))

# Function for calculating the length of any list
def len_of_list(lst):
    return len(lst)

# Function for calculating the average value of a list
def avg_value(lst):
    return sum(lst) / len(lst)

# Printing the average values for each numerical column
avg_ages = round(avg_value(data_dict["ages"]))
print("Average Age:", avg_ages)

avg_bmis = round(avg_value(data_dict["bmis"]), 2)
print("Average BMI:", avg_bmis)

avg_children = round(avg_value(data_dict["childrens"]))
print("Average Number of Children:", avg_children)

avg_charges = round(avg_value(data_dict["charges"]), 2)
print("Average Insurance Charge:", avg_charges)

# Function to count the occurrences of values in a list
def count_occurrences(lst, value):
    return lst.count(value)

# Counting smokers and non-smokers
total_smokers = count_occurrences(data_dict["smokers"], "yes")
total_non_smokers = count_occurrences(data_dict["smokers"], "no")
print("Total Smokers:", total_smokers)
print("Total Non-Smokers:", total_non_smokers)

# Counting males and females
total_males = count_occurrences(data_dict["sexes"], "male")
total_females = count_occurrences(data_dict["sexes"], "female")
print("Total Males:", total_males)
print("Total Females:", total_females)

# Function to create a dictionary with the count of each unique value
def create_value_count_dict(lst):
    value_count_dict = {}
    for item in lst:
        if item in value_count_dict:
            value_count_dict[item] += 1
        else:
            value_count_dict[item] = 1
    return value_count_dict

# Creating dictionaries for regions, smokers, and sexes
region_counts = create_value_count_dict(data_dict["regions"])
print("Region Counts:", region_counts)

smoker_counts = create_value_count_dict(data_dict["smokers"])
print("Smoker Counts:", smoker_counts)

sex_counts = create_value_count_dict(data_dict["sexes"])
print("Sex Counts:", sex_counts)

# Function to calculate the difference in average charges between two groups
def calculate_charge_difference(group1, group2, charges):
    total_group1_charges = sum(charges[i] for i, val in enumerate(group1) if val)
    total_group2_charges = sum(charges[i] for i, val in enumerate(group2) if val)
    avg_group1_charge = total_group1_charges / len(group1)
    avg_group2_charge = total_group2_charges / len(group2)
    return round(avg_group1_charge - avg_group2_charge, 2)

# Calculating the difference in average charges between smokers and non-smokers
charge_difference = calculate_charge_difference(data_dict["smokers"], ["no"] * len(data_dict["smokers"]), data_dict["charges"])
print("Average Charge Difference (Smokers - Non-Smokers):", charge_difference)

# Function to calculate the average age of individuals with a specified number of children
def average_age_with_children(children_count, ages, childrens):
    relevant_ages = [ages[i] for i, count in enumerate(childrens) if count == children_count]
    return round(avg_value(relevant_ages))

# Calculating the average age of individuals with one child
average_age_one_child = average_age_with_children(1, data_dict["ages"], data_dict["childrens"])
print("Average Age of Individuals with One Child:", average_age_one_child)
