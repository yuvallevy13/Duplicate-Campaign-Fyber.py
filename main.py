from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import pyautogui
import time
import platform

# date = input("what the campaign date you want to duplicate?")
# new_date = input("What is today date?")
date = "14_Nov"
new_date = "19_Nov"

os = platform.system()
print(os)
input("df")
s = Service("C:\\Temp\\PSL\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)

# print(pyautogui.position())

# if needed to add more game we have to put his name in the list
gamelist = ["Go Toy!", "The Monster Hunter", "Crypto Magnet", "Eat Repeat", "Go Green!", "Go Candy!", "Crashy Cops 3D", "Prison Escape: Pin Puzzle", "Pin Pulls", "Axe Champ", "Tricky Holes"]

# if needed to add more campaign  we have to put his name in the list

campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                 "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_", "_9000M_android_Fyber_CPE_US_",
                 "_4000M_android_Fyber_CPE_US_", "_800M_android_Fyber_CPE_US_", "_android_Fyber_MR_CPE_HARD_BR_",
                 "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_", "_9000M_android_Fyber_CPE_BR_",
                 "_4000M_android_Fyber_CPE_BR_", "_800M_android_Fyber_CPE_BR_", "_android_Fyber_MR_CPE_Medium_GB_", "_android_Fyber_MR_CPE_Easy_WW_", "_android_Fyber_MR_CPE_Medium_WW_"]
########################################################################




driver.get("https://acp-edge.fyber.com/")
driver.maximize_window()
time.sleep(7)

email = driver.find_element(By.CSS_SELECTOR, '#email').send_keys("publishing@ovivogames.com")
time.sleep(1)
password = driver.find_element(By.CSS_SELECTOR, "#password").send_keys("123Rty098bnM!")
time.sleep(3)
signin = driver.find_element(By.CSS_SELECTOR,
                             "#auth > div > form > div > div > div:nth-child(4) > button > span.MuiButton-label.jss116.jss118").click()

