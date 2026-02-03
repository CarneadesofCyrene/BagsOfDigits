# -*- coding: utf-8 -*-



import csv
import random
import ast
import os
Base = "Base 9/" # 1. Changed Base from "Base 8/" to "Base 9/"


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


def base_9_conversion(n): # 2. Renamed function from base_8_conversion
    """
    Converts a non-negative integer to its nonary (base-9) string representation.
    """
    if n == 0:
        return '0'
    nums = []
    temp_n = abs(n)
    while temp_n:
        # 3. Change the base from 8 to 9
        temp_n, r = divmod(temp_n, 9)
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
        # 4. Change the base from 8 to 9
        n, r = divmod(n, 9)
        nums.append(str(r))
    return ''.join(reversed(nums))

def run_program_base_9_collapse(current_sum): # 5. Renamed function from run_program_base_8_collapse
    """
    Generates and processes the (a, b, c, d, e, f, g, h, i) nonuples up to max_sum such that a+b+c+d+e+f+g+h+i=n.
    """
    # Base 9 uses nine digits (0, 1, 2, 3, 4, 5, 6, 7, 8), so we now need nonuples (a, b, c, d, e, f, g, h, i)
    # The sum will be a + b + c + d + e + f + g + h + i = n.
    # Inner list structure:
    # [a, b, c, d, e, f, g, h, i, Total, TotalDigits, Zeros9..Eights9, ZerosCount..EightsCount]
    maximum_digits = 0

    print_num = 0
    all_counter = 0
    # 6. The nested loops to generate the (a, b, c, d, e, f, g, h, i) nonuples (Added 'i' loop and calculation)
    for a in range(current_sum + 1):
        for b in range(current_sum + 1 - a):
            for c in range(current_sum + 1 - a - b):
                for d in range(current_sum + 1 - a - b - c):
                    for e in range(current_sum + 1 - a - b - c - d):
                        for f in range(current_sum + 1 - a - b - c - d - e):
                            for g in range(current_sum + 1 - a - b - c - d - e - f):
                                for h in range(current_sum + 1 - a - b - c - d - e - f - g):
                                    # i is the remainder to make the sum equal to current_sum
                                    i = current_sum - a - b - c - d - e - f - g - h # 7. Added variable i
                                    
                                    # 8. Calculate base 9 representations (renamed function and added 'i')
                                    zeros9 = base_9_conversion(a)
                                    ones9 = base_9_conversion(b)
                                    twos9 = base_9_conversion(c)
                                    threes9 = base_9_conversion(d) 
                                    fours9 = base_9_conversion(e)
                                    fives9 = base_9_conversion(f)
                                    sixes9 = base_9_conversion(g)
                                    sevens9 = base_9_conversion(h)
                                    eights9 = base_9_conversion(i) # 9. Added variable for base 9 of i
                                    
                                    # 10. Calculate lengths (added 'i')
                                    zeros_count = length_of_string(zeros9)
                                    ones_count = length_of_string(ones9)
                                    twos_count = length_of_string(twos9)
                                    threes_count = length_of_string(threes9)
                                    fours_count = length_of_string(fours9)
                                    fives_count = length_of_string(fives9)
                                    sixes_count = length_of_string(sixes9)
                                    sevens_count = length_of_string(sevens9)
                                    eights_count = length_of_string(eights9) # 11. Added count for i
                                    
                                    # 12. Calculate total digits (added eighth count)
                                    total_digits = zeros_count + ones_count + twos_count + threes_count + fours_count + fives_count + sixes_count + sevens_count + eights_count
                            
                                    # 13. Append the complete 'row' (list) to the main data list (added i)
                                    # Indices: 0-8: a, b, c, d, e, f, g, h, i; 9: Total; 10: TotalDigits
                                    if total_digits > maximum_digits:
                                        maximum_digits = total_digits
                                    
                                    # Check for progress print
                                    if print_num == 1000000:
                                        print(f"Processed: {current_sum}, Entries {all_counter}")
                                        print_num = 0
                                    print_num += 1
                                    all_counter += 1
    return(maximum_digits)

