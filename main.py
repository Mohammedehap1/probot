from attr import s
from selenium import webdriver
import undetected_chromedriver as uc
from fake_useragent import UserAgent as ua 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import os
import time
class data_function:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data_file = 'data.txt'
        self.data_list = []
        self.token = None
        self.token_list = []
        self.token_file = 'token.txt' 
        self.account_name = None
        self.last_claim = None
        self.current_credit = ''
        self.banned = False    
    def write_data(self,*args):
        file = open(self.data_file,'a')
        file.write(f'{self.token} / /{self.account_name} / /{self.last_claim} / /{self.current_credit} / /{self.banned}\n')
        file.close()
    def read_data(self,*args):
        data_file = open(self.data_file,'r')
        data_lines = data_file.readlines()
        for line in range(len(data_lines)):
            data = data_lines[line].split('\n')
            self.data_list.append(data[0])
    def make_data_readble(self,index = 0,*args):
        data = self.data_list[index].split(' / /')
        self.token, self.account_name, self.last_claim, self.current_credit, self.banned = data[0], data[1], data[2], data[3], data[4]
    def get_tokens(self,*args):
        token_file = open(self.token_file,'r')
        tokens = token_file.readlines()
        token_file.close()
        for count in range(len(tokens)):
            token = tokens[count].split('\n')
            self.token_list.append(token[0])

class Browser(data_function):
    driver_path = 'chromedriver.exe'
    user_data = r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data"
    home_page = None 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_agent = ua().random
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.options.add_argument(f'user-data-dir={self.user_data}')
        self.driver = uc.Chrome(executable_path=self.driver_path ,options=self.options)
        self.xpath_list = ['//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/section/div[2]/div[1]/div[2]/div[1]/div', # account name xpath
                           '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/nav/ul/div[2]/div[3]/div[1]/div[2]/div', # fisrt selver in discord
                           '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div[2]/main/form/div/div[1]/div/div[3]/div/div[2]/div',#text
                           '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/main/form/div/div[2]/div/div[2]/div/div/div',# sent text
                           '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div/section/div[2]/div[2]/button[3]/div',#settings button
                           '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div/div[1]/div/nav/div/div[35]/div',#logout button
                           '//*[@id="app-mount"]/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/button[1]/div',#logout conform Button
                           '//*[@id="app-mount"]/div[2]/div[1]/div[1]/div/div/div/section/div[2]/div[2]/div/div/div[3]/button[2]/div',#delete 
                           '//*[@id="manage-multi-account-remove-account"]/div',# conform delete


                           
                           ]
    def login_discord(self, *args):
      self.driver.execute_script('window.t = "' + self.token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
    def logout_discord(self,*args):
       self.load_element(self.xpath_list[4],click=True)
       self.load_element(self.xpath_list[5],click=True)
       self.load_element(self.xpath_list[6],click=True)
       time.sleep(5)
       if self.load_element('//*[@id=":rb:"]',callback=True) == False:
          self.load_element(self.xpath_list[7],click=True)
          self.load_element(self.xpath_list[8],click=True)
    def load_element(self, element, key = None, click = False, callback = False):
      found = False
      while not found:
        time.sleep(.5)
        try:
          self.driver.find_element(By.XPATH,element)
          if click == True :
            self.driver.find_element(By.XPATH,element).click()
          elif key != None :
            self.driver.find_element(By.XPATH,element).send_keys(key)
          elif callback == True:
             return True
          found = True
        except:
          found = False
          if callback == True:
             return False
    def change_window(self, *args):
      all_handles=self.driver.window_handles
      self.home_page = self.driver.current_window_handle
      for handle in all_handles:
        if handle != all_handles:
          self.driver.switch_to.window(handle)
    def check_cf(self, xpath = '//*[@id="challenge-running"]',*args): #return True if pass cf 
      found = 0
      while True:
        if self.load_element(xpath,callback=True) == True and found <= 3 :
            time.sleep(20)
            found +=1
        elif self.load_element(xpath,callback=True) == True and found >3 :
            return False
        else:
            return True
    def get_info(self,*args):
       #get username 
       self.driver.get('https://discord.com/channels/1139458107446149130/1139458107446149133')
       self.load_element(self.xpath_list[0])
       self.account_name = self.driver.find_element(By.XPATH,self.xpath_list[0]).text
       #get currunt credit
        #send /credits to probot
       self.load_element(self.xpath_list[2])
       send = self.driver.find_element(By.XPATH,self.xpath_list[2])
       send.send_keys('/credits')
       send.send_keys(Keys.ENTER)
       time.sleep(3)
       send.send_keys(Keys.ENTER)
       self.driver.find_element(By.XPATH,self.xpath_list[3]).send_keys(Keys.ENTER)
       time.sleep(5)
         #get response
       all_massege = self.driver.find_elements(By.CLASS_NAME,'inline')
       last_massege = all_massege[-1].text
       print(last_massege)
       credit = ''
       for litter in last_massege:
          try:
             type(int(litter))
             credit += ''.join((litter))
          except:
             pass
       self.current_credit = credit
    def test(self,*args):
       self.token = "but your token"
       self.driver.get('https://discord.com/login')
       time.sleep(10)
       self.login_discord()
       input()
       self.get_info()
       input()
       self.write_data()
       input()
       self.logout_discord()
       input()
