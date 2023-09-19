from selenium.webdriver.remote.webelement import WebElement


class MockWebElement(WebElement):
    def __init__(self, parent, id_, tag_name='div'):
        super().__init__(parent, id_)
        self._tag_name = tag_name
        self.attributes = {}
        self.styles = {}
        self.properties = {}

    @property
    def tag_name(self):
        return self._tag_name

    def set_attribute(self, name, value):
        self.attributes[name] = value

    def get_attribute(self, name):
        return self.attributes.get(name, None)

    def set_style(self, name, value):
        self.styles[name] = value

    def value_of_css_property(self, name):
        return self.styles.get(name, None)

    def set_property(self, name, value):
        self.properties[name] = value

    def get_property(self, name):
        return self.properties.get(name, None)


