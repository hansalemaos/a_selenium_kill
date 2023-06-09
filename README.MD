# A decorator to kill Chrome if Selenium/ChromeDriver got stuck


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-kill

import undetected_chromedriver as uc
from a_selenium_kill import add_kill_selenium


@add_kill_selenium
def get_driver():
    return uc.Chrome()
    #return driver


if __name__ == "__main__":
    driver = get_driver()
    driver2 = get_driver()
    driver3 = get_driver()

	
	#Kill Chrome:
	# driver.die_die_die_selenium()
```


