# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 15:57:29 2025

@author: carne
"""

import csv
import random
import ast
import os
Base = "Base 5/"


#pypy "C:\Users\thabe\Documents\Carneades\xkcd Puzzle\More Bases\Base 5\One Off Checking\Base 5 One Off Checking.py"

#folder = "C:/Users/carne/OneDrive/Carneades/Experimental Philosophy/XKCD Puzzle/Base 4 After 500/"
#Main Computer 
folder = 'C:/Users/thabe/Documents/Carneades/xkcd Puzzle/1.26.26 Cleanup of Existing Data and Gephy/'
extra = ''

with open(folder + Base + extra + '/LastGood.txt', 'r') as file:
    tuple_str = file.read()

# Using eval() to parse the string back into a tuple (use with caution)
retrieved_tuple = eval(tuple_str)
CurrentNumberToCheck = retrieved_tuple[1] + 1
ImportLastGoodDiagonal = retrieved_tuple[0]
last_good_Diagonal = ImportLastGoodDiagonal


def base_5_conversion(n):

    if n == 0:
        return '0'
    nums = []
    temp_n = abs(n)
    while temp_n:
        temp_n, r = divmod(temp_n, 5)
        nums.append(str(r))
    return ''.join(reversed(nums))

def length_of_string(s):

    return len(s)

def BaseConversion (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 5)
        nums.append(str(r))
    return ''.join(reversed(nums))

def run_program_base_5(current_sum):
    all_data = []

    print_num = 0
    all_counter = 0
    for a in range(current_sum + 1):
        for b in range(current_sum + 1 - a):
            for c in range(current_sum + 1 - a - b):
                for d in range(current_sum + 1 - a - b - c):
                    e = current_sum - a - b - c - d
                    
                    zeros5 = base_5_conversion(a)
                    ones5 = base_5_conversion(b)
                    twos5 = base_5_conversion(c)
                    threes5 = base_5_conversion(d) 
                    fours5 = base_5_conversion(e) 
    
                    # 3. Calculate lengths
                    zeros_count = length_of_string(zeros5)
                    ones_count = length_of_string(ones5)
                    twos_count = length_of_string(twos5)
                    threes_count = length_of_string(threes5)
                    fours_count = length_of_string(fours5)
                    
    
                    # 4. Calculate total digits
                    total_digits = zeros_count + ones_count + twos_count + threes_count + fours_count
    
                    row = [a, b, c, d, e, current_sum, total_digits]
                    all_data.append(row)
    
                    # Check for progress print
                    if print_num == 1000000:
                        print(f"Processed: {current_sum}, Entries {all_counter}")
                        print_num = 0
                    print_num += 1
                    all_counter += 1
    return(all_data)

def collapsing(to_collapse):
    # --- Data Summarization (Replacing GroupBy and Max) ---
    collapsed_data = {}

    # The column indices for Total (4) and TotalDigits (5) in the all_data list
    TOTAL_INDEX = 5
    TOTAL_DIGITS_INDEX = 6

    for row in to_collapse:
        total_sum = row[TOTAL_INDEX]
        total_digits = row[TOTAL_DIGITS_INDEX]

        if total_sum not in collapsed_data or total_digits > collapsed_data[total_sum]:
            collapsed_data[total_sum] = total_digits

    # --- CSV Output (Replacing .to_csv) ---

    collapsed_rows = [['Total', 'TotalDigits']] + [[k, v] for k, v in collapsed_data.items()]

    # Sort by 'Total'
    collapsed_rows[1:] = sorted(collapsed_rows[1:], key=lambda x: x[0])
    return(collapsed_rows[1][1])

def split_number(number):
    digits = []
    if number == 0:
        digits = [0]
    else:
        while number > 0:
            digits.insert(0, number % 10)
            number //= 10
    return digits

def drop_sublist(full_list, drop_list):
    new_sublist = full_list.copy()
    for dr_value in drop_list:
        new_sublist.remove(dr_value)
    return(new_sublist)

def split_into_digits(numbers):
    result = []
    for num in numbers:
        for digit in str(num):
            result.append(int(digit))
    return result

def remove_zeros(test_list, item): 
    # using list comprehension to perform the task 
    res = [i for i in test_list if i != item] 
    return res 
FullExit = 0
while FullExit <100000:
    full_data = run_program_base_5(CurrentNumberToCheck)
    collapsed_data = collapsing(full_data)
    
    Exit = 0
    goodlist = []
    goodcounterlist = []
    goodhistorylist = []
    goodhistorylisttemp = []
    savecount = 0
    #Counting the number of instances checked before a save
    runcount = 0
    #Counting the number of instances checked regardless of saves
    allcount = 0
    #!# (2/5)  This symbol is where we added the "last good" efficiency improvement
    Found_Bad = 0
    for node in full_data:
        runcount = runcount + 1
        allcount = allcount + 1

        ogcount0 = node[0]
        ogcount1 = node[1]
        ogcount2 = node[2]
        ogcount3 = node[3]
        ogcount4 = node[4]
        
        count0 = ogcount0
        count1 = ogcount1
        count2 = ogcount2
        count3 = ogcount3
        count4 = ogcount4
        
        tpcount0 = count0
        tpcount1 = count1
        tpcount2 = count2
        tpcount3 = count3
        tpcount4 = count4
        
        BASEcount0 = int(BaseConversion(count0))
        BASEcount1 = int(BaseConversion(count1))
        BASEcount2 = int(BaseConversion(count2))
        BASEcount3 = int(BaseConversion(count3))
        BASEcount4 = int(BaseConversion(count4))
        BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3, BASEcount4]
        counter_list = [count0,count1,count2,count3,count4]
        if runcount == 1000000: #At 6 sec with (1000000).  Adding for 10min
            #print("Save")
            print(allcount)
            print(counter_list)
            runcount = 0
        digit_count = node[5]
        loseable_digits =  collapsed_data + 5 
        lowest_possible_diagonal = digit_count - loseable_digits
        if lowest_possible_diagonal > last_good_Diagonal:
            print(lowest_possible_diagonal)
            print(loseable_digits)
            print(last_good_Diagonal)
            print("BROKEN")
            FullExit = 100000
            break
            Found_Bad = 1
        ogcounter_list = [count0,count1,count2,count3,count4]
        Check_Exit = 0
        history_list = []
        while Check_Exit == 0:
            count0 = tpcount0
            count1 = tpcount1
            count2 = tpcount2
            count3 = tpcount3
            count4 = tpcount4
            BASEcount0 = int(BaseConversion(count0))
            BASEcount1 = int(BaseConversion(count1))
            BASEcount2 = int(BaseConversion(count2))
            BASEcount3 = int(BaseConversion(count3))
            BASEcount4 = int(BaseConversion(count4))
            
            if not(BASEcounter_list in history_list):
                history_list.append(BASEcounter_list)
            counter_list = [count0,count1,count2,count3,count4]
            BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3,BASEcount4]
    
            #This removes one from each count if the digit is still there because it will need to be stated.
            if count0 >0:
                tpcount0 = count0 - 1
            if count1 >0:
                tpcount1 = count1 - 1
            if count2 >0:
                tpcount2 = count2 - 1
            if count3 >0:
                tpcount3 = count3 - 1
            if count4 >0: # Change: Added count4 logic
                tpcount4 = count4 - 1
            # This drops zeros, then it splits all the remaining numbers into digits.
            nozerolist = remove_zeros(BASEcounter_list, 0)
            splitlist = split_into_digits(nozerolist)
            #This counts the number of zero digits
            spcount0 = splitlist.count(0)
            tpcount0 = tpcount0 - spcount0
            if tpcount0 < 0:
                Check_Exit = 1
            else:
                spcount1 = splitlist.count(1)
                tpcount1 = tpcount1 - spcount1
                if tpcount1 < 0:
                    Check_Exit = 1
                else:
                    spcount2 = splitlist.count(2)
                    tpcount2 = tpcount2 - spcount2
                    if tpcount2 < 0:
                        Check_Exit = 1
                    else:
                        spcount3 = splitlist.count(3)
                        tpcount3 = tpcount3 - spcount3
                        if tpcount3 < 0:
                            Check_Exit = 1
                        else:
                            spcount4 = splitlist.count(4)
                            tpcount4 = tpcount4 - spcount4
    
            if tpcount0< 0 or tpcount1<0 or tpcount2<0 or tpcount3<0 or tpcount4<0:
                Check_Exit = 1
            #!# (4/5) Need to indent everythign after this and don't forget to add the extra term
            else:
                tp_Diagonal = tpcount0 + tpcount1 + tpcount2 + tpcount3 + tpcount4
                if tp_Diagonal > last_good_Diagonal:
                    Check_Exit = 1
                    #print("Cantor:", CantorCount, counter_list, BASEcounter_list, " Reduced:", reducedCantorCount, [tpcount0,tpcount1,tpcount2])
                #!#
                else:
                    tpcounterlist = [tpcount0,tpcount1,tpcount2,tpcount3,tpcount4]
                    if not(BASEcounter_list in history_list):
                        history_list.append(BASEcounter_list)
                        #print(history_list)
                    if (tpcounterlist == [0,0,0,0,0] and Check_Exit==0):  #or (mylist in goodlist and Check_Exit ==0)
                        print("newgood")
                        print(history_list)
                        print(Exit)
                        file1 = open (folder + Base + extra + '/Location.txt', 'w')
                        file1.write(str(counter_list))
                        file1.close()
                        #!# (5/5)
                        last_good_Diagonal = digit_count
                        #!#
                        if not(ogcounter_list in goodcounterlist):
                            for old_list in history_list:
                                goodcounterlist.append(old_list)
                            goodhistorylist.append(history_list)
                            goodhistorylisttemp.append(history_list)
                            Exit = Exit + 1
                            savecount = savecount + 1
                        Check_Exit = 1
        #ogcount0 = ogcount0 + 1
        if savecount == 1:
            savecount = 0
            csv_file = folder + Base + extra + '/Output Updating.csv'
        
            # Write the data to the CSV file
            with open(csv_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(goodhistorylisttemp)
                file.close
                goodhistorylisttemp = []
        
            print(f"Data written to {csv_file}")
    
    print("Final Good List")
    print(goodlist)
    print("Good History")
    print(goodhistorylist)
    print("Good Counter")
    print(goodcounterlist)
    
    csv_file = folder+ Base + extra + 'Data/Output Updating' + str(CurrentNumberToCheck) +'.csv'
    
    # Write the data to the CSV file
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(goodhistorylisttemp)
        file.close
    
    
    # Specify the CSV file name
    csv_file = folder+ Base + extra + 'Data/Output Final' + str(CurrentNumberToCheck) + '.csv'
    
    # Write the data to the CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(goodhistorylist)
        file.close
    
    file1 = open (folder + Base + extra + '/LastGood.txt', 'w')
    Storage = (last_good_Diagonal, CurrentNumberToCheck)
    file1.write(str(Storage))
    file1.close()
    
    
    print(f"Data written to {csv_file}")
    
    print("End")
    CurrentNumberToCheck = CurrentNumberToCheck + 1


