from _ast import Assert

import HtmlTestRunner
from selenium import webdriver
import unittest
import time
class GooleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="D:\python\Driver\CormieDriver\Crome83\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    def test_search_automationStep(self):
        self.driver.get("https:google.com")
        self.driver.find_element_by_name("q").send_keys("ducks ")

        time.sleep(3)
        self.driver.find_element_by_class_name("gNO89b").click()

       # element= self.driver.title

       # assert element.text == 'ducks - Google Search'

        #Assert.assertEquals(('ducks - Google Search'),(self.driver.title))
        time.sleep(3)
        print("Display on page: "+self.driver.title)
        get_title = self.driver.title

        # Printing the title of this URL
        self.assertIn("ducks - Google Search", self.driver.title)
        print(get_title, "  ", len(get_title))

        print(self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test complet")

        if __name__ == '__main__':
            unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/Project/Python/demoProject/reports'))

        print("Run repoet")