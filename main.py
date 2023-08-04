# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

from old_exp_data_converter import convert_old_experiment
from final_exp_data_converter import convert_experiment
from combine_data import concatenate_dataframes
from distance_matrix import process_and_combine_similarities
from subject_weights_converter import process_data_and_save_to_csv
from individual_map import process_and_save_data

import pandas as pd

# Transfer SPSS data to csv file, replace when needed
group_space = """\
    1      A1_LP       .9234   -.7453
    2      A2_LP      1.0571   -.1295
    3      A3_LP       .7585   1.0165
    4      A4_LP      1.0828   -.3490
    5      A_HN      -1.5516    .4468
    6      B_HN      -1.7621    .9994
    7      C_LN       -.7134  -1.2636
    8      F_HN       -.7537   1.3125
    9      G_HP        .9034   1.2468
   10      H_HP       1.0188   1.3441
   11      J_Ne        .3534  -1.1146
   12      K_Ne        .2663  -1.2796
   13      M_LN       -.9606   -.7672
   14      N_LN      -1.1905   -.4857
   15      O_LN       -.8392  -1.1695
   16      P_HP        .9683   1.2652
   17      Q_HP       1.0794   1.2712
   18      U_Ne        .5032   -.9808
   19      V_Ne        .3194   -.9988
   20      W_HN      -1.4631    .3810
"""


subject_weights = """\
      1     .4745    .4816    .4852
      2     .5386    .0050    .0058
      3     .2803    .6703    .1876
      4     .1772    .4774    .2793
      5     .0160    .7205    .3100
      6     .2168    .7521    .2344
      7     .5805    .1048    .1352
      8     .4367    .2826    .2632
      9     .5847    .1565    .2041
     10     .2133    .4501    .2794
     11     .1094    .6644    .3484
     12     .2311    .6565    .1998
     13     .0492    .7702    .3145
     14     .0075    .6852    .3059
     15     .1646    .5222    .2992
     16     .4697    .7795    .1521
     17     .2110    .6895    .2170
     18     .3035    .8089    .2173
     19     .3010    .7979    .2154
     20     .2704    .5795    .3962
     21     .4163    .7671    .1670
     22     .4931    .0957    .1003
     23     .0384    .5698    .2670
     24     .2686    .4861    .3313
     25     .4530    .8880    .1795
     26     .2472    .3730    .2451
     27     .0269    .6811    .3134
     28     .4566    .7622    .1529
     29     .2717    .7023    .1995
     30     .2461    .7877    .2337
     31     .1395    .6940    .3819
     32     .2078    .7293    .2308
     33     .3305    .3121    .2372
     34     .2182    .6635    .2063
     35     .5267    .1702    .1926
     36     .2354    .5102    .3287
     37     .1411    .6570    .3625
     38     .0910    .5782    .2944
     39     .0064    .7289    .3248
"""

# Create a dictionary to store repositories
repository_data = {}

# Read repositories from the text file and store them in the dictionary
with open("repository.txt", "r") as txt_file:
    for line in txt_file:
        name, url = line.strip().split(',')
        repository_data[name] = url

# Access repositories using the dictionary
repository_name_1 = "raw_data_old"
raw_data_old = repository_data[repository_name_1]

repository_name_2 = "raw_data_final"
raw_data_final = repository_data[repository_name_2]

repository_name_3 = "processed_data"
processed_data = repository_data[repository_name_3]

repository_name_4 = "new_data"
new_data = repository_data[repository_name_4]

repository_name_5 = "new_data_2"
new_data_2 = repository_data[repository_name_5]

repository_name_6 = "distance_matrix"
distance_matrix = repository_data[repository_name_6]

repository_name_7 = "group_space_data"
group_space_data = repository_data[repository_name_7]

repository_name_8 = "subject_weights_data"
subject_weights_data = repository_data[repository_name_8]

repository_name_9 = "individual_ground_truth"
individual_ground_truth = repository_data[repository_name_9]

repository_name_10 = "updated_data"
updated_data = repository_data[repository_name_10]


while True:
    print("\nChoose a function:")
    print("1. convert old raw data from txt to csv")
    print("2. convert final raw data from txt to csv")
    print("3. merge new data to existing dataframe")
    print("4. compute distance matrix")
    print("5. convert group space and subject weights from string to csv")
    print("6. compute individual ground_truth")
    print("7. Exit")

    choice = input("Enter the number of the function you want to choose: ")

    if choice == "1":
        convert_old_experiment(raw_data_old, processed_data)
    elif choice == "2":
        convert_experiment(raw_data_final, processed_data)
    elif choice == "3":
        concatenate_dataframes(new_data, new_data_2,updated_data)
    elif choice == "4":
        process_and_combine_similarities(processed_data, distance_matrix)
    elif choice == "5":
        process_data_and_save_to_csv(group_space, group_space_data, subject_weights, subject_weights_data)
    elif choice == "6":
        group_space = np.genfromtxt(group_space_data, delimiter=',')
        subject_weights = np.genfromtxt(subject_weights_data, delimiter=',')
        process_and_save_data(individual_ground_truth, group_space, subject_weights)
    elif choice == "7":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice.")


