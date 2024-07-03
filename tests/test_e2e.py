from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
import pytest

class TestOne(BaseClass):

    def test_e2e(self):
        # self.driver.find_element(By.NAME, 'sd')
        print(self.driver.title)
