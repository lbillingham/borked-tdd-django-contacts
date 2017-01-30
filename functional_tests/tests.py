"""
High level tests ensuring our users get the functionality
they need.
We're going to have comment driven BDD-lite
Selenium used to drive a real browser.
Currently only
[Firefox Extended Support Release](https://www.mozilla.org/en-US/firefox/organizations/)
because latest F-fox doesn't place nice
with Selenium out of the box
"""
import unittest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

_TIME_WAIT_4_LOAD = 3  # seconds for browser to wait for pageload

class NewVisitorTest(LiveServerTestCase):
    """test we treat 1st visit properly"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(_TIME_WAIT_4_LOAD)

    def tearDown(self):
        self.browser.quit()

    def check_for_item_text_in_list(self, item_text):
        """do any of our list elements contain `item_text?"""
        org_list = self.browser.find_element_by_id('id_organisations_list')
        orgs = org_list.find_elements_by_tag_name('li')
        self.assertIn(item_text, [org.text for org in orgs])

    def test_can_add_new_organisations_and_see_on_home_page(self):
        """test adding 2 contacts shows up on home page"""
        # Alex has heard about an new online address book
        # and checks out its homepage
        self.browser.get(self.live_server_url)

        # Alex notices the page title mentions contacts
        self.assertIn('Contacts', self.browser.title)
        # and the header mentions organisations
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Organisations', header_text)

        # Alex sees an empty list of organisations
        org_list = self.browser.find_element_by_id('id_organisations_list')
        orgs = org_list.find_elements_by_tag_name('li')
        self.assertEqual([], [org.text for org in orgs])

        # Alex sees a link to add a new organisation and clicks it
        link = self.browser.find_element_by_id('id_add_organisation')
        link.click()

        # Alex is redirected to the add orginisation page
        # They are invited to enter a Organisation Contact straight away
        # ... adding the organisation name
        namebox = self.browser.find_element_by_id('id_name')
        emailbox = self.browser.find_element_by_id('id_email')

        # Alex types "Round Table." into the name box,
        namebox.send_keys('Round Table')
        namebox.send_keys(Keys.ENTER)
        # ... and rtable@example.com into the email box
        emailbox.send_keys('rtable@example.com')
        emailbox.send_keys(Keys.ENTER)

        # When they hit enter, Alex is returned to the home page
        self.assertRegex(self.browser.current_url, '/$')
        # which now lists "Round Table" as an organisation
        self.check_for_item_text_in_list('Round Table')

        # Alex follows the link to add another organisation.
        self.browser.find_element_by_id('id_add_organisation').click()
        # Alex enters "Cheese Shop"
        namebox = self.browser.find_element_by_id('id_name')
        namebox.send_keys('Cheese Shop')
        namebox.send_keys(Keys.ENTER)
        emailbox = self.browser.find_element_by_id('id_email')
        emailbox.send_keys('cheese_shop@example.com')
        emailbox.send_keys(Keys.ENTER)

        # Alex is returned to the home page agiain
        # it now shows both Organisations persisted
        self.check_for_item_text_in_list('Round Table [edit]')
        self.check_for_item_text_in_list('Cheese Shop [edit]')

        # Alex wonders whether the site will remember their contacts.
        # Then they see that the site has generated a unique URL for them
        self.fail('finish the test!')

    def test_organisations_added_can_be_edited(self):
        """test can add an org then edit it"""
        # Alex has heard about an new online address book
        # and checks out its homepage
        self.browser.get(self.live_server_url)
        # Alex adds a new organisation by following a link
        link = self.browser.find_element_by_id('id_add_organisation')
        link.click()
        namebox = self.browser.find_element_by_id('id_name')
        emailbox = self.browser.find_element_by_id('id_email')
        namebox.send_keys('Can I be edited')
        namebox.send_keys(Keys.ENTER)
        emailbox.send_keys('edit.me@example.com')
        emailbox.send_keys(Keys.ENTER)

        # When they hit enter, Alex is returned to the home page
        # which now lists the new org
        self.check_for_item_text_in_list('Can I be edited [edit]')
        # Alex notices an edit link next to the new org
        link = self.browser.find_element_by_id('id_edit_organisation')
        link.click()
        # they are redirected to a url
        org_url = self.browser.current_url
        self.assertRegex(org_url, '/edit-organisation/.+')
        # Alex sees their organisation named
        namebox = self.browser.find_element_by_id('id_name')
        self.assertEqual(namebox.get_attribute('value'), 'Can I be edited')
        # alex edits the organisations name
        namebox.clear()
        namebox.send_keys('Edited I have been')
        namebox.send_keys(Keys.ENTER)
        # Alex is sent back to the homepage and sees
        # the edits have worked
        self.check_for_item_text_in_list('Edited I have been [edit]')

    def test_organisation_persistance(self):
        """do orgs hang around after browser quits?"""
        # Alex adds a new organisation
        # clciks the link to its edit page
        self.browser.get(self.live_server_url)
        link = self.browser.find_element_by_id('id_add_organisation')
        link.click()
        namebox = self.browser.find_element_by_id('id_name')
        emailbox = self.browser.find_element_by_id('id_email')
        namebox.send_keys('Round Table')
        namebox.send_keys(Keys.ENTER)
        emailbox.send_keys('rtable@example.com')
        emailbox.send_keys(Keys.ENTER)
        edit_link = self.browser.find_element_by_id('id_edit_organisation')
        edit_link.click()
        # they are redirected to a url
        org_url = self.browser.current_url
        # Alex quits the browser
        # later they return to the home page
        # and find their added org still there
        ## We use a new browser session to make sure that no information
        ## of Alex's is coming through from cookies etc
        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        self.check_for_item_text_in_list('Round Table [edit]')
        # alex returns to the orgs edit page and sees it
        # is at the same url
        edit_link = self.browser.find_element_by_id('id_edit_organisation')
        edit_link.click()
        self.assertEqual(org_url, self.browser.current_url)