# -*- coding: utf-8 -*-

import csv
import random
import ast
import os
Base = "Base 10/" # 1. Changed Base from "Base 9/" to "Base 10/"


#Main Computer 
folder = 'BagsOfDigits/'
extra = ''

with open(folder + Base + extra + '/LastGood.txt', 'r') as file:
    tuple_str = file.read()

# Using eval() to parse the string back into a tuple (use with caution)
retrieved_tuple = eval(tuple_str)
CurrentNumberToCheck = retrieved_tuple[1] + 1
ImportLastGoodDiagonal = retrieved_tuple[0]
last_good_Diagonal = ImportLastGoodDiagonal

# 2. Base Conversion functions are no longer needed, as we work in Base 10.

def length_of_string(n):
    """
    Returns the length of the string representation of a non-negative integer.
    """
    return len(str(n))

# 3. BaseConversion function is effectively replaced by str() for Base 10
def BaseConversion(n):
    """
    For Base 10, this simply converts the number to a string.
    """
    return str(n)


def run_program_base_10_collapse(current_sum): # 4. Renamed function from run_program_base_9_collapse
    """
    Generates and processes the (a, b, c, d, e, f, g, h, i, j) decuples up to max_sum such that a+b+c+d+e+f+g+h+i+j=n.
    """
    # Base 10 uses ten digits (0, 1, ..., 9), so we now need decuples (a, b, c, d, e, f, g, h, i, j)
    # a=Count of 0s, b=Count of 1s, ..., j=Count of 9s
    # The sum will be a + b + c + d + e + f + g + h + i + j = n.
    # Inner list structure:
    # [a, b, c, d, e, f, g, h, i, j, Total, TotalDigits]
    maximum_digits = 0

    print_num = 0
    all_counter = 0
    # 5. The nested loops to generate the (a, b, c, d, e, f, g, h, i, j) decuples (Added 'j' loop and calculation)
    for a in range(current_sum + 1):
        for b in range(current_sum + 1 - a):
            for c in range(current_sum + 1 - a - b):
                for d in range(current_sum + 1 - a - b - c):
                    for e in range(current_sum + 1 - a - b - c - d):
                        for f in range(current_sum + 1 - a - b - c - d - e):
                            for g in range(current_sum + 1 - a - b - c - d - e - f):
                                for h in range(current_sum + 1 - a - b - c - d - e - f - g):
                                    for i in range(current_sum + 1 - a - b - c - d - e - f - g - h):
                                        # j is the remainder to make the sum equal to current_sum
                                        j = current_sum - a - b - c - d - e - f - g - h - i # 6. Added variable j
                                        
                                        # 7. Base 10 representations are just the strings of the numbers
                                        zeros10 = str(a)
                                        ones10 = str(b)
                                        twos10 = str(c)
                                        threes10 = str(d) 
                                        fours10 = str(e)
                                        fives10 = str(f)
                                        sixes10 = str(g)
                                        sevens10 = str(h)
                                        eights10 = str(i)
                                        nines10 = str(j) # 8. Added variable for string of j
                                        
                                        # 9. Calculate lengths
                                        zeros_count = len(zeros10)
                                        ones_count = len(ones10)
                                        twos_count = len(twos10)
                                        threes_count = len(threes10)
                                        fours_count = len(fours10)
                                        fives_count = len(fives10)
                                        sixes_count = len(sixes10)
                                        sevens_count = len(sevens10)
                                        eights_count = len(eights10)
                                        nines_count = len(nines10) # 10. Added count for j
                                        
                                        # 11. Calculate total digits
                                        total_digits = zeros_count + ones_count + twos_count + threes_count + fours_count + fives_count + sixes_count + sevens_count + eights_count + nines_count
                                
                                        # 12. Update maximum_digits
                                        # Indices: 0-9: a, b, c, d, e, f, g, h, i, j; 10: Total; 11: TotalDigits
                                        if total_digits > maximum_digits:
                                            maximum_digits = total_digits
                                        
                                        # Check for progress print
                                        if print_num == 1000000:
                                            print(f"Processed: {current_sum}, Entries {all_counter}")
                                            print_num = 0
                                        print_num += 1
                                        all_counter += 1
    return(maximum_digits)

