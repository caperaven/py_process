from selenium.webdriver.remote.webelement import WebElement


class MockWebElement(WebElement):
    def __init__(self, parent, id_, tag_name='div'):
        super().__init__(parent, id_)
        self._tag_name = tag_name
        self._attributes = {}
        self._styles = {}
        self._properties = {}
        self._selected = False
        self._children = []

    @property
    def tag_name(self):
        return self._tag_name

    def is_selected(self):
        return self._selected

    def set_attribute(self, name, value):
        self._attributes[name] = value

    def get_attribute(self, name):
        return self._attributes.get(name, None)

    def set_style(self, name, value):
        self._styles[name] = value

    def value_of_css_property(self, name):
        return self._styles.get(name, None)

    def set_property(self, name, value):
        self._properties[name] = value

    def get_property(self, name):
        return self._properties.get(name, None)

    def set_selected(self, value):
        self._selected = value

    def add_children(self, *children):
        self._children.extend(children)

    def find_elements(self, by_type, query):
        return self._children

    def find_element(self, by_type, query):
        if len(self._children) == 0:
            return None

        return self._children[0]

