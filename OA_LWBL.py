#coding=gbk
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


#test_log = open("C:/Users/hyasn/Desktop/test_log.txt","a+")
browser = webdriver.Chrome("E:\SetupMenu\Anaconda\chromedriver.exe") # Get local session of Chrome
browser.get("http://19.16.104.13:8080/default/index/indexBlue/index.jsp#") # Load page
assert "广东省国土资源厅政务办公系统" in browser.title

username = "cxh"  #用户名
password = "000000"	#用户密码
input_username = browser.find_element_by_name("userId") # 通过ID获取用户名输入框
input_username.send_keys(username)	#输入用户名
input_password = browser.find_element_by_name("password")	#通过名称获取密码输入框
input_password.send_keys(password)	#输入密码

input_submit = browser.find_element_by_class_name("loginBtn")	#通过名称获取登录按钮
input_submit.click()	#单击登录

#assert "注销" in browser.find_element_by_class_name("login_out").title
#print(username+"登录成功")
#test_log.write(username + "登录成功\n")

# 点击公文管理
gwbl = browser.find_element_by_class_name("g-pt-gwbl")
gwbl.click()

# 点击发起公文										
fqgw = browser.find_element_by_class_name("g-pt-fqgw")
fqgw.click()

# 点击来文办理
lwbl = browser.find_element_by_class_name("g-pt-lwbl")
lwbl.click()

#切换标签页
# browser.switch_to.window("来文办理")
for handle in browser.window_handles:
   browser.switch_to.window(handle)
   #print(browser.title)

inputBt = browser.find_element_by_name("lwdj.bt")
inputBt.send_keys("来文标题")  
time.sleep(10) 
# 上传附件
uploadFile = browser.find_element_by_class_name("diyBtnAdd")
uploadFile.click()
time.sleep(10)
# 选择文件
pickfile = browser.find_element_by_id("picker")
pickfile.click()

#time.sleep(0.2) # Let the page load, will be added to the API
#登出
#browser.get("http://172.16.101.18:8080/default/coframe/auth/login/login.jsp")	#登出
#print(username+"登出")
#test_log.write(username + "登出\n")

#test_log.close()
#try:
#    browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
#except NoSuchElementException:
#    assert 0, "can't find seleniumhq"
#browser.close()