def run_program_base_10_generator(current_sum): # Renamed function from run_program_base_9_generator
    """
    (GENERATOR) Yields the (a, b, c, d, e, f, g, h, i, j) data rows up to current_sum.
    This saves memory by not storing all results in a list.
    """
    # Base 10 uses ten digits (0, 1, ..., 9), so we need decuples (a, b, c, d, e, f, g, h, i, j)
    # The sum will be a + b + c + d + e + f + g + h + i + j = current_sum.
    # Yielded data structure:
    # [a, b, c, d, e, f, g, h, i, j, Total, TotalDigits]

    # The nested loops to generate the (a, b, c, d, e, f, g, h, i, j) decuples
    for a in range(current_sum + 1):
        for b in range(current_sum + 1 - a):
            for c in range(current_sum + 1 - a - b):
                for d in range(current_sum + 1 - a - b - c):
                    for e in range(current_sum + 1 - a - b - c - d):
                        for f in range(current_sum + 1 - a - b - c - d - e):
                            for g in range(current_sum + 1 - a - b - c - d - e - f):
                                for h in range(current_sum + 1 - a - b - c - d - e - f - g):
                                    for i in range(current_sum + 1 - a - b - c - d - e - f - g - h):
                                        # j is the remainder to make the sum equal to current_sum
                                        j = current_sum - a - b - c - d - e - f - g - h - i
                                        
                                        # Calculate Base 10 representations (just the numbers as strings)
                                        # Note: 'zeros10' is just str(a), etc.
                                        
                                        # Calculate lengths
                                        zeros_count = length_of_string(a)
                                        ones_count = length_of_string(b)
                                        twos_count = length_of_string(c)
                                        threes_count = length_of_string(d) 
                                        fours_count = length_of_string(e)
                                        fives_count = length_of_string(f)
                                        sixes_count = length_of_string(g)
                                        sevens_count = length_of_string(h)
                                        eights_count = length_of_string(i)
                                        nines_count = length_of_string(j)
                                        
                                        # Calculate total digits
                                        total_digits = zeros_count + ones_count + twos_count + threes_count + fours_count + fives_count + sixes_count + sevens_count + eights_count + nines_count
                                        
                                        # YIELD the data row instead of appending to a list (added j, changed index for total_digits)
                                        row = [a, b, c, d, e, f, g, h, i, j, current_sum, total_digits] 
                                        yield row


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
    generator = run_program_base_10_generator(CurrentNumberToCheck)
    collapsed_data = run_program_base_10_collapse(CurrentNumberToCheck)
    
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
    Found_Bad = 0
    for i, node in enumerate(generator):
        runcount = runcount + 1
        allcount = allcount + 1
        
        # 13. Added ogcount9 and adjusted list indices
        ogcount0 = node[0]
        ogcount1 = node[1]
        ogcount2 = node[2]
        ogcount3 = node[3]
        ogcount4 = node[4]
        ogcount5 = node[5]
        ogcount6 = node[6]
        ogcount7 = node[7]
        ogcount8 = node[8]
        ogcount9 = node[9] 
        
        count0 = ogcount0
        count1 = ogcount1
        count2 = ogcount2
        count3 = ogcount3
        count4 = ogcount4
        count5 = ogcount5
        count6 = ogcount6
        count7 = ogcount7
        count8 = ogcount8
        count9 = ogcount9 # 14. Added count9
        
        tpcount0 = count0
        tpcount1 = count1
        tpcount2 = count2
        tpcount3 = count3
        tpcount4 = count4
        tpcount5 = count5
        tpcount6 = count6
        tpcount7 = count7
        tpcount8 = count8
        tpcount9 = count9 # 15. Added tpcount9
        
        # 16. For Base 10, BASEcount is just the number itself.
        BASEcount0 = count0 
        BASEcount1 = count1
        BASEcount2 = count2
        BASEcount3 = count3
        BASEcount4 = count4
        BASEcount5 = count5
        BASEcount6 = count6
        BASEcount7 = count7
        BASEcount8 = count8
        BASEcount9 = count9 # 17. Added BASEcount9
        
        BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3, BASEcount4, BASEcount5, BASEcount6, BASEcount7, BASEcount8, BASEcount9] # 18. Added BASEcount9
        counter_list = [count0,count1,count2,count3,count4, count5, count6, count7, count8, count9] # 19. Added count9
        if runcount == 1000000: 
            print(allcount)
            print(counter_list)
            runcount = 0
            
        digit_count = node[10] # 20. Index changed from 9 to 10 (Total sum)
        loseable_digits = collapsed_data + 10 # 21. Changed +9 to +10 for 10 digits
        lowest_possible_diagonal = digit_count - loseable_digits
        if lowest_possible_diagonal > last_good_Diagonal:
            print(lowest_possible_diagonal)
            print(loseable_digits)
            print(last_good_Diagonal)
            print("BROKEN")
            FullExit = 100000
            break
            Found_Bad = 1
            
        ogcounter_list = [count0,count1,count2,count3,count4, count5, count6, count7, count8, count9] # 22. Added count9
        Check_Exit = 0
        history_list = []
        while Check_Exit == 0:
            count0 = tpcount0
            count1 = tpcount1
            count2 = tpcount2
            count3 = tpcount3
            count4 = tpcount4
            count5 = tpcount5
            count6 = tpcount6
            count7 = tpcount7
            count8 = tpcount8
            count9 = tpcount9 # 23. Added count9
            
            # 24. For Base 10, BASEcount is just the number itself.
            BASEcount0 = count0 
            BASEcount1 = count1
            BASEcount2 = count2
            BASEcount3 = count3
            BASEcount4 = count4
            BASEcount5 = count5
            BASEcount6 = count6
            BASEcount7 = count7
            BASEcount8 = count8
            BASEcount9 = count9 # 25. Added BASEcount9
            
            if not(BASEcounter_list in history_list):
                history_list.append(BASEcounter_list)
            counter_list = [count0,count1,count2,count3,count4, count5, count6, count7, count8, count9] # 26. Added count9
            BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3,BASEcount4, BASEcount5, BASEcount6, BASEcount7, BASEcount8, BASEcount9] # 27. Added BASEcount9
            
            #This removes one from each count if the digit is still there because it will need to be stated.
            if count0 >0:
                tpcount0 = count0 - 1
            if count1 >0:
                tpcount1 = count1 - 1
            if count2 >0:
                tpcount2 = count2 - 1
            if count3 >0:
                tpcount3 = count3 - 1
            if count4 >0: 
                tpcount4 = count4 - 1
            if count5 >0: 
                tpcount5 = count5 - 1
            if count6 >0: 
                tpcount6 = count6 - 1
            if count7 >0: 
                tpcount7 = count7 - 1
            if count8 >0: 
                tpcount8 = count8 - 1
            if count9 >0: # 28. Added count9 logic
                tpcount9 = count9 - 1
                
            # This drops zeros, then it splits all the remaining numbers into digits.
            nozerolist = remove_zeros(BASEcounter_list, 0)
            splitlist = split_into_digits(nozerolist)
            
            #This counts the number of zero digits (0 through 9)
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
                            if tpcount4 < 0:
                                Check_Exit = 1
                            else:
                                spcount5 = splitlist.count(5)
                                tpcount5 = tpcount5 - spcount5
                                if tpcount5 < 0:
                                    Check_Exit = 1
                                else:
                                    spcount6 = splitlist.count(6)
                                    tpcount6 = tpcount6 - spcount6
                                    if tpcount6 < 0:
                                        Check_Exit = 1
                                    else:
                                        spcount7 = splitlist.count(7)
                                        tpcount7 = tpcount7 - spcount7
                                        if tpcount7 < 0:
                                            Check_Exit = 1
                                        else:
                                            spcount8 = splitlist.count(8)
                                            tpcount8 = tpcount8 - spcount8
                                            if tpcount8 < 0: # 29. Added check for tpcount8
                                                Check_Exit = 1
                                            else:
                                                spcount9 = splitlist.count(9) # 30. Added check for spcount9 and tpcount9
                                                tpcount9 = tpcount9 - spcount9
            
            if tpcount0< 0 or tpcount1<0 or tpcount2<0 or tpcount3<0 or tpcount4<0 or tpcount5<0 or tpcount6<0 or tpcount7<0 or tpcount8<0 or tpcount9<0: # 31. Added tpcount9 check
                Check_Exit = 1
            
            else:
                tp_Diagonal = tpcount0 + tpcount1 + tpcount2 + tpcount3 + tpcount4 + tpcount5 + tpcount6 + tpcount7 + tpcount8 + tpcount9 # 32. Added tpcount9 to diagonal sum
                if tp_Diagonal > last_good_Diagonal:
                    Check_Exit = 1
                
                else:
                    tpcounterlist = [tpcount0,tpcount1,tpcount2,tpcount3,tpcount4,tpcount5,tpcount6,tpcount7,tpcount8,tpcount9] # 33. Added tpcount9
                    if not(BASEcounter_list in history_list):
                        history_list.append(BASEcounter_list)
                    if (tpcounterlist == [0,0,0,0,0,0,0,0,0,0] and Check_Exit==0):  # 34. Final zero check
                        print("newgood")
                        print(history_list)
                        print(Exit)
                        file1 = open (folder + Base + extra + '/Location.txt', 'w')
                        file1.write(str(counter_list))
                        file1.close()
                        
                        last_good_Diagonal = digit_count
                        
                        if not(ogcounter_list in goodcounterlist):
                            for old_list in history_list:
                                goodcounterlist.append(old_list)
                            goodhistorylist.append(history_list)
                            goodhistorylisttemp.append(history_list)
                            Exit = Exit + 1
                            savecount = savecount + 1
                        Check_Exit = 1
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