def run_program_base_9_generator(current_sum): # Renamed function from run_program_base_8_generator
    """
    (GENERATOR) Yields the (a, b, c, d, e, f, g, h, i) data rows up to current_sum.
    This saves memory by not storing all results in a list.
    """
    # Base 9 uses nine digits (0, 1, 2, 3, 4, 5, 6, 7, 8), so we need nonuples (a, b, c, d, e, f, g, h, i)
    # The sum will be a + b + c + d + e + f + g + h + i = current_sum.
    # Yielded data structure:
    # [a, b, c, d, e, f, g, h, i, Total, TotalDigits]

    # The nested loops to generate the (a, b, c, d, e, f, g, h, i) nonuples
    for a in range(current_sum + 1):
        for b in range(current_sum + 1 - a):
            for c in range(current_sum + 1 - a - b):
                for d in range(current_sum + 1 - a - b - c):
                    for e in range(current_sum + 1 - a - b - c - d):
                        for f in range(current_sum + 1 - a - b - c - d - e):
                            for g in range(current_sum + 1 - a - b - c - d - e - f):
                                for h in range(current_sum + 1 - a - b - c - d - e - f - g):
                                    # i is the remainder to make the sum equal to current_sum
                                    i = current_sum - a - b - c - d - e - f - g - h
                                    
                                    # Calculate base 9 representations
                                    zeros9 = base_9_conversion(a)
                                    ones9 = base_9_conversion(b)
                                    twos9 = base_9_conversion(c)
                                    threes9 = base_9_conversion(d) 
                                    fours9 = base_9_conversion(e)
                                    fives9 = base_9_conversion(f)
                                    sixes9 = base_9_conversion(g)
                                    sevens9 = base_9_conversion(h)
                                    eights9 = base_9_conversion(i)
                                    
                                    # Calculate lengths
                                    zeros_count = length_of_string(zeros9)
                                    ones_count = length_of_string(ones9)
                                    twos_count = length_of_string(twos9)
                                    threes_count = length_of_string(threes9)
                                    fours_count = length_of_string(fours9)
                                    fives_count = length_of_string(fives9)
                                    sixes_count = length_of_string(sixes9)
                                    sevens_count = length_of_string(sevens9)
                                    eights_count = length_of_string(eights9)
                                    
                                    # Calculate total digits
                                    total_digits = zeros_count + ones_count + twos_count + threes_count + fours_count + fives_count + sixes_count + sevens_count + eights_count
                                    
                                    # YIELD the data row instead of appending to a list (added i, changed index for total_digits)
                                    row = [a, b, c, d, e, f, g, h, i, current_sum, total_digits] 
                                    yield row




# def collapsing(to_collapse):
#      # --- Data Summarization (Replacing GroupBy and Max) ---
#      collapsed_data = {}

#      # 14. The column indices for Total (9) and TotalDigits (10) in the all_data list
#      TOTAL_INDEX = 9 
#      TOTAL_DIGITS_INDEX = 10

#      for row in to_collapse:
#          total_sum = row[TOTAL_INDEX]
#          total_digits = row[TOTAL_DIGITS_INDEX]

#          # Find the max TotalDigits for each Total sum
#          if total_sum not in collapsed_data or total_digits > collapsed_data[total_sum]:
#              collapsed_data[total_sum] = total_digits

#      # --- CSV Output (Replacing .to_csv) ---

#      # 15. Output for 'CollapsedOrderedBase9.csv' 
#      collapsed_rows = [['Total', 'TotalDigits']] + [[k, v] for k, v in collapsed_data.items()]

