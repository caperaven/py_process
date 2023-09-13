from process_api.modules.selenium.modules.selenium_perform import PerformModule
from process_api.modules.selenium.modules.selenium_wait import WaitModule
from process_api.modules.selenium.modules.selenium_assert import AssertModule


def register(api):
    PerformModule.register(api)
    WaitModule.register(api)
    AssertModule.register(api)

