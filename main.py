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
        self.data_file = 'test.txt'
        self.token_list = None
        self.token_file = None 
        self.account_name = None
        self.last_claim = None
        self.current_coin = None
        self.banned = False
    
    def write_data(self,*args):
        file = open(self.token_file,'a')
        file.write(f'{self.token} / /{self.account_name} / /{self.last_claim} / /{self.current_coin ,self.banned}')
        file.close()
    def read_data(self,*args):
        data_file = open(self.data_file,'r')
        data_lines = data_file.readlines()
        for line in range(len(data_lines)):
            data = data_lines[line].split('\n')
            self.data_list.append(data)
    def make_r_data(self,index = 0,*args):
        data = self.data_list[index].split('\n')
        
        
    
    
    
class Browser:
    tokens = ['lol']
    token_path = 'token.txt'
    driver_path = 'chromedriver.exe'
    user_data = r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data"
    sshome_page = None 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.tokens == []:
          self.get_tokens(self.token_path)
        self.user_agent = ua().random
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f'user-agent={self.user_agent}')
        self.options.add_argument(f'user-data-dir={self.user_data}')
        self.driver = uc.Chrome( options=self.options)
    def get_tokens(self,token_path,*args):
        token_file = open(token_path,'r')
        tokens = token_file.readlines()
        token_file.close()
        for count in range(len(tokens)):
            token = tokens[count].split('\n')
            self.tokens.append(token[0])
    def login_discord(self, *args):
      self.driver.execute_script('window.t = "' + self.token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
    def load_element(self, element, key = '', click = False):
      found = False
      while not found:
        time.sleep(.5)
        try:
          self.driver.find_element(By.XPATH,element)
          if click == True :
            self.driver.find_element(By.XPATH,element).click()
          elif key != '' :
            self.driver.find_element(By.XPATH,element).send_keys(key)
          found = True
        except:
          found = False
    def change_window(self, *args):
      all_handles=self.driver.window_handles
      self.home_page = self.driver.current_window_handle
      for handle in all_handles:
        if handle != all_handles:
          self.driver.switch_to.window(handle)
    def check_cf(self,*args):
      pass
    def start(self, *args):
      print(self.driver_path)
      self.driver.get("http://www.example.com/")
      input()

Browser().start()