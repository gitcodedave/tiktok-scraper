from selenium import webdriver

PATH = "/Users/Dave/chromedriver"
service = webdriver.ChromeService(executable_path=PATH)
driver = webdriver.Chrome(service=service)
