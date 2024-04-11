# SBETET MARKS FETCHER

## About the Project

The SBETET_MARKS_FETCHER is a Python program designed to streamline the process of fetching class results from the Andhra Pradesh State Board of Technical Education and Training (SBTET) website. It automates the retrieval of student data and stores it in a structured format for easy access and analysis.

### Features:
- **Automation**: Utilizes Selenium framework to automate the process of accessing the SBTET website, entering PIN numbers, and retrieving results.
- **Data Extraction**: Extracts subject-wise marks, total marks, and pass/fail status for each student.
- **CSV Output**: Saves the retrieved data into a CSV file for further processing and analysis.

## Steps to Use this Program

1. **Download Python and Selenium**:
   - Download the latest version of Python.
   - Install the Selenium library using pip:
     ```python
     pip install selenium
     ```

2. **Download WebDriver**:
   - Depending on your browser, download the corresponding Selenium WebDriver from the following links:
     - [Chrome](https://chromedriver.chromium.org/downloads)
     - [Firefox](https://github.com/mozilla/geckodriver/releases)
     - [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
     - [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

3. **Setup WebDriver**:
   - After downloading, place the WebDriver executable in a new folder in the `C:/` drive.
   - Note down the path of this folder.

4. **Modify `main.py`**:
   - Open the [main.py](https://github.com/PavanTheHacker55/SBETET_MARKS_FETCHER/blob/main/main.py) file.
   - Make the following changes:
     - Replace `<your_browser_name>` with your browser name (all lowercase).
     - Adjust the number of students in your class at line 12.
     - Update `<your_branch_code>` and `<batch_code>` as per your institution's codes.
     - Replace `<driver_path>` with the path to the folder where you placed the WebDriver executable.
     - Modify subject codes at line 16 according to your semester.
     - Adjust URLs if you have more than 9 subjects in your semester.

5. **Save and Execute**:
   - Save the `main.py` file.
   - Execute the `main.py` file.

Done! 🎉
