from multiprocessing import Process
import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get("http://msn.com")
def func1():
  print ('launching: MSN')
  driver.execute_script("window.open('http://www.msn.com');")

def func2():
  print ('launching: CNN')
  driver.execute_script("window.open('http://www.cnn.com');")

if __name__ == '__main__':
  p1 = Process(target=func1)
  p1.start()
  p2 = Process(target=func2)
  p2.start()
  p1.join()
  p2.join()

def runInParallel(*fns):
  proc = []
  for fn in fns:
    p = Process(target=fn)
    p.start()
    proc.append(p)
  for p in proc:
    p.join()

runInParallel(func1, func2)