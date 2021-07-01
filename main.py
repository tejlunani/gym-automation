import time

import credentials
from datetime import date, timedelta
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

TIME_OUT_SECONDS = 100


def login():
    username = browser.find_element_by_id("Username")
    username.clear()
    username.send_keys(credentials.POP_EMAIL)

    password = browser.find_element_by_id("Password")
    password.clear()
    password.send_keys(credentials.POP_PASSWORD)

    browser.find_element_by_id("SignIn").click()

def create_gym_res(dates_to_book):
    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/conciergereservations.aspx#tab_MakeAReservation')

    for date in dates_to_book:
        #Select Amenity
        select = Select(browser.find_element_by_id("ResourceId"))
        select.select_by_value("Fitness Center")
        #Select reason for booking

        #input # of guests


if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.implicitly_wait(TIME_OUT_SECONDS)

    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/userlogin.aspx')
    assert ("Login to Premiere on Pine" in browser.title)
    login()

    try:
        WebDriverWait(browser, TIME_OUT_SECONDS).until(expected_conditions.title_contains("Premiere on Pine | Apartments in Seattle, WA |"))
    except TimeoutException:
        print("Timed out while trying to log in..")
        raise

    browser.get('https://premiereonpine.securecafe.com/residentservices/premiere-on-pine/conciergereservations.aspx#tab_MakeAReservation')

    select = Select(browser.find_element_by_name("ResourceId"))
    select.select_by_value("294")
    time.sleep(5.0)

    select = Select(browser.find_element_by_name("OverbookReason"))
    select.select_by_value("Fitness")

    select = browser.find_element_by_name("GuestCount")
    select.clear()
    select.send_keys("0")

    select = Select(browser.find_element_by_name("Duration"))
    select.select_by_value("60")
    time.sleep(5.0)

    select = browser.find_element_by_name("StartDate")
    select.clear()
    select.send_keys("value", "7/3/2021")
    time.sleep(5.0)

    select = Select(browser.find_element_by_id("AmPmStart"))
    select.select_by_value("AM")
    time.sleep(3.0)

    select = Select(browser.find_element_by_id("HoursStart"))
    select.select_by_value("7")
    time.sleep(3.0)

    select = Select(browser.find_element_by_id("MinutesStart"))
    select.select_by_value("0")




    # calc list of possible booking dates, from today to 10 days from now, put into data struct
    # we do this so that we can avoid booking the fitness center on days where it is already booked
    today = date.today()
    start_date_str = today.strftime("%m/%d/%y")

    dates_to_book_str = set()
    for i in range(0, 11):
        d = today + timedelta(days=i)
        dates_to_book_str.add(d.strftime("%m/%d/%y"))

    print(start_date_str)
    print(dates_to_book_str)

    #navigate to 'view reservations' page

    #check each entry if Amenity="Fitness Center (PST)"

    #get start date for fitness center entry, check if it's in list, remove if it is

    #do this until the date is < current

    # current_date = date.today()
    # create_reservation('Fitness Center', current_date.strftime("%d/%m/%Y"))






