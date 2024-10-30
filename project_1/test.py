from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your ChromeDriver
driver_path = r'\Users\User\Desktop\Korola\Scrapping\chromedriver-win64\chromedriver.exe'

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

# Initialize WebDriver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Step 1: Open the website
url = 'https://www.prothomalo.com/'
driver.get(url)

# Step 2: Wait for the page to load
time.sleep(3)

# Step 3: Extract the content you want
titles = driver.find_elements(By.CLASS_NAME, 'tilte-no-link-parent')

print('Test')
# Print the extracted titles
for title in titles:
    if title.text:  # Check if the title is non-empty
        print(title.text, "\n")
        
        # Step 5: Open the new website (ChatGPT) in a new tab
        driver.execute_script("window.open('https://chat.openai.com', '_blank');")
        
        # Step 6: Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])
        
        # Step 7: Wait for the page to load and for the input field to appear
        try:
            # Wait until the element is visible
            time.sleep(10)
            input_field = driver.find_elements(By.CSS_SELECTOR, 'div.ProseMirror p')
            #input_field = WebDriverWait(driver, 10).until(
                #EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ProseMirror p'))
            #)
            # Send the extracted title to the input field
            #input_field.send_keys(title.text)
            print(input_field)
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        break

print('Test End')

# Close the browser
driver.quit()
