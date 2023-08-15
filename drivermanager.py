from imports import *


def initialize_chrome_driver(debbug=False):
    options = uc.ChromeOptions()
    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )
    if not debbug:
        options.headless = True
        options.add_argument("--headless")
    chrome = uc.Chrome(options=options)
    return chrome
