# -*- coding: utf-8 -*-
import csv
import random
import ast
import os
Base = "Base 4/"


#Main Computer 
folder =  'BagsOfDigits/'

with open(folder + Base + '/LastGood.txt', 'r') as file:
    tuple_str = file.read()

# Using eval() to parse the string back into a tuple (use with caution)
retrieved_tuple = eval(tuple_str)
CurrentNumberToCheck = retrieved_tuple[1] + 1
ImportLastGoodDiagonal = retrieved_tuple[0]
last_good_Diagonal = ImportLastGoodDiagonal


def base_4_conversion(n):
    """
    Converts a non-negative integer to its quaternary (base-4) string representation.
    """
    if n == 0:
        return '0'
    nums = []
    temp_n = abs(n)
    while temp_n:
        # Change the base from 3 to 4
        temp_n, r = divmod(temp_n, 4)
        nums.append(str(r))
    return ''.join(reversed(nums))

def length_of_string(s):
    """
    Returns the length of a string.
    """
    return len(s)

def BaseConversion (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 4)
        nums.append(str(r))
    return ''.join(reversed(nums))

def run_program_base_4(current_sum):
    """
    Generates and processes the (a, b, c, d) quadruples up to max_sum such that a+b+c+d=n.
    """
    # Base 4 uses four digits (0, 1, 2, 3), so we now need quadruples (a, b, c, d)
    # The sum will be a + b + c + d = n.
    # This will be the main list, replacing the pandas DataFrame 'df'.
    # Inner list structure:
    # [a, b, c, d, Total, TotalDigits, Zeros4, Ones4, Twos4, Threes4, ZerosCount, OnesCount, TwosCount, ThreesCount]
    all_data = []

    print_num = 0
    all_counter = 0
    # The nested loops to generate the (a, b, c, d) quadruples
    for a in range(current_sum + 1):
        for b in range(current_sum + 1 - a):
            for c in range(current_sum + 1 - a - b):
                # d is the remainder to make the sum equal to current_sum
                d = current_sum - a - b - c

                # 1. Calculate derived values
                total = a + b + c + d # Redundant, but follows the original program structure

                # 2. Calculate base 4 representations (replacing .map(ternary))
                zeros4 = base_4_conversion(a)
                ones4 = base_4_conversion(b)
                twos4 = base_4_conversion(c)
                threes4 = base_4_conversion(d) # New variable for the fourth digit

                # 3. Calculate lengths
                zeros_count = length_of_string(zeros4)
                ones_count = length_of_string(ones4)
                twos_count = length_of_string(twos4)
                threes_count = length_of_string(threes4) # New count

                # 4. Calculate total digits
                total_digits = zeros_count + ones_count + twos_count + threes_count

                # Append the complete 'row' (list) to the main data list
                # Indices: 0-3: a, b, c, d; 4: Total; 5: TotalDigits
                row = [a, b, c, d, total, total_digits]
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
    TOTAL_INDEX = 4
    TOTAL_DIGITS_INDEX = 5

    for row in to_collapse:
        total_sum = row[TOTAL_INDEX]
        total_digits = row[TOTAL_DIGITS_INDEX]

        # Find the max TotalDigits for each Total sum
        if total_sum not in collapsed_data or total_digits > collapsed_data[total_sum]:
            collapsed_data[total_sum] = total_digits

    # --- CSV Output (Replacing .to_csv) ---

    # 1. Output for 'CollapsedOrderedBase4.csv' (equivalent to collapseddf)
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
    full_data = run_program_base_4(CurrentNumberToCheck)
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
        #!# (3/5) Note that we need to add another term each time
        #lastcheckcount = ogcount0 + maxrange*ogcount1 + maxrange*maxrange*ogcount2 + maxrange*maxrange*maxrange*ogcount3
        #!#
        ogcount0 = node[0]
        ogcount1 = node[1]
        ogcount2 = node[2]
        ogcount3 = node[3]
        
        count0 = ogcount0
        count1 = ogcount1
        count2 = ogcount2
        count3 = ogcount3
        
        tpcount0 = count0
        tpcount1 = count1
        tpcount2 = count2
        tpcount3 = count3
        
        BASEcount0 = int(BaseConversion(count0))
        BASEcount1 = int(BaseConversion(count1))
        BASEcount2 = int(BaseConversion(count2))
        BASEcount3 = int(BaseConversion(count3))
        BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3]
        counter_list = [count0,count1,count2,count3]
        if runcount == 1000000: #At 6 sec with (1000000).  Adding for 10min
            #print("Save")
            print(allcount)
            print(counter_list)
            runcount = 0
        digit_count = node[4]
        loseable_digits =  collapsed_data + 4
        lowest_possible_diagonal = digit_count - loseable_digits
        if lowest_possible_diagonal > last_good_Diagonal:
            print(lowest_possible_diagonal)
            print(loseable_digits)
            print(last_good_Diagonal)
            print("BROKEN")
            FullExit = 100000
            break
            Found_Bad = 1
        ogcounter_list = [count0,count1,count2,count3]
        Check_Exit = 0
        history_list = []
        while Check_Exit == 0:
            count0 = tpcount0
            count1 = tpcount1
            count2 = tpcount2
            count3 = tpcount3
            BASEcount0 = int(BaseConversion(count0))
            BASEcount1 = int(BaseConversion(count1))
            BASEcount2 = int(BaseConversion(count2))
            BASEcount3 = int(BaseConversion(count3))
            
            if not(BASEcounter_list in history_list):
                history_list.append(BASEcounter_list)
            counter_list = [count0,count1,count2,count3]
            BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3]
    
            #This removes one from each count if the digit is still there because it will need to be stated.
            if count0 >0:
                tpcount0 = count0 - 1
            if count1 >0:
                tpcount1 = count1 - 1
            if count2 >0:
                tpcount2 = count2 - 1
            if count3 >0:
                tpcount3 = count3 - 1
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
    
            if tpcount0< 0 or tpcount1<0 or tpcount2<0 or tpcount3<0:
                Check_Exit = 1
            #!# (4/5) Need to indent everythign after this and don't forget to add the extra term
            else:
                tp_Diagonal = tpcount0 + tpcount1 + tpcount2 + tpcount3
                if tp_Diagonal > last_good_Diagonal:
                    Check_Exit = 1
                    #print("Cantor:", CantorCount, counter_list, BASEcounter_list, " Reduced:", reducedCantorCount, [tpcount0,tpcount1,tpcount2])
                #!#
                else:
                    tpcounterlist = [tpcount0,tpcount1,tpcount2,tpcount3]
                    if not(BASEcounter_list in history_list):
                        history_list.append(BASEcounter_list)
                        #print(history_list)
                    if (tpcounterlist == [0,0,0,0] and Check_Exit==0):  #or (mylist in goodlist and Check_Exit ==0)
                        print("newgood")
                        print(history_list)
                        print(Exit)
                        file1 = open (folder + Base + '/Location.txt', 'w')
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
        ogcount0 = ogcount0 + 1
        if savecount == 1:
            savecount = 0
            csv_file = folder + Base + '/Data/Output Updating.csv'
        
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
    
    csv_file = folder+ Base + '/Data/Output Updating' + str(CurrentNumberToCheck) +'.csv'
    
    # Write the data to the CSV file
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(goodhistorylisttemp)
        file.close
    
    
    # Specify the CSV file name
    csv_file = folder+ Base + '/Data/Output Final' + str(CurrentNumberToCheck) + '.csv'
    
    # Write the data to the CSV file
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(goodhistorylist)
        file.close
    
    file1 = open (folder + Base + '/Data/LastGood.txt', 'w')
    Storage = (last_good_Diagonal, CurrentNumberToCheck)
    file1.write(str(Storage))
    file1.close()
    
    
    print(f"Data written to {csv_file}")
    
    print("End")
    CurrentNumberToCheck = CurrentNumberToCheck + 1


