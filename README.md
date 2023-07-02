# About the Project
This Program will automatically fetches all the results of a class, this program built with Selenium framework...

## Steps to Use this Program
1. Download the latest version of Python along with selenium library using PIP as follows
```python
pip install selenium
```
2. Now Based on the Browser that you are currently using, Download the latest version of selenium webdriver (every web browser have its own selenium driver) from below links.<br>
   Download Drivers from here 👇</br>
   o [Chrome](https://chromedriver.chromium.org/downloads)<br>
   o [Firefox](https://github.com/mozilla/geckodriver/releases)<br>
   o [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)<br>
   o [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)<br>
4. After Downloding is completed, place the downloaded selenium executable file in ```C:/``` drive by creating a new folder and make sure to copy the path of that folder. 
5. if you done with step 3, Now Open the [main.py](https://github.com/PavanTheHacker55/SBETET_MARKS_FETCHER/blob/main/main.py) file and make the following changes... <br>
   🔰 At line 4 replace ```<your_browser_name>``` with your browser name (Note: all letters must be smallcase).<br>
   🔰 At line 12 change the value to no.of students in your class (simply, strenght of your section), at line 11 don't modify the value 😅. </br>
   🔰 At line 13 change the ```<your_branch_code>``` value accordingly, and at line 14 replace ```<batch_code>``` with your college code (batch code). </br>
   🔰 At line 15 replace the ```<driver_path>``` with the path that you have copied in step 4.<br>
   🔰 At line 16 change the subject codes according to your semester (don't change other values like PIN, TOTAL, STATUS). <br>
   🔰 At line 24 replace ```<Browser_name>``` with Your Browser name (Note: First letter of Browser name must be capital).<br>
   🔰 In your semester if you have only 5 thoery subjects and 4 practical subjects, you're good to go, continue with step 6.
   if you have more than 9 subjects in your semester you have to modify some URLs from line 58, and you have change the code accordingly, suppose if you have 10 subjects in your semester, already 9 subjects are added in the code now you have to create a new variable ```sub_10``` at line 59 and copy paste the same content from above line, but change number 13 to 14 in that URL. once you do that now you have to update the numbers at line 61 (change value in url from 14 to 15) and line 63 (change value in url from 15 to 16), and you have to update the line 66 too. 
6. Now Save the main.py file
7. Then execute the main.py file
Done!
