# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:30:55 2024

@author: dmelvin
"""

import pandas as pd
import requests
import re

# Read URLs from the spreadsheet
df = pd.read_excel('C:/Users/dmelvin/Documents/jackentratter.xlsx')  # Adjust the file path and sheet name as needed
urls = df['Link']  # Adjust the column name if needed

# Prepare a list to hold the extracted data
extracted_data = []

# Define your regex pattern
pattern = re.compile(r'\<a\shref\=\"(\/ark.*)\"\srel\=\"bookmark\"\>')  # Replace with your actual regex pattern

for url in urls:
    try:
        # Fetch the source code of the web page
        response = requests.get(url)
        response.raise_for_status()
        source_code = response.text

        # Find all matches using the regex pattern
        matches = pattern.findall(source_code)

        # Add each match as a row in the extracted data
        for match in matches:
            extracted_data.append([url, match])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Convert the extracted data to a DataFrame
result_df = pd.DataFrame(extracted_data, columns=['Link', 'Match'])

# Write the results to a new spreadsheet
result_df.to_excel('C:/Users/dmelvin/Documents/generateArk/extracted_data001.xlsx', index=False)  # Adjust the file path as needed

print("Data extraction complete. Check 'extracted_data001.xlsx' for the results.")
