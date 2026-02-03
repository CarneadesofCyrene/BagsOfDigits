# -*- coding: utf-8 -*-

# Before Using, save /Output Updating.csv as an xlsx.
import csv
import pandas as pd
import math

Base = 9
#Final Output and Final Input will need to have the right number of columns based on the base added.

NoDigits = "[0, 0, 0, 0, 0, 0, 0, 0, 0]"
Location = "BagsOfDigits/Base 9"

initial_data = pd.read_excel(Location + "/Output Final Base 9 68.xlsx", header=None)

import numpy as np #BUGFIX
last_column_name = initial_data.columns[-1] #BUGFIX
Final_column_name = last_column_name + 1 #BUGFIX
initial_data[Final_column_name] = np.nan #BUGFIX

final_data = pd.DataFrame(columns=["Input","Output"])
print(initial_data.head())

for index, row in initial_data.iterrows():
    TryCount = 0
    MaxColumns = 1000
    while TryCount < MaxColumns:
        print(row)
        try:
            StartCol = TryCount
            NextCol = StartCol -1
            PrevCol = StartCol + 1
            print(math.isnan(row[PrevCol]))
            MidDF = pd.DataFrame({"Input":row[StartCol],"Output":"[0, 0, 0, 0, 0, 0, 0, 0, 0]"}, index = [0])
            while StartCol >0:
                IttPair = pd.DataFrame({"Input":row[NextCol],"Output":row[StartCol]}, index = [0])
                MidDF = pd.concat([MidDF,IttPair])
                print(MidDF)
                StartCol = StartCol -1
                NextCol = NextCol - 1
            final_data = pd.concat([final_data,MidDF])
            TryCount = MaxColumns
        except:
            TryCount = TryCount + 1
            

final_data.to_csv(Location +"/Cleaned Base 9 68.csv", index = False)                            

print("Done")

final_data['Count'] = 1
Collapsed = final_data.groupby(['Input','Output']).agg(SUM = ('Count','sum'))
print(Collapsed.head())
Collapsed.to_csv(Location + "/Collapsed Base 9 68.csv", index = True) 

###############################################################################
#Renaming

initial_data = pd.read_csv(Location +"/Collapsed Base 9 68.csv")
print(initial_data.head())
print(type(initial_data['Input']))

initial_data['Input'] = initial_data['Input'].str.replace(" ", "")
initial_data['Output'] = initial_data['Output'].str.replace(" ", "")

initial_data['Input'] = initial_data['Input'].str.replace("[", "")
initial_data['Output'] = initial_data['Output'].str.replace("[", "")

initial_data['Input'] = initial_data['Input'].str.replace("]", "")
initial_data['Output'] = initial_data['Output'].str.replace("]", "")


#Input Data
input_data = initial_data['Input']
split_input = input_data.str.split(',',expand=True)

for i in range(Base):
    j=str(i)
    for index, row in split_input.iterrows():
        if split_input.iloc[index,i] == "0":
            split_input.iloc[index,i] = ""
        elif split_input.iloc[index,i] == "1":
            split_input.iloc[index,i] = ", 1 "+j
        else:
            jj = split_input.iloc[index,i]
            split_input.iloc[index,i] = ", "+jj+" "+j+"'s"



#final_input = pd.DataFrame("We have" + split_input[0] + split_input[1] + split_input[2] + split_input[3] + split_input[4] + split_input[5] + split_input[6] + split_input[7] + split_input[8] + split_input[9] +".")
final_input = pd.DataFrame("We have" + split_input[0] + split_input[1] + split_input[2] + split_input[3] + split_input[4] + split_input[5] + split_input[6] + split_input[7] + split_input[8] + ".")
pd.set_option('display.max_columns', None)
final_input[0] = final_input[0].str.replace("We have,", "We have:")
final_input[0] = final_input[0].str.replace("We have.", "We have no digits.")
print(split_input.head(20))
print(final_input.head(20))
final_input = final_input.rename(columns={0: 'Source_String'})

#Output Data
output_data = initial_data['Output']
split_output = output_data.str.split(',',expand=True)

for i in range(Base):
    j=str(i)
    for index, row in split_output.iterrows():
        if split_output.iloc[index,i] == "0":
            split_output.iloc[index,i] = ""
        elif split_output.iloc[index,i] == "1":
            split_output.iloc[index,i] = ", 1 "+j
        else:
            jj = split_output.iloc[index,i]
            split_output.iloc[index,i] = ", "+jj+" "+j+"'s"

#final_output = pd.DataFrame("We have" + split_output[0] + split_output[1] + split_output[2] + split_output[3] + split_output[4] + split_output[5] + split_output[6] + split_output[7] + split_output[8] + split_output[9] +".")
final_output = pd.DataFrame("We have" + split_output[0] + split_output[1] + split_output[2] + split_output[3] + split_output[4] + split_output[5] + split_output[6] + split_output[7] + split_output[8] + ".")
pd.set_option('display.max_columns', None)
final_output[0] = final_output[0].str.replace("We have,", "We have:")
final_output[0] = final_output[0].str.replace("We have.", "We have no digits.")
print(split_output.head(20))
print(final_output.head(20))
final_output = final_output.rename(columns={0: 'Target_String'})    

weight_data = pd.DataFrame(initial_data['SUM'])

weight_data = weight_data.rename(columns={'SUM': 'weight'})    

concatenated_df = pd.concat([final_input, final_output, weight_data], axis=1, join='outer')

print(concatenated_df)

concatenated_df.to_csv(Location + "/Output_Pairs_Named Base 9 68.csv", index = False)   
#Some columns might need to be renamed for the next file
