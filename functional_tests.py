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

_TIME_WAIT_4_LOAD = 3  # seconds for browser to wait for pageload

class NewVisitorTest(unittest.TestCase):
    """test we treat 1st visit properly"""

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(_TIME_WAIT_4_LOAD)


    def tearDown(self):
        self.browser.quit()

    def test_can_add_new_organization_and_retrieve_later(self):
        """test adding a contact and verifying persistence"""
        # Alex has heard about an new online address book
        # and checks out its homepage
        self.browser.get('http://localhost:8000')

        # Alex notices the page title mentions contacts
        self.assertIn('Contacts', self.browser.title)

        # do more work on test
        self.fail()
        # They are invited to enter a to-do item straight away

        # They type "Round Table." into a text box

        # When they hit enter, the page updates, and now the page lists
        # "Acme Inc." as an item

        # There is another text box inviting her to add an email.
        # Alex enters "info@rtable.com"

        # The page updates again, and now shows both items persisted

        # Alex wonders whether the site will remember her contact.
        # Then they see that the site has generated a unique URL for them
        #  -- there is some explanatory text to that effect.

        # They visit that URL - The "Round Table" contact is still there.

        # Satisfied, Alex goes back to sleep

if __name__ == '__main__':
    unittest.main()