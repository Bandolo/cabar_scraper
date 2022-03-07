# cabar_scraper
## How to Run the scraper
### Prerequisite
The only prerequisite you need is to have python3 installed in your machine.If you do not have Python installed, you can use this link to install it: https://www.python.org/downloads/

### Steps to follow
The steps are simple, and you just need to download this reporsitory, activate the virtual environment (venv) and run the scraper through the command line.
Below are the detailed steps.
- 1.) Fork this repository and download this whole directory to your local computer
- 2.) Using the terminal, navigate to the where you stored this downloaded reporsitory in your local computer
- 3.) Install Python 3.9 running the command 
''' 
brew install python@3.9"
'''
- 
- Activate the "venv" folder(the virtual environment) by running the command "venv\Scripts\activate" in your command prompt
- 4.) Once the (venv) environment is activated, run this code "python scraper.py".
- 5.) When you run the code, the scraper will ask you for two inputs:
  - "Please enter the Beginning ID number and press 'Enter'" : Here you enter the first matricule number you want the scraper to start scraping (for example 123439)
  - "Please enter the Ending ID number and press 'Enter'" : Here you enter the last matricule number you want the scraper to end with (for example 123500)
- 6.) After entering those two numbers and pressing "Enter" you just wait for the scraper to scrape all the pages
- 7.) At the end you will see a message telling you "the .json file has been successfully created.You can copy the scraped file".
- 8.) Finally you go the folder and you will see the newly created .json file.
