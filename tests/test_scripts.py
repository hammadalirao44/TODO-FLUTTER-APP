from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

def setup_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "Android Emulator"
    options.app = "app-release.apk"
    options.automation_name = "UiAutomator2"

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver


def test_app_launch():
    driver = setup_driver()
    time.sleep(5)

    assert driver.current_package is not None

    driver.quit()


def test_home_screen_loaded():
    driver = setup_driver()
    time.sleep(5)

    # Example validation (replace with real locator)
    assert driver.page_source is not None

    driver.quit()


def test_app_background_and_resume():
    driver = setup_driver()
    time.sleep(3)

    driver.background_app(3)
    time.sleep(2)

    assert driver.current_activity is not None

    driver.quit()
