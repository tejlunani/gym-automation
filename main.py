import credentials
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

TIME_OUT_SECONDS = 100


def login():
    username = browser.find_element_by_id("Username")
    username.clear()
    username.send_keys(credentials.POP_EMAIL)

    password = browser.find_element_by_id("Password")
    password.clear()
    password.send_keys(credentials.POP_PASSWORD)

    browser.find_element_by_id("SignIn").click()

#def create_reservation(activity, cur_date):


if __name__ == '__main__':
    browser = webdriver.Chrome()

    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/userlogin.aspx')
    assert ("Login to Premiere on Pine" in browser.title)
    login()

    try:
        WebDriverWait(browser, TIME_OUT_SECONDS).until(expected_conditions.title_contains("Premiere on Pine | Apartments in Seattle, WA |"))
    except TimeoutException:
        print("Timed out while trying to log in..")
        raise

    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/conciergereservations.aspx#tab_MakeAReservation')

    #calc list of possible booking dates, from today to 10 days from now, put into data struct

    #navigate to 'view reservations' page

    #get start date for fitness center entry, check if it's in list, remove if it is

    #do this until the date is no longer in the list

    # current_date = date.today()
    # create_reservation('Fitness Center', current_date.strftime("%d/%m/%Y"))






