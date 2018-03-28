#coding=u8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import datetime


###打开浏览器并进入OA登录页面###
browser = webdriver.Chrome()
origin_window = browser.current_window_handle
browser.get("http://172.16.101.18:8080/default/index/indexBlue/index.jsp#") 
###登录用户###
username = "wt"  
password = "000000\n"	
input_username = browser.find_element_by_name("userId") 
input_username.send_keys(username)	
input_password = browser.find_element_by_name("password")
input_password.send_keys(password)	
###发起用章申请###
browser.find_element_by_class_name("g-pt-jgsw").click()
time.sleep(5)
browser.find_element_by_class_name("g-pt-yzgl").click()
time.sleep(5)
browser.find_element_by_class_name("g-pt-yzsq").click()
time.sleep(5)

def switch_window(browser):
	for handle in browser.window_handles:
   		browser.switch_to.window(handle)
   #print(browser.title)
switch_window(browser)
#browser.close()

yzsq_name = "用章申请"+datetime.datetime.now().strftime('%m%d%H%M')
#yzsqbt = "用章申请"+time.strftime('%m%d%H%M',time.localtime(time.time()))
browser.find_element_by_name("yzsq.bt").send_keys(yzsq_name)
browser.find_element_by_name("yzsq.yznr").send_keys("无")
#公章类型下拉
browser.find_element_by_xpath("//table[@class='formTable baseInfoTable']/tbody/tr[3]//input[@class='mini-buttonedit-input']").click()
#选择厅章
browser.find_element_by_xpath("//table[@class='mini-listbox-items']/tbody//tr[@index='1']").click()
'''
#打开附件上传
browser.find_element_by_class_name("diyBtnAdd").click()
#time.sleep(10)
#切换至附件上传窗口
browser.switch_to.frame(browser.find_element_by_xpath("//div[@class='mini-panel-viewport']//iframe"))
#点击选择文件
#browser.find_element_by_id("picker").click()
browser.find_element_by_name("file").send_keys("E:\万物\政务系统所有文件\OA系统文档合集\测试脚本及测试结果\测试文本txt.txt")
browser.find_element_by_id("btnUpload").click()
#关闭附件上传
browser.switch_to_default_content()
browser.find_element_by_class_name("mini-tools-close").click()
'''
#
#提交表单
#browser.find_element_by_class_name("g-btn-save").click()
browser.find_element_by_class_name("g-btn-submit").click()
time.sleep(5)
#切换至iframe
browser.switch_to.frame(browser.find_element_by_xpath("//div[@class='mini-panel-body']/iframe"))
browser.find_element_by_link_text("确定").click()
#browser.switch_to_default_content()

#切换用户
browser.switch_to.window(origin_window)

def switch_user(username,browser):
	#for handle in browser.window_handles:
		#browser.switch_to.window(handle)
	browser.get("http://172.16.101.18:8080/default/coframe/auth/login/login.jsp")
	browser.find_element_by_name("userId").send_keys(username)	
	browser.find_element_by_name("password").send_keys("000000\n")

switch_user("xjh",browser)

##################################################
###处室审核###
#进入工作中心
browser.find_element_by_class_name("g-pt-gzzx").click()
#搜索案卷
browser.switch_to.frame(browser.find_element_by_xpath("//div[@id='tabPage_dbj']/iframe"))
browser.find_element_by_id("search-input").send_keys(yzsq_name)
browser.find_element_by_class_name("search-btn").click()
time.sleep(3)
#进入案卷
#browser.find_element_by_xpath("//table[@id='resultList']//a[@title=yzsq_name]").click()#有问题
browser.find_element_by_link_text(yzsq_name).click()
time.sleep(5)
#切换至案卷页面
switch_window(browser)
#同意并提交审核
browser.switch_to.frame(browser.find_element_by_xpath("//div[@class='mini-tabs-body mini-tabs-hideOverflow']/iframe"))
browser.find_element_by_id("suggestArea").send_keys("同意")
browser.find_element_by_id("submit").click()
time.sleep(5)
browser.switch_to_default_content()
browser.switch_to.frame(browser.find_element_by_xpath("//div[@class='mini-panel-body']/iframe"))
browser.find_element_by_id("multSelect0").click()
browser.find_element_by_link_text("确定").click()
#切换用户
browser.switch_to.window(origin_window)
switch_user("cgr",browser)
###厅长签批###
browser.find_element_by_class_name("g-pt-gzzx").click()
browser.switch_to.frame(browser.find_element_by_xpath("//div[@id='tabPage_qpj']/iframe"))
browser.find_element_by_id("search-input").send_keys(yzsq_name)
browser.find_element_by_class_name("search-btn").click()
time.sleep(3)
browser.find_element_by_link_text(yzsq_name).click()
time.sleep(5)
switch_window(browser)
'''
for handle in browser.window_handles:
	browser.switch_to.window(handle)
'''
browser.switch_to.frame(browser.find_element_by_xpath("//div[@class='mini-tabs-body mini-tabs-hideOverflow']/iframe"))
browser.find_element_by_id("suggestArea").send_keys("同意")
browser.find_element_by_id("submit").click()
time.sleep(5)
browser.switch_to_default_content()
browser.switch_to.frame(browser.find_element_by_xpath("//div[@class='mini-panel-body']/iframe"))
#browser.find_element_by_id("multSelect0").click()
browser.find_element_by_link_text("确定").click()