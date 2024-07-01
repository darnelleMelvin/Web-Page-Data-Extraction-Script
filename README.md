# Web-Page-Data-Extraction-Script
This Python script reads a list of URLs from a spreadsheet, fetches the source code for each page, extracts multiple matches using a regular expression (regex) pattern, and writes the results to a new spreadsheet. Each match found on a page is written as a row in the output file.
## Prerequisites
Before you run the script, ensure you have the following installed:

* Python 3.x
* pandas library
* requests library
* openpyxl library

You can install the required libraries using pip:
~~~~
pip install pandas requests openpyxl
~~~~
## Script Explanation
The script performs the following steps:

1. Read URLs from the spreadsheet: It uses the pandas library to read URLs from the specified Excel file.
2. Fetch the web pages: It uses the requests library to retrieve the source code of each URL.
3. Extract data using regex: It uses the re library to find all matches in the source code based on the provided regex pattern.
4. Write the extracted data to a new spreadsheet: It uses the pandas library to write the results to a new Excel file.

## Customization
* Regex Pattern: Update the pattern variable with your desired regex pattern to extract specific data from the web pages.
* Input/Output Files: Adjust the file paths and names for the input (urls.xlsx) and output (extracted_data.xlsx) files as needed.

## License
Source code is made available under the [BSD 3-Clause License](LICENSE). For questions, contact [Darnelle Melvin](https://github.com/darnelleMelvin).