for game in gamelist:
    # if needed to add more game we have to put his shortcut here #
    if game == "Go Toy!":
        game_shortcut = "GT"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                 "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_", "_9000M_android_Fyber_CPE_US_",
                 "_4000M_android_Fyber_CPE_US_", "_800M_android_Fyber_CPE_US_", "_android_Fyber_MR_CPE_HARD_BR_",
                 "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_", "_9000M_android_Fyber_CPE_BR_",
                 "_4000M_android_Fyber_CPE_BR_", "_800M_android_Fyber_CPE_BR_", "_android_Fyber_MR_CPE_Medium_GB_", "_8000M_android_Fyber_CPE_WW_", "_600M_android_Fyber_CPE_WW_",
                         "_android_Fyber_MR_CPE_Easy_WW_", "_android_Fyber_MR_CPE_Medium_WW_"]

    elif game == "Go Candy!":
        game_shortcut = "GC"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                 "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_", "_9000M_android_Fyber_CPE_US_",
                 "_4000M_android_Fyber_CPE_US_", "_800M_android_Fyber_CPE_US_", "_android_Fyber_MR_CPE_HARD_BR_",
                 "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_", "_9000M_android_Fyber_CPE_BR_",
                 "_4000M_android_Fyber_CPE_BR_", "_800M_android_Fyber_CPE_BR_", "_android_Fyber_MR_CPE_Medium_GB_", "_10000M_android_Fyber_CPE_WW_", "_650M_android_Fyber_CPE_WW_",
                         "_android_Fyber_MR_CPE_Easy_WW_", "_android_Fyber_MR_CPE_Medium_WW_"]

    elif game == "Go Green!":
        game_shortcut = "GG"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                 "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_", "_9000M_android_Fyber_CPE_US_",
                 "_4000M_android_Fyber_CPE_US_", "_800M_android_Fyber_CPE_US_", "_android_Fyber_MR_CPE_HARD_BR_",
                 "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_", "_9000M_android_Fyber_CPE_BR_",
                 "_4000M_android_Fyber_CPE_BR_", "_800M_android_Fyber_CPE_BR_", "_android_Fyber_MR_CPE_Medium_GB_", "_10000M_android_Fyber_CPE_WW_", "_700M_android_Fyber_CPE_WW_",
                         "_android_Fyber_MR_CPE_Easy_WW_", "_android_Fyber_MR_CPE_Medium_WW_"]

    elif game == "The Monster Hunter":
        game_shortcut = "TMH"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                 "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_", "_9000M_android_Fyber_CPE_US_",
                 "_4000M_android_Fyber_CPE_US_", "_800M_android_Fyber_CPE_US_", "_android_Fyber_MR_CPE_HARD_BR_",
                 "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_", "_9000M_android_Fyber_CPE_BR_",
                 "_4000M_android_Fyber_CPE_BR_", "_800M_android_Fyber_CPE_BR_", "_android_Fyber_MR_CPE_Medium_GB_", "_8500M_android_Fyber_CPE_WW_", "_750M_android_Fyber_CPE_WW_",
                         "_android_Fyber_MR_CPE_Easy_WW_", "_android_Fyber_MR_CPE_Medium_WW_"]

    elif game == "Crypto Magnet":
        game_shortcut = "CM"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                         "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_",
                         "_9000M_android_Fyber_CPE_US_",
                         "_4000M_android_Fyber_CPE_US_", "_800M_android_Fyber_CPE_US_",
                         "_android_Fyber_MR_CPE_HARD_BR_",
                         "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_",
                         "_9000M_android_Fyber_CPE_BR_",
                         "_4000M_android_Fyber_CPE_BR_", "_800M_android_Fyber_CPE_BR_",
                         "_android_Fyber_MR_CPE_Medium_GB_"]


    elif game == "Eat Repeat":

        game_shortcut = "ER"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                 "_10000M_android_Fyber_CPE_US_", "_10000M_android_Fyber_CPE_WW_", "_4000M_android_Fyber_CPE_WW_",
                 "_9500M_android_Fyber_CPE_WW_", "_800M_android_Fyber_CPE_WW_",
                 "_android_Fyber_MR_CPE_Medium_WW_"]

    elif game == "Pin Pulls":
        game_shortcut = "PP"
        campaignslist = ["_android_Fyber_Balloon_Unlock_13_CPE_US_", "_android_Fyber_Balloon_Unlock_13_CPE_WW_"]


    elif game == "Crashy Cops 3D":
        game_shortcut = "CC"
        campaignslist = ["_android_Fyber_ALL_CARS_CPE_WW_"]


    elif game == "Prison Escape: Pin Puzzle":
        game_shortcut = "PE"
        campaignslist = ["_android_Fyber_MR_CPE_Medium_WW_",
                         "_android_Fyber_MR_CPE_Medium_US_", "_300K_android_Fyber_CPE_WW_",
                         "_300K_android_Fyber_CPE_BR_", "_300K_android_Fyber_CPE_US_"]

    elif game == "Axe Champ":
        game_shortcut = "AC"
        campaignslist = ["_300K_Coins_android_Fyber_CPE_WW_", "_android_Fyber_CPE_Medium_US_",
                         "_300K_Coins_android_Fyber_CPE_US_", "_200K_Coins_android_Fyber_CPE_US_",
                         "_200K_Coins_android_Fyber_CPE_WW_", "_50K_Coins_android_Fyber_CPE_WW_"]

    elif game == "Tricky Holes":
        game_shortcut = "TH"
        campaignslist = ["_30K_android_Fyber_CPE_US_", "_100K_android_Fyber_CPE_US_",
                         "_50K_android_Fyber_CPE_US_"]

    search_game = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div[2]/input")
    search_game.send_keys(game)
    time.sleep(1)
    open_campaigns = driver.find_element(By.CSS_SELECTOR, "#product-table > div:nth-child(2) > table > tbody")
    open_campaigns.click()
    time.sleep(3)
    for campaign_name in campaignslist:

        campaign_game = game_shortcut + campaign_name + new_date
        my_file = open('C:\\Users\\User\\PycharmProjects\\duplicate_Campaign_in_fyber\\campaigns.txt', "r")
        data = my_file.read()
        list_if_need_to_stop = data.split("\n")

        if campaign_game in list_if_need_to_stop:
            pass
        else:
            search_campaign = driver.find_element(By.XPATH,
                                                  "/html/body/div[1]/div/div/main/div/div[2]/div[2]/table/tbody/tr[3]/td/div/div[1]/div/div[2]/input")
            search_campaign.send_keys(campaign_name + date)
            campaign_exact_name = driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div/div/main/div/div[2]/div[2]/table/tbody/tr[3]/td/div/div[2]/table/tbody/tr[1]/td[3]/span").text
            time.sleep(3)
            active_menu = pyautogui.click(1813, 898)
            time.sleep(2)
            duplicate = pyautogui.click(1702, 866)
            time.sleep(12)
            open_new_campaign = driver.find_element(By.CSS_SELECTOR,
                                                    "#ofw-campaign-table > div:nth-child(2) > table > tbody > tr:nth-child(2)")
            open_new_campaign.click()
            time.sleep(5)
            new_campaign_name = driver.find_element(By.CSS_SELECTOR, "#name")
            new_campaign_name_full = game_shortcut + campaign_name + new_date
            new_campaign_name.send_keys(Keys.CONTROL + 'a' + Keys.NULL, new_campaign_name_full)
            time.sleep(3)
            save = pyautogui.click(1836, 976)
            time.sleep(3)
            go_back = driver.find_element(By.LINK_TEXT, game)
            go_back.click()
            time.sleep(3)
            search_campaign_23 = driver.find_element(By.XPATH,
                                                     "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div[2]/input")
            search_campaign_23.send_keys(campaign_name + date)
            time.sleep(3)
            menu2 = pyautogui.click(1843, 592)
            time.sleep(2)
            disable = pyautogui.click(1709, 755)
            time.sleep(2)
            search_campaign_23.clear()
            time.sleep(1)
            search_campaign_23.send_keys(new_campaign_name_full)
            time.sleep(2)
            active_new_campigan = driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/div/div/main/div/div[2]/div[2]/table/tbody/tr/td[4]/div/div/button")
            active_new_campigan.click()
            time.sleep(2)
            back_to_deshbord = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div/h4/div/div[1]/a")
            back_to_deshbord.click()
            time.sleep(2)
            search_game_2 = driver.find_element(By.XPATH,
                                                "/html/body/div[1]/div/div/main/div/div[2]/div[1]/div/div[2]/input")
            search_game_2.send_keys(game)
            time.sleep(2)
            open_campaigns_2 = driver.find_element(By.CSS_SELECTOR, "#product-table > div:nth-child(2) > table > tbody")
            open_campaigns_2.click()
            time.sleep(2)
            my_file2 = open('C:\\Users\\User\\PycharmProjects\\duplicate_Campaign_in_fyber\\campaigns.txt', "a")
            my_file2.write(campaign_game + '\n')
            my_file2.close()

            time.sleep(1)
        campaignslist = ["_android_Fyber_MR_CPE_Medium_US_", "_android_Fyber_MR_CPE_Medium_WW_",
                         "_android_Fyber_MR_CPE_HARD_US_", "_10000M_android_Fyber_CPE_US_",
                         "_9000M_android_Fyber_CPE_US_", "_4000M_android_Fyber_CPE_US_",
                         "_800M_android_Fyber_CPE_US_", "_android_Fyber_MR_CPE_HARD_BR_",
                         "_android_Fyber_MR_CPE_Medium_BR_", "_10000M_android_Fyber_CPE_BR_",
                         "_9000M_android_Fyber_CPE_BR_", "_4000M_android_Fyber_CPE_BR_",
                         "_800M_android_Fyber_CPE_BR_", "_android_Fyber_MR_CPE_Medium_GB_"]
        
        campaignslist = ["_8000M_android_Fyber_CPE_WW_", "_600M_android_Fyber_CPE_WW_",
                         "_android_Fyber_MR_CPE_Easy_WW_", "_android_Fyber_MR_CPE_Medium_WW_"]

    driver.refresh()
    time.sleep(3)
