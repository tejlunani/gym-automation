import time

import credentials
from datetime import date, timedelta
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

TIME_OUT_SECONDS = 100
SLEEP = 3.0


def login():
    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/userlogin.aspx')
    assert ("Login to Premiere on Pine" in browser.title)

    username = browser.find_element_by_id("Username")
    username.clear()
    username.send_keys(credentials.POP_EMAIL)

    password = browser.find_element_by_id("Password")
    password.clear()
    password.send_keys(credentials.POP_PASSWORD)

    browser.find_element_by_id("SignIn").click()

    try:
        WebDriverWait(browser, TIME_OUT_SECONDS).until(expected_conditions.title_contains("Premiere on Pine | Apartments in Seattle, WA |"))
    except TimeoutException:
        print("Timed out while trying to log in..")
        raise


def generate_dates():
    today = date.today()
    dates_to_book_str = set()
    for i in range(0, 11):
        d = today + timedelta(days=i)
        dates_to_book_str.add(d.strftime("%m/%d/%y"))
    return dates_to_book_str


def remove_existing_reservations(dates_to_book):
    # navigate to 'view reservations' page
    # check each entry if Amenity="Fitness Center (PST)"
    # get start date for fitness center entry, check if it's in list, remove if it is
    # do this until the date is < current
    return


def create_gym_reservations(dates_to_book):
    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/conciergereservations.aspx#tab_MakeAReservation')

    for date in dates_to_book:
        select = Select(browser.find_element_by_name("ResourceId"))
        select.select_by_value("294")
        time.sleep(3.0)

        select = Select(browser.find_element_by_name("OverbookReason"))
        select.select_by_value("Fitness")

        select = browser.find_element_by_name("GuestCount")
        select.clear()
        select.send_keys("0")

        select = Select(browser.find_element_by_name("Duration"))
        select.select_by_value("60")
        time.sleep(3.0)

        select = browser.find_element_by_name("StartDate")
        select.clear()
        select.send_keys("value", date)
        time.sleep(3.0)

        select = Select(browser.find_element_by_id("AmPmStart"))
        select.select_by_value("AM")
        time.sleep(3.0)

        select = Select(browser.find_element_by_id("HoursStart"))
        select.select_by_value("7")
        time.sleep(3.0)

        select = Select(browser.find_element_by_id("MinutesStart"))
        select.select_by_value("0")
        time.sleep(3.0)

        browser.find_element_by_id("btnCreateReservation").click()


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.implicitly_wait(TIME_OUT_SECONDS)

    login()
    dates_to_book = generate_dates()
    remove_existing_reservations(dates_to_book)
    create_gym_reservations(dates_to_book)








