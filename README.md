# Web-Page-Data-Extraction-Script
This Python script reads a list of URLs from a spreadsheet, fetches the source code for each page, extracts multiple matches using a regular expression (regex) pattern, and writes the results to a new spreadsheet. Each match found on a page is written as a row in the output file.
## Prerequisites
Before you run the script, ensure you have the following installed:

* Python 3.x
* __`pandas`__ library
* __`requests`__ library
* __`openpyxl`__ library

You can install the required libraries using pip:
~~~~
pip install pandas requests openpyxl
~~~~
## Script Explanation
The script performs the following steps:

1. __Read URLs from the spreadsheet__: It uses the __`pandas`__ library to read URLs from the specified Excel file.
2. __Fetch the web pages__: It uses the __`requests`__ library to retrieve the source code of each URL.
3. __Extract data using regex__: It uses the __`re`__ library to find all matches in the source code based on the provided regex pattern.
4. __Write the extracted data to a new spreadsheet__: It uses the __`pandas`__ library to write the results to a new Excel file.

## Customization
* __Regex Pattern__: Update the __`pattern`__ variable with your desired regex pattern to extract specific data from the web pages.
* __Input/Output Files__: Adjust the file paths and names for the input (__`urls.xlsx`__) and output (__`extracted_data.xlsx`__) files as needed.

## Contact
If you encounter any issues or have questions, feel free to open an issue or contact contact [Darnelle Melvin](https://github.com/darnelleMelvin).

## License
Source code is made available under the [BSD 3-Clause License](LICENSE).
