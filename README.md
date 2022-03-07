# cabar_scraper
## How to Run the scraper
### Steps to follow
The steps are simple, and you just need to download this reporsitory, activate the virtual environment (venv) and run the scraper through the command line.
Below are the detailed steps.
- 1.) Fork this repository and download this whole directory to your local computer
- 2.) Using the terminal, navigate to the where you stored this downloaded reporsitory in your local computer
- 3.) Install Python 3.9 by running the command "__brew install python@3.9__"
- 4.) Install the latest version of pip by using the command "__python3.9 -m pip install --user --upgrade pip__"
- 5.) Install the virtual environment by running "__python3.9 -m pip install --user virtualenv__"
- 6.) Activate the virtual environment by running "__source venv/Scripts/activate__"
- 7.) Install Selenium by running "__sudo pip3 install selenium__"
- 8.) Instal webdriver-manager by running "__sudo pip3 install webdriver-manager__"
- 9.) Install chromediver vy running "__brew cask install chromedrive__"
- 10.) Once the (venv) environment is activated, run this code "__python scraper.py__".
- 11.) When you run the code, the scraper will ask you for two inputs:
  - "Please enter the Beginning ID number and press 'Enter'" : Here you enter the first matricule number you want the scraper to start scraping (for example 123439)
  - "Please enter the Ending ID number and press 'Enter'" : Here you enter the last matricule number you want the scraper to end with (for example 123500)
- 12.) After entering those two numbers and pressing "Enter" you just wait for the scraper to scrape all the pages
- 13.) At the end you will see a message telling you "the .json file has been successfully created.You can copy the scraped file".
- 14.) Finally you go the folder and you will see the newly created .json file.
