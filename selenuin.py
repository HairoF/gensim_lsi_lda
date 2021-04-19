from selenium import webdriver
from model import Question
import re

from selenium.common.exceptions import TimeoutException
delay = 2
url = 'https://www.udemy.com/courses/development/'
driver_location = '/home/fidan/Documents/pyProjects/chromedriver'
driver = webdriver.Chrome(driver_location)
driver.implicitly_wait(2)


class UdemyParser(object):

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.go_to_tests_page()
        self.parse_question_page()

    def go_to_tests_page(self):
        self.driver.get(url)
        slide_elems = self.driver.find_elements_by_class_name('browse-course-card--link--3KIkQ')

        for elem in slide_elems:
            links = elem.get_attribute('href')
            print(links)
            self.driver.get(links)
            break

    def parse_question_page(self):
        question = Question()
        self.fill_question_title(question)
        print(question)
        self.fill_question_price(question)
        print(question)


    def fill_question_title(self, question):
        try:
            question_title_elm = self.driver.find_element_by_tag_name('h1')
            question.title = question_title_elm.text
        except TimeoutException:
            print("Time is out")

    def fill_question_price(self, question):
        question_price_elm = self.driver.find_element_by_css_selector('.price-text--original-price--2e-F5')
        dd = question_price_elm.text.replace(' ', '')
        question.price = re.findall('\d+', dd)[0]









def main():
    parser = UdemyParser(driver)
    parser.parse()

if __name__ == "__main__":
    main()