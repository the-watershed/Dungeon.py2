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
  edge_driver_path = r"C:\Users\tejur\Downloads\msedgedriver.exe"  # Update this path

  # Initialize the Edge WebDriver
  try:
      # For newer versions of Selenium
      from selenium.webdriver.edge.service import Service
      edge_service = Service(executable_path=edge_driver_path)
      driver = webdriver.Edge(service=edge_service, options=edge_options)
      print("Edge WebDriver initialized successfully.")
  except Exception as e:
      print(f"Error initializing Edge WebDriver: {e}")
      exit(1)

  # Navigate to Bing.com
  try:
      driver.get("https://www.bing.com")
      print("Navigated to Bing.com")
  except Exception as e:
      print(f"Error navigating to Bing.com: {e}")
      driver.quit()
      exit(1)

  # Main loop
  try:
      while True:
          try:
              # Wait for the search box to be present
              search_box = WebDriverWait(driver, 10).until(
                  EC.presence_of_element_located((By.NAME, "q"))
              )
              print("Search box located.")

              # Clear the search box
              search_box.clear()

              # Choose a random topic
              topic = random.choice(topics)
              print(f"Searching for: {topic}")  # Log the topic being searched

              # Type the topic and submit
              search_box.send_keys(topic)
              search_box.send_keys(Keys.RETURN)

              # Wait for 5 seconds
              time.sleep(5)

              # Go back to Bing homepage
              driver.get("https://www.bing.com")
          except Exception as e:
              print(f"Error during search loop: {e}")
              break

  except KeyboardInterrupt:
      print("Script terminated by user.")
  finally:
      # Close the browser
      driver.quit()
      print("Browser closed.")