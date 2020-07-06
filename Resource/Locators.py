
#Locator strategy for automate Testing
#I would prefer use only ID locators, cause ID is unique in a web page. But in my case I was able to use ID only for my login(username and pass) locators.
#As a second option I considered Name locators, but in my case I had a lot of names/words repetition(read,book and etc), and for not to get confused I didn't use name locators.
#Mostly I used CSS_Selectors, cause it's cross-browser performant and simple to maintain,
#Also I used X_Path (Absolute Path), for solving Dynamic element problem (when I add book to shelf it's locator change)

from selenium.webdriver.common.by import By


class LoginPageLocators:
    _username_input ={"by": By.ID, "value": "userSignInFormEmail"}
    _password_input ={"by": By.ID, "value": "user_password"}
    _signin_button ={"by": By.CSS_SELECTOR, "value": "input.gr-button.gr-button--dark"}
    _login_failure ={"by": By.CSS_SELECTOR, "value":"gr-flashMessage gr-flashMessage--error"}

class HomePageLocators:
    _login_success ={"by": By.CSS_SELECTOR, "value": "div.siteHeader__topLine.gr-box.gr-box--withShadow"}
    _search_box = {"by": By.CSS_SELECTOR, "value": "input.searchBox__input.searchBox__input--navbar"}
    _search_button = {"by": By.XPATH, "value": "div[2]/form/button"}
    _menu = {"by":By.CLASS_NAME, "value": "siteHeader__topLevelItem"}
    _mybooks = {"by": By.LINK_TEXT, "value": "My Books"}

class Search_LOTR:
    _lotr1 = {"by": By.LINK_TEXT, "value": "The Fellowship of the Ring (The Lord of the Rings, #1)"}

class Lotr_book_first:
    want_to_read = {"by": By.XPATH, "value": "/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/form/button"}

class myShelves:
    _Lotr_first= {"by": By.XPATH, "value": "/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[6]/table/tbody/tr/td[4]/div/a"}
    _delete_book = {"by": By.XPATH,"value": "/html/body/div[2]/div[3]/div[1]/div[1]/div[3]/div[2]/div[6]/table/tbody/tr/td[30]/div/div/a"}
    _empty_shelf = {"by": By.CSS_SELECTOR, "value": "div.greyText.nocontent.stacked"}