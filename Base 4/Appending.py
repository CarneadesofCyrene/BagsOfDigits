# -*- coding: utf-8 -*-

#Combining
#Note, you need to copy the files from Data to To Append before running this program

import csv
import glob
import os
import re
from io import StringIO
BASEFolder = "Base 4/"

folder_to_process = 'BagsOfDigits/'+ BASEFolder + 'To Append' 
Output = "BagsOfDigits/"+ BASEFolder + "Output Final.csv"

# --- Configuration ---
FILE_ENCODING = 'latin-1' 
# ---------------------

# --- Helper Functions ---

def numerical_sort_key(filename):
    """
    Extracts the first sequence of digits from a filename and returns it 
    as an integer for true numerical sorting.
    """
    base_name = os.path.basename(filename)
    # Find all sequences of digits (numbers) in the filename
    parts = re.findall(r'(\d+)', base_name)
    # Return the first found number as an integer, or 0 if no number is found
    return int(parts[0]) if parts else 0

def find_delimiter(filename, enc):
    """Tries to sniff the delimiter, falling back to common options."""
    delimiters_to_check = [',', ';', '\t', '|'] 
    
    with open(filename, 'r', newline='', encoding=enc) as f:
        sample = f.read(2048)
        if not sample:
            return ','

        # Try Sniffer
        try:
            sniffed_delimiter = csv.Sniffer().sniff(sample).delimiter
            if sniffed_delimiter in delimiters_to_check:
                return sniffed_delimiter
        except Exception:
            pass

        # Manual checks: Find the delimiter that results in the most fields
        best_delimiter = ','
        max_fields = 1
        
        for delim in delimiters_to_check:
            try:
                reader = csv.reader(StringIO(sample), delimiter=delim)
                current_fields = 0
                for _ in range(5):
                    try:
                        row = next(reader)
                        current_fields = max(current_fields, len(row))
                    except StopIteration:
                        break

                if current_fields > max_fields:
                    max_fields = current_fields
                    best_delimiter = delim
            except Exception:
                continue

        return best_delimiter

# ---------------------------------------------------------------------

def append_variable_csvs_numerically(folder_path, output_filename="appended_data_numeric_sort.csv"):
    """
    Appends CSV files in true numerical order of filename, handling variable columns
    and padding shorter rows.
    """
    all_files = glob.glob(os.path.join(folder_path, "*.csv"))
    if not all_files:
        print(f"No CSV files found in the folder: {folder_path}")
        return

    # 🔑 KEY CHANGE: Sort the files using the numerical_sort_key function
    sorted_files = sorted(all_files, key=numerical_sort_key)
    
    print("Files will be processed in true numerical order:")
    print([os.path.basename(f) for f in sorted_files])

    # --- 1. First Pass: Determine Maximum Columns ---
    max_columns = 0
    print("\nStep 1: Analyzing files to determine maximum column count...")
    
    for filename in sorted_files:
        try:
            current_delimiter = find_delimiter(filename, FILE_ENCODING)
            with open(filename, 'r', newline='', encoding=FILE_ENCODING) as infile:
                reader = csv.reader(infile, delimiter=current_delimiter)
                for row in reader:
                    max_columns = max(max_columns, len(row))
        except Exception as e:
            print(f"  - WARNING: Could not analyze {os.path.basename(filename)}. Skipping analysis. Error: {e}")

    if max_columns == 0:
        print("ERROR: Could not read any data to determine column count.")
        return
    
    print(f"\nMaximum columns found across all files: {max_columns}")

    # --- 2. Second Pass: Read, Pad, and Write Data ---
    output_path = os.path.join(folder_path, output_filename)
    total_rows_added = 0
    
    with open(output_path, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        
        print("\nStep 2: Appending and padding data...")
        
        # Iterate over the *numerically sorted* list
        for filename in sorted_files:
            try:
                current_delimiter = find_delimiter(filename, FILE_ENCODING)
                rows_added = 0
                
                with open(filename, 'r', newline='', encoding=FILE_ENCODING) as infile:
                    reader = csv.reader(infile, delimiter=current_delimiter)
                    
                    for row in reader:
                        if not row:
                            continue
                            
                        # Padding Logic: Ensure every row has max_columns width
                        if len(row) < max_columns:
                            row.extend([''] * (max_columns - len(row)))
                            
                        writer.writerow(row)
                        rows_added += 1
                        
                    total_rows_added += rows_added
                    print(f"  - Appended {os.path.basename(filename)}: {rows_added} rows.")
                        
            except Exception as e:
                print(f"  - **ERROR**: Failed to process {os.path.basename(filename)}. Skipping. Error: {e}")

    # --- 3. Summary ---
    print("\n--- Summary ---")
    print(f"Successfully created a new file with {max_columns} fixed columns.")
    print(f"Total Rows Added to final file: {total_rows_added}")
    print(f"Saved to: {output_path}")





# Call the function
append_variable_csvs_numerically(folder_to_process, output_filename=Output)


