# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFlipkart():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_flipkart(self):
    self.driver.get("https://www.flipkart.com/")
    self.driver.set_window_size(1280, 672)
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1ch8e_:nth-child(2) .\\_3ETuFY").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(4) .\\_1mIbUg:nth-child(2) .kJjFO0").click()
    self.driver.execute_script("window.scrollTo(0,0)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_167Mu3:nth-child(6) .\\_4921Z:nth-child(1) .\\_24_Dny").click()
    self.driver.execute_script("window.scrollTo(0,92)")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_2WDRax").click()
    self.driver.find_element(By.LINK_TEXT, "Bedsheets").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) > .\\_13oc-S > div:nth-child(3) .\\_396cs4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) > .\\_13oc-S > div:nth-child(3) .\\_396cs4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".\\_1AtVbE:nth-child(2) > .\\_13oc-S > div:nth-child(3) .\\_396cs4")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
  
