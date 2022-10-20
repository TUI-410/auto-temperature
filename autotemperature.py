from selenium import webdriver
from selenium.webdriver import ChromeOptions, ActionChains  # 这个包用来规避被检测的风险
import time
from chaojiying import Chaojiying_Client
from selenium.webdriver.common.by import By



timetamp = time.mktime(time.localtime())
timetamp = int(timetamp)
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


option = webdriver.ChromeOptions()
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver_path = r'./chromedriver.exe'  # 定义好路径
driver = webdriver.Chrome(executable_path=driver_path, options=option)  # 初始化路径+规避检测
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})
try:
    chaojiying = Chaojiying_Client('256904767 ', 'zjl123321...', '1005')  # 超级鹰账号
    driver.get('http://xscfw.hebust.edu.cn/survey/login')

    user_name = driver.find_element(By.XPATH,'//*[@id="user"]').send_keys('2102100132')  # 输入账号
    time.sleep(4)
    pass_word = driver.find_element(By.XPATH,'//*[@id="pwd"]').send_keys('Zjl1584572446...')  # 输入密码
    time.sleep(5)

    log_in = driver.find_element(By.XPATH,'//*[@id="login"]').click()  # 点击登录按钮
    time.sleep(5)
    img = driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/img').screenshot_as_png  # 截图
    dic = chaojiying.PostPic(img, 1902)

    verification_code = dic['pic_str']
    # print(verification_code)
    time.sleep(5)
    auth_code = driver.find_element(By.XPATH,'//*[@id="vcode"]').send_keys(verification_code)  # 输入验证码
    time.sleep(5)
    log_qd = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/a[2]').click()  # 点击确定按钮

    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/a[1]').click()

    # 鼠标点击事件
    time.sleep(1)
    ActionChains(driver).click(driver.find_element(By.CSS_SELECTOR, 'li[class="mdui-list-item mdui-ripple"]')).perform()
    print("登录成功")

except Exception:
    print("验证码错误\n")
    time.sleep(1)

try:
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='c1']").clear()
    driver.find_element(By.CSS_SELECTOR, "input[name='c4']").clear()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[name='c1']").send_keys("36.5")
    driver.find_element(By.CSS_SELECTOR, "input[name='c4']").send_keys("36.5")
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="main"]/div[7]/label[2]').click()
    time.sleep(1)
    driver.find_element(By.ID, "save").click()
    time.sleep(1)
    b = "打卡成功"
    driver.quit()
except Exception:
    b="打卡失败\n"
    time.sleep(1)

# file = open("mydata.html", 'w+', encoding='UTF-8')
# file.write(a+'*****'+b)
# file.close()

