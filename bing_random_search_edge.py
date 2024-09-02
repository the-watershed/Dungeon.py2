
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

# List of random topics to search
topics = [
    "Python programming",
    "Machine learning",
    "Artificial intelligence",
    "Web development",
    "Data science",
    "Cybersecurity",
    "Cloud computing",
    "Internet of Things",
    "Blockchain technology",
    "Quantum computing",
    "Virtual reality",
    "Augmented reality",
    "Robotics",
    "5G technology",
    "Renewable energy"
]

# Set up the Edge WebDriver
edge_options = Options()
edge_options.use_chromium = True

# Path to msedgedriver.exe
edge_driver_path = r"C:\path\to\msedgedriver.exe"  # Update this path

# Initialize the Edge WebDriver
try:
    # For newer versions of Selenium
    from selenium.webdriver.edge.service import Service
    edge_service = Service(executable_path=edge_driver_path)
    driver = webdriver.Edge(service=edge_service, options=edge_options)
except TypeError:
    # For older versions of Selenium
    driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)

# Navigate to Bing.com
driver.get("https://www.bing.com")

# Main loop
try:
    while True:
        # Wait for the search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Clear the search box
        search_box.clear()

        # Choose a random topic
        topic = random.choice(topics)

        # Type the topic and submit
        search_box.send_keys(topic)
        search_box.send_keys(Keys.RETURN)

        # Wait for 5 seconds
        time.sleep(5)

        # Go back to Bing homepage
        driver.get("https://www.bing.com")

except KeyboardInterrupt:
    print("Script terminated by user.")
finally:
    # Close the browser
    driver.quit()
