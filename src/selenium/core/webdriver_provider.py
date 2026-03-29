import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions


class WebDriverProvider:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            supported_browsers = ['chrome', 'ch', 'headlesschrome', 'headlessch', 'firefox', 'ff', 'headlessff',
                                  'headlessfirefox']
            browser = os.environ.get('BROWSER')

            # Get the test environment
            execution_env = os.environ.get('EXECUTION_ENV', 'local')

            grid_url = "http://selenium-hub:4444/wd/hub"

            if not browser:
                raise Exception("The Environment Variable BROWSER must be set.")

            browser = browser.lower()

            if browser not in supported_browsers:
                raise Exception(f"Browser '{browser}' is not supported. Supported: {supported_browsers}")

            options = None

            # Common Options
            if browser in ('chrome', 'ch'):
                options = ChOptions()
                options.add_argument("--window-size=1920,1080")
            elif browser in ('headlesschrome', 'headlessch'):
                options = ChOptions()
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")
            elif browser in ('firefox', 'ff'):
                options = FFOptions()
                options.add_argument("--window-size=1920,1080")
            elif browser in ('headlessfirefox', 'headlessff'):
                options = FFOptions()
                options.add_argument("--headless")
                options.add_argument("--window-size=1920,1080")

            # Open Driver depending on test environment
            if execution_env == 'docker':
                # If tests run on Docker
                cls._driver = webdriver.Remote(command_executor=grid_url, options=options)
                
                # If tests run on GIT
            elif os.environ.get("BASE_URL") == "http://wordpress/":
                cls._driver = webdriver.Remote(command_executor="http://selenium-hub:4444/wd/hub", options=options)
            
            else:
                # If tests run on local machine
                if 'chrome' in browser or 'ch' in browser:
                    cls._driver = webdriver.Chrome(options=options)
                elif 'firefox' in browser or 'ff' in browser:
                    cls._driver = webdriver.Firefox(options=options)


            if 'headless' not in browser:
                cls._driver.maximize_window()
            else:
                cls._driver.set_window_size(1920, 1080)

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None