from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def get_country_code(search_query):

    options = Options()
    options.headless = False  # Si lo deseas, puedes cambiar a True para ejecutar Firefox en modo headless

    driver = webdriver.Firefox(options=options)
    driver.get("https://www.google.com/")

    try:
        search_box = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "q"))
        )
        search_box.send_keys(search_query)
        search_box.submit()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3"))
        )
        first_result = driver.find_element(By.CSS_SELECTOR, "h3")
        first_result.click()

        url = driver.current_url
        print(url)
        country_code = url.split("-g")[-1].split("-")[0]
        return country_code
    except:
        print("Timeout")
    finally:
        driver.quit()
        print("Test completed")


search_query = "barcelona best traditional restaurants"  # Término de búsqueda en Google
country_code = get_country_code(search_query)
print(f"Country code for the search query '{search_query}': {country_code}")
