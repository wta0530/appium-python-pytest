from appium.webdriver.common.appiumby import AppiumBy


class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value="new UiScrollable(new UiSelector().scrollable(true).instance("
                                  "0)).scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def scrollToText(xpath, text, driver):
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value="new UiScrollable(new UiSelector().resourceId(\"" + xpath + "\")).scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def scrollToInstance(xpath, driver):
        driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                            value="new UiScrollable(new UiSelector().className(\"" + xpath + "\").instance(21)").click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)