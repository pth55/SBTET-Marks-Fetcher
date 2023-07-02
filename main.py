import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

filename = "./result.csv"
droppers_list = [] # list for storing uneligible pin numbers
start_roll_no = 1
end_roll_no = 131
branch_code = 'CM'
clg_code = '20158'
with open(filename, "w+") as f:
	header = "PIN,501,502,503,504,505,506,507,508,509,TOTAL,STATUS\n"
	f.write(header)

for i in range(start_roll_no, end_roll_no + 1):
	try:
		# create instance of Chrome webdriver
		firefox_services = Service(executable_path="C:/SWSetup/geckodriver.exe")
		driver = webdriver.Firefox(service = firefox_services)
		# driver.get("https://sbtetuat.ap.gov.in/APSBTET/results.do")
		driver.minimize_window() #to minimize the window when a selenium session is created
		driver.get("https://sbtet1.ap.gov.in/APSBTET/results.xls")

		if i<10:
			tv = clg_code+'-'+branch_code+'-00'+str(i)
		elif i>=10 and i<=99:
			tv= clg_code+'-'+branch_code+'-0'+str(i)
		else:
			tv = clg_code+'-'+branch_code+'-'+str(i)

		# PIN
		driver.find_element('xpath', '//*[@id="aadhar1"]').send_keys(tv)
		
		# SEM
		# /html/body/div[3]/div/div/div[2]/div/form/div[2]/div/div/select/option[<sem-number>]
		driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/div[2]/div/div/select/option[5]').click()
		
		# SUBMIT
		driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/div[3]/div/input').click()
		
		# PIN
		pin = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[1]/td[1]').text
		#name=driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[2]/td').text
		
		#SEBJECTS 501 to 509
		sub_1 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[5]/td[1]').text
		sub_2 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[6]/td[1]').text
		sub_3 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[7]/td[1]').text
		sub_4 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[8]/td[1]').text
		sub_5 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[9]/td[1]').text
		sub_6 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[10]/td[1]').text
		sub_7 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[11]/td[1]').text
		sub_8 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[12]/td[1]').text
		sub_9 = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[13]/td[1]').text
		
		# TOTAL MARKS
		total = driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[14]/td').text
		# STATUS PASS/FAIL
		status=driver.find_element('xpath', '/html/body/div[3]/div/div/div[2]/div/form/table/tbody/tr[15]/td').text
		
		with open("result.csv","a") as f:
			f.write(pin + "," + sub_1 + ","+ sub_2 + "," + sub_3 + "," + sub_4 + "," + sub_5 + "," + sub_6 + "," + sub_7 + "," + sub_8 + "," + sub_9 + "," + total + "," + status + "\n")
		
		# close the web driver
		driver.close()

		# printing the success msg!
		print("["+tv+"]==>Results Fetched Successfully")

	except Exception as exception:
		# if any number dos't exist then, it will add that number to seprate list
		droppers_list.append(tv)
		driver.close()
		continue


print("These Numbers are does't exist..")
for i in droppers_list:
	print(i)