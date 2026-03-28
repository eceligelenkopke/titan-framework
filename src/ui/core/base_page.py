from src.selenium.core.webdriver_provider import WebDriverProvider
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self):
        self.webdriver_provider = WebDriverProvider()
        self.driver = self.webdriver_provider.get_driver()
        self.timeout = 15

    def wait_and_click(self,locator):
        WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_until_elements_visible(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
    def wait_until_element_visible(self,locator):
        WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_and_send_input(self,locator,input_text):
        WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(input_text)

    def wait_until_element_clickable(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_and_clear_input_line(self,locator):
        click_on_element = WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        click_on_element.click()
        click_on_element.send_keys(Keys.CONTROL + 'a')
        return click_on_element.send_keys(Keys.BACKSPACE)

    def wait_until_element_invisible(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_and_scroll_until_element_visible(self, locator):
        target_element = WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )
        try:
            ActionChains(self.driver).scroll_to_element(target_element).perform()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", target_element)

        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return target_element


    def get_text_of_element(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        ).text

    def check_if_element_clickable(self, locator):
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
    def get_attribute_of_element(self, locator, attribute_name):
        element = WebDriverWait(self.driver,self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute(attribute_name)

    def wait_until_alert_is_visible(self):
        WebDriverWait(self.driver,self.timeout).until(
            EC.alert_is_present()
        )

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver,self.timeout).until(
            EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break


