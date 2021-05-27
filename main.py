from splinter import Browser
import time

#urls
# https://10fastfingers.com/typing-test/german

#open browser window
browser = Browser('chrome')
browser.visit('https://10fastfingers.com/typing-test/german')

#allow cookies and get inputfield
allow = browser.find_by_id('CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
allow.click()
time.sleep(3)
inputfield = browser.find_by_id('inputfield')

print("start")

#loop through all words and type them
while True:
    word = browser.find_by_xpath('//div[@id="row1"]//span[@class="highlight"]').text
    arr = list(word)
    for j in arr:
        inputfield.type(j)
        time.sleep(0.03)
    inputfield.type(" ")
    time.sleep(0.2)






#ets-radio-control
