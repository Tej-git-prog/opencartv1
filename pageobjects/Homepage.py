from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():
    link_account_xpath="//span[normalize-space()='My Account']"
    link_register_xpath="//a[@class='dropdown-item'][normalize-space()='Register']"
    link_login_xpath="//a[@class='dropdown-item'][normalize-space()='Register']"

def __init__(self,driver):
    self.driver = driver

def clickAccount(self):
    self.driver.find_element(By.XPATH,self.link_account_xpath).click()
def registerButton(self):
    self.driver.find_element(By.XPATH,self.link_register_xpath).click()
def loginButton(self):
    self.driver.find_element(By.XPATH,self.link_register_xpath).click()
