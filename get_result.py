from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
import time
import sys
import builtins
import os


CHROME_PATH = 'C:/Users/liral/Desktop/project/chromedriver'
URL = 'https://www.gsmarena.com/'
OS_XPATH = '//*[@id="specs-list"]/table[5]/tbody/tr[1]/td[2]'
GPU_XPATH = '//*[@id="specs-list"]/table[5]/tbody/tr[4]/td[2]'
CPU_XPATH = '//*[@id="specs-list"]/table[5]/tbody/tr[3]/td[2]'
SELECT = '//*[@id="review-body"]/div/ul/li/a/img'
SEARCH_BOX = '//*[@id="topsearch-text"]'
SELECT_PHONE = '//*[@id="topsearch"]/div[1]/div[2]/ul/li[1]/a'


def get_results(search_term):
    browser = webdriver.Chrome(executable_path=CHROME_PATH)
    browser.get(URL)
    search_bar = browser.find_element_by_xpath(SEARCH_BOX)
    search_bar.send_keys(search_term)
    time.sleep(5)
    search_bar.find_element_by_xpath(SEARCH_BOX).click()
    data = []
    try:
        time.sleep(2)
        search_bar.find_element_by_xpath(SELECT_PHONE).click()
        time.sleep(5)
        # OS
        os_text = browser.find_element_by_xpath(OS_XPATH).text
        '''
        os_text.split(',')
        old_version = os_text[0]
        new_version = os_text[1]
        data.append(old_version)
        data.append(new_version)
        '''
        data.append(os_text)
        # GPU
        gpu_text = browser.find_element_by_xpath(GPU_XPATH).text
        data.append(gpu_text)
        # CPU
        cpu_text = browser.find_element_by_xpath(CPU_XPATH).text
        data.append(cpu_text)
    except:
        print("Error : Device Not Found :( ")
    finally:
        print_data(data)
        browser.close()


def print_data(data):
    print("The OS versions :", data[0])
    print("The GPU :", data[1])
    print("The CPU : ", data[2])


if __name__ == "__main__":
    get_results("iphone 12 pro max")