#      # Sort by 'Total'
#      collapsed_rows[1:] = sorted(collapsed_rows[1:], key=lambda x: x[0])
#      return(collapsed_rows[1][1])

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
    #full_data = run_program_base_9(CurrentNumberToCheck) # 16. Renamed function
    #collapsed_data = collapsing(full_data)
    generator = run_program_base_9_generator(CurrentNumberToCheck)
    collapsed_data = run_program_base_9_collapse(CurrentNumberToCheck)
    
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
        
        # 17. Added ogcount7 and ogcount8 and adjusted list indices
        ogcount0 = node[0]
        ogcount1 = node[1]
        ogcount2 = node[2]
        ogcount3 = node[3]
        ogcount4 = node[4]
        ogcount5 = node[5]
        ogcount6 = node[6]
        ogcount7 = node[7]
        ogcount8 = node[8] 
        
        count0 = ogcount0
        count1 = ogcount1
        count2 = ogcount2
        count3 = ogcount3
        count4 = ogcount4
        count5 = ogcount5
        count6 = ogcount6
        count7 = ogcount7
        count8 = ogcount8 # 18. Added count8
        
        tpcount0 = count0
        tpcount1 = count1
        tpcount2 = count2
        tpcount3 = count3
        tpcount4 = count4
        tpcount5 = count5
        tpcount6 = count6
        tpcount7 = count7
        tpcount8 = count8 # 19. Added tpcount8
        
        BASEcount0 = int(BaseConversion(count0))
        BASEcount1 = int(BaseConversion(count1))
        BASEcount2 = int(BaseConversion(count2))
        BASEcount3 = int(BaseConversion(count3))
        BASEcount4 = int(BaseConversion(count4))
        BASEcount5 = int(BaseConversion(count5))
        BASEcount6 = int(BaseConversion(count6))
        BASEcount7 = int(BaseConversion(count7))
        BASEcount8 = int(BaseConversion(count8)) # 20. Added BASEcount8
        
        BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3, BASEcount4, BASEcount5, BASEcount6, BASEcount7, BASEcount8] # 21. Added BASEcount8
        counter_list = [count0,count1,count2,count3,count4, count5, count6, count7, count8] # 22. Added count8
        if runcount == 1000000: #At 6 sec with (1000000).  Adding for 10min
            #print("Save")
            print(allcount)
            print(counter_list)
            runcount = 0
            
        digit_count = node[9] # 23. Index changed from 8 to 9
        loseable_digits = collapsed_data + 9 # 24. Changed +8 to +9 for 9 digits
        lowest_possible_diagonal = digit_count - loseable_digits
        if lowest_possible_diagonal > last_good_Diagonal:
            print(lowest_possible_diagonal)
            print(loseable_digits)
            print(last_good_Diagonal)
            print("BROKEN")
            FullExit = 100000
            break
            Found_Bad = 1
            
        ogcounter_list = [count0,count1,count2,count3,count4, count5, count6, count7, count8] # 25. Added count8
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
            count8 = tpcount8 # 26. Added count8
            
            BASEcount0 = int(BaseConversion(count0))
            BASEcount1 = int(BaseConversion(count1))
            BASEcount2 = int(BaseConversion(count2))
            BASEcount3 = int(BaseConversion(count3))
            BASEcount4 = int(BaseConversion(count4))
            BASEcount5 = int(BaseConversion(count5))
            BASEcount6 = int(BaseConversion(count6))
            BASEcount7 = int(BaseConversion(count7))
            BASEcount8 = int(BaseConversion(count8)) # 27. Added BASEcount8
            
            if not(BASEcounter_list in history_list):
                history_list.append(BASEcounter_list)
            counter_list = [count0,count1,count2,count3,count4, count5, count6, count7, count8] # 28. Added count8
            BASEcounter_list = [BASEcount0,BASEcount1,BASEcount2,BASEcount3,BASEcount4, BASEcount5, BASEcount6, BASEcount7, BASEcount8] # 29. Added BASEcount8
            
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
            if count8 >0: # 30. Added count8 logic
                tpcount8 = count8 - 1
                
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
                                        if tpcount7 < 0: # 31. Added check for tpcount7
                                            Check_Exit = 1
                                        else:
                                            spcount8 = splitlist.count(8) # 32. Added check for spcount8 and tpcount8
                                            tpcount8 = tpcount8 - spcount8
            
            if tpcount0< 0 or tpcount1<0 or tpcount2<0 or tpcount3<0 or tpcount4<0 or tpcount5<0 or tpcount6<0 or tpcount7<0 or tpcount8<0: # 33. Added tpcount8 check
                Check_Exit = 1
            
            else:
                tp_Diagonal = tpcount0 + tpcount1 + tpcount2 + tpcount3 + tpcount4 + tpcount5 + tpcount6 + tpcount7 + tpcount8 # 34. Added tpcount8 to diagonal sum
                if tp_Diagonal > last_good_Diagonal:
                    Check_Exit = 1
                    #print("Cantor:", CantorCount, counter_list, BASEcounter_list, " Reduced:", reducedCantorCount, [tpcount0,tpcount1,tpcount2])
                
                else:
                    tpcounterlist = [tpcount0,tpcount1,tpcount2,tpcount3,tpcount4,tpcount5,tpcount6,tpcount7,tpcount8] # 35. Added tpcount8
                    if not(BASEcounter_list in history_list):
                        history_list.append(BASEcounter_list)
                        #print(history_list)
                    if (tpcounterlist == [0,0,0,0,0,0,0,0,0] and Check_Exit==0):  # 36. Added final zero
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