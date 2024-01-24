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

class TestOjee():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_ojee(self):
    self.driver.get("https://ojee.nic.in/")
    self.driver.set_window_size(1280, 672)
    self.driver.find_element(By.LINK_TEXT, "Schedule").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .fa").click()
    self.vars["win6323"] = self.wait_for_window(2000)
    self.vars["root"] = self.driver.current_window_handle
    self.driver.switch_to.window(self.vars["win6323"])
    self.driver.switch_to.window(self.vars["root"])
  
