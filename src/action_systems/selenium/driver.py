from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class Driver:
    @staticmethod
    async def init(browser, options=None):
        browser_fn = getattr(Driver, browser)

        if browser_fn is None:
            raise Exception(f"browser {browser} is not supported")

        return await browser_fn(options)

    @staticmethod
    async def close(driver):
        driver.close()

    @staticmethod
    async def chrome(options):
        opt = webdriver.ChromeOptions()
        opt.add_argument("start-maximized")
        opt.add_argument("ignore-certificate-errors")

        if options is not None and "arguments" in options:
            for arg in options["arguments"]:
                opt.add_argument(arg)

        driver_path = options["driver_path"]
        chrome_service = ChromeService(driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=opt)
        driver.get("about:blank")

        return driver

    @staticmethod
    async def firefox(options):
        opts = webdriver.FirefoxOptions()
        opts.add_argument("start-maximized")
        opts.add_argument("ignore-certificate-errors")

        driver = webdriver.Firefox()
        pass

    @staticmethod
    async def edge(options):
        pass

    @staticmethod
    async def safari(options):
        pass
