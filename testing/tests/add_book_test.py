from selenium import webdriver
from Pages.Fellowship_page import FellowshipPage
from Pages.My_Books_page import MybookPage
from Pages.Search_result_page import SearchPage
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
import pytest
#Goodread is a website for readers and book recommendation, where you can see what books your friends are reading.
#and track the books you're reading, have read, and want to read.
#Test scenario >>> test searching and adding a book to shelf functionalaties
#Verify that the user can search the book in ‘Search books’ search functionality.
#Verify that users can navigate and choose the book from the searching list
#Verify that the user can add the book to user's "Want to read" shelf.
#I Navigate and go to user's shelf and print "want to read" booklist (I did it only for using multiple windows interactions here)
#Go back to user's shelf >> Want to read section
#Delet the book from user's <want to read> list


class Test_Search():
    def test_search_book(self, browser):
        login_pg = LoginPage(browser)
        home_pg = HomePage(browser)
        browser.get("https://www.goodreads.com/")
        login_pg.with_("irairina27@gmail.com", "SuperPassword")
        assert home_pg.success_message_present()
        home_pg.search_input("The Lord of the Rings")
        list_pg = SearchPage(browser)
        list_pg.choose_book()
        bookone_pg = FellowshipPage(browser)
        bookone_pg.add_to_read()
        bookone_pg.mybook()
        mybook_pg = MybookPage(browser)
        browser.refresh()
        assert mybook_pg.book_on_shelf()
        window_before = browser.window_handles[0]
        browser.find_element_by_link_text("Print").click()
        window_after = browser.window_handles[1]
        browser.switch_to.window(window_after)
        browser.find_element_by_link_text("My Books").click()
        browser.switch_to.window(window_before)
        mybook_pg.delete()
        browser.switch_to.alert.accept()
        assert mybook_pg.verify_empty_shelf()










