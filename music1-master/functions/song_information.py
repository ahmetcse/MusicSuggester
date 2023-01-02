from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import re


def get_statics(song_url):
    data = []
    url = f"https://soundcloud.com{song_url}"
    options = Options()
    options.add_argument("--headless")
    options.page_load_strategy = "none"
    options.add_experimental_option("prefs", {"profile.default_content_settings.cookies": 2})
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(url)
    try:
        elements = WebDriverWait(driver, 60).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "sc-ministats-item")))
        try:
            comment = WebDriverWait(driver, 5).until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "commentsList__actualTitle")))
        except:
            comment[0] = "No Comment"
        data.append(
            {"url": song_url, "view": elements[0].get_attribute("title"), "repost": elements[2].get_attribute("title"),
             "likes": elements[1].get_attribute("title"), "comment": comment[0].text})
        driver.quit()
    except:
        print("Şarkı bulunamadı")
        driver.quit()
    return data
