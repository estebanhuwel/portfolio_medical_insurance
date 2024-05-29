import random # I did it in first instance to create the full_name column
import csv
import pandas as pd

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

# Test on pandas
df1 = pd.read_csv('insurance.csv')
# df1 = pd.DataFrame(data_dict)
print(df1.head(4))
def average_fn(df_pd, column_name):
    return round(df_pd[column_name].mean())

avg_age_pd = average_fn(df1, "age")
print("This is the average Age, calculed with Pandas: " + str(avg_age_pd))

# Lets say we have a list name, with first and last name, not separated if it is male or female.
# The goal is to create a list combination long enough to feed my current data DataFrame so:
first_names = [
    "Adriana", "Alejandro", "Alicia", "Alonso", "Andrés", "Ángel", "Antonio", "Beatriz", 
    "Carlos", "Carmen", "Catalina", "Cecilia", "Cristina", "Daniel", "David", "Diego", 
    "Eduardo", "Elena", "Emilio", "Ernesto", "Fernando", "Francisco", "Gabriel", "Gloria", 
    "Guillermo", "Héctor", "Ignacio", "Isabel", "Javier", "Jesús", "Joaquín", "Jorge", 
    "José", "Juan", "Julia", "Laura", "Luis", "Manuel", "Marcos", "María", "Marta", 
    "Martín", "Miguel", "Natalia", "Nicolás", "Óscar", "Pablo", "Patricia", "Pedro", 
    "Raúl", "Ricardo", "Rosa", "Salvador", "Santiago", "Silvia", "Teresa", "Tomás", 
    "Victoria", "Ximena", "Yolanda", "Zacarías"
]

last_names = [
    "Aguirre", "Alonso", "Álvarez", "Arias", "Benítez", "Blanco", "Cabrera", "Calvo", 
    "Campos", "Cano", "Castillo", "Castro", "Cortés", "Delgado", "Díaz", "Domínguez", 
    "Durán", "Escobar", "Fernández", "García", "Giménez", "Gómez", "González", "Guerrero", 
    "Gutiérrez", "Hernández", "Iglesias", "Jiménez", "López", "Martínez", "Medina", "Mendoza", 
    "Molina", "Moreno", "Muñoz", "Navarro", "Núñez", "Ortega", "Ortiz", "Pérez", "Ramírez", 
    "Ramos", "Reyes", "Rodríguez", "Romero", "Ruiz", "Sánchez", "Santos", "Serrano", "Suárez", 
    "Torres", "Vargas", "Vázquez", "Vega", "Velázquez", "Vicente", "Zamora", "Zapata"
]

# it is enough combinations?
num_combinations = len(df1.age)

assert len(first_names) * len(last_names) >= num_combinations, "There is not enough unique combinations, feed more!"

full_name_list = set()
while len(full_name_list) < num_combinations:
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    full_name_list.add(f"{first_name} {last_name}")

full_name_list = list(full_name_list)

get_first_name = lambda str: str.split(' ')[0]
get_last_name = lambda str: str.split(' ')[-1]

# Once we created the full_name_list, we add it to our DataFrame
df1["Full Name"] = full_name_list
# df1["First Name"] = df['Full Name'].apply(get_first_name) # if we want to add the first name in a new column
# df1["Last Name"] = df['Last Name'].apply(get_last_name) # if we want to add the last name in a new column

print(df1.head(4))

# if we want to find how many, or average value of smokers for example, and know the average age of people who smokes or not:
smokers_group_age = df1.groupby("smoker").age.mean()
print(smokers_group_age)

# average price of the insurance from smokers an no smokers
smokers_group_charge = df1.groupby("smoker").charges.mean()
print(smokers_group_charge)

# average charge of insurance for smokers and the amount of kids
smokers_group_kids_charge = df1.groupby(["smoker", "children"]).charges.mean()
print(smokers_group_kids_charge)

# because we noted that the insured people that smoke and have 5 kids is less than the avg charge we want to know the avg BMI
smokers_children_group_bmi_charges = df1.groupby(["smoker", "children"])[['bmi', 'charges']].mean()
print(smokers_children_group_bmi_charges)

# now we want to do a more complex avg table
general_avg = df1.groupby(["sex", "smoker", "children"])[['age', 'bmi', 'charges']].mean()
general_avg["age"] = general_avg["age"].round()
general_avg["bmi"] = general_avg["bmi"].round(2)
general_avg["charges"] = general_avg["charges"].round(2)
print(general_avg)
