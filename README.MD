# A decorator to kill Chrome if Selenium/ChromeDriver got stuck


```python
# Tested with:
# https://github.com/ultrafunkamsterdam/undetected-chromedriver
# Python 3.9.13
# Windows 10


$pip install a-selenium-kill

from a_selenium_kill import add_kill_selenium
from auto_download_undetected_chromedriver import download_undetected_chromedriver
import undetected_chromedriver as uc

# You have to create the instance in a function, and use the decorator @add_kill_selenium
@add_kill_selenium
def get_driver():
    folderchromedriver = "f:\\seleniumdriver2"
    path = download_undetected_chromedriver(folder_path_for_exe=folderchromedriver, undetected=True)
    driver = uc.Chrome(driver_executable_path=path)
    return driver

if __name__ == "__main__":
    driver = get_driver()
	
	#Kill Chrome:
	
	driver.die_die_die_selenium()
```


