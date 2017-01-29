"""
High level tests ensuring our users get the functionality
they need.
We're going to have comment driven BDD-lite
Selenium used to drive a real browser.
Currently only [Firefox Extended Support Release](https://www.mozilla.org/en-US/firefox/organizations/)
because latest F-fox doesn't place nice
with Selenium out of the box
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

_TIME_WAIT_4_LOAD = 3  # seconds for browser to wait for pageload

class NewVisitorTest(unittest.TestCase):
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

    def test_can_add_new_organisation_and_retrieve_later(self):
        """test adding a contact and verifying persistence"""
        # Alex has heard about an new online address book
        # and checks out its homepage
        self.browser.get('http://localhost:8000')

        # Alex notices the page title mentions contacts
        self.assertIn('Contacts', self.browser.title)
        # and the header mentions organisations
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Organisations', header_text)

        # They are invited to enter a Organisation Contact straight away
        inputbox = self.browser.find_element_by_id('id_new_organisation')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter an organisation name'
        )

        # Alex types "Round Table." into a text box
        inputbox.send_keys('Round Table')
        inputbox.send_keys(Keys.ENTER)

        # When they hit enter, the page updates, and now the page lists
        # "Round Table" as an organisation
        self.check_for_item_text_in_list('Round Table')

        # There is another text box inviting them to add an second organisation.
        # Alex enters "Cheese Shop"
        inputbox = self.browser.find_element_by_id('id_new_organisation')
        inputbox.send_keys('Cheese Shop')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both Organisations persisted
        self.check_for_item_text_in_list('Round Table')
        self.check_for_item_text_in_list('Cheese Shop')

        # Alex wonders whether the site will remember their contact.
        # Then they see that the site has generated a unique URL for them
        #  -- there is some explanatory text to that effect.
        self.fail('finish the test!')

        # They visit that URL - The "Round Table" contact is still there.

        # Satisfied, Alex goes back to sleep

if __name__ == '__main__':
    unittest.main()
