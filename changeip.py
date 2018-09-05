from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sys import exit
import socket

def ip_to_2():
    try:
        edit_ip_i = driver.find_element_by_name("startIp")
        edit_ip_ii = driver.find_element_by_name("endIp")
        ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")
        edit_ip_i.clear()
        edit_ip_ii.clear()
        edit_ip_i.send_keys('192.168.10.2')
        edit_ip_ii.send_keys('2')
        ok_button.click()

        edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
        edit_button_1.click()
        edit_ip_i = driver.find_element_by_name("startIp")
        edit_ip_ii = driver.find_element_by_name("endIp")
        ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")

        edit_ip_i.clear()
        edit_ip_ii.clear()
        edit_ip_i.send_keys('192.168.10.20')
        edit_ip_ii.send_keys('20')
        ok_button.click()

    except:
        print("Warning ip mis-spelled")
        driver.get('http://192.168.10.1/qoscfg.html')
        edit_ip_i = driver.find_element_by_name("startIp")
        edit_ip_ii = driver.find_element_by_name("endIp")
        ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")
        edit_ip_i.clear()
        edit_ip_ii.clear()
        edit_ip_i.send_keys('192.168.10.20')
        edit_ip_ii.send_keys('20')
        ok_button.click()

        edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
        edit_button_1.click()
        edit_ip_i = driver.find_element_by_name("startIp")
        edit_ip_ii = driver.find_element_by_name("endIp")
        ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")

        edit_ip_i.clear()
        edit_ip_ii.clear()
        edit_ip_i.send_keys('192.168.10.2')
        edit_ip_ii.send_keys('2')
        ok_button.click()
##Getting the Ip and processing it
try:
    ip_adrss=socket.gethostbyname(socket.gethostname())
except Exception as e:
    print(e)
    print("")
    print("Ip adress couldnt be found check internet connection")
    x=input("Press any key to quit")
    quit()

len_ip_adrss=len(ip_adrss)

if len_ip_adrss==12:
    ip_adrss_no=ip_adrss[11]

elif len_ip_adrss==13:
    ip_adrss_no=ip_adrss[11]+ip_adrss[12]
else:
    print("Ip adress couldnt be found check internet connection")
    x=input("Press any key to quit")
    quit()

print(ip_adrss)

##Starting the browser

driver=webdriver.Firefox()
driver.get('http://192.168.10.1/login.html')

##Login Screen

id_box = driver.find_element_by_id('username')
id_box.send_keys('admin')
id_box2 = driver.find_element_by_id('password')
id_box2.send_keys('Change this to your admin password')##Change this to your own password

login_button = driver.find_element_by_name('button')
login_button.click()

driver.get('http://192.168.10.1/main.html')
#class_select = driver.find_element_by_class_name('menuLink')
#class_select.click()

driver.get('http://192.168.10.1/qoscfg.html')


##Starting the ip Change
edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
edit_button_1.click()

edit_ip_i = driver.find_element_by_name("startIp")
edit_ip_ii = driver.find_element_by_name("endIp")
ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")
apply_button=driver.find_element_by_xpath("/html/body/blockquote/form/center/input")

if ip_adrss_no=='2':
    ip_to_2()

    edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
    edit_button_1.click()
    edit_ip_i.clear()
    edit_ip_ii.clear()
    edit_ip_i.send_keys('192.168.10.3')
    edit_ip_ii.send_keys('3')
    ok_button.click()

    edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
    edit_button_1.click()
    edit_ip_i = driver.find_element_by_name("startIp")
    edit_ip_ii = driver.find_element_by_name("endIp")
    ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")

    edit_ip_i.clear()
    edit_ip_ii.clear()
    edit_ip_i.send_keys('192.168.10.4')
    edit_ip_ii.send_keys('20')
    ok_button.click()
    apply_button.click()

else:
    ip_to_2()

    edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
    edit_button_1.click()
    edit_ip_i.clear()
    edit_ip_ii.clear()
    edit_ip_i.send_keys('192.168.10.2')
    ip_adrss_no=int(ip_adrss_no)
    low_no=ip_adrss_no-1
    high_no=ip_adrss_no+1
    edit_ip_ii.send_keys(str(low_no))
    ok_button.click()

    edit_button_1 = driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/table[@class='table']/tbody[@id='ctrlTable']/tr[2]/td[7]/button[1]")
    edit_button_1.click()
    edit_ip_i = driver.find_element_by_name("startIp")
    edit_ip_ii = driver.find_element_by_name("endIp")
    ok_button=driver.find_element_by_xpath("/html/body/blockquote/form/div[@id='netCtrl']/p/button[@id='addqos']")

    edit_ip_i.clear()
    edit_ip_ii.clear()
    edit_ip_i.send_keys('192.168.10.'+str(high_no))
    edit_ip_ii.send_keys('20')
    ok_button.click()
    apply_button.click()
print("Ip Changed Successfully")
x=input("Do you want a speed check (y/n)")
if x=='y' or x=='Y':
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.get('http://fast.com/')
x=input("Press any key to quit")
driver.quit()
exit()
