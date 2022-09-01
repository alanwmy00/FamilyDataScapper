import pandas as pd
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyshadow.main import Shadow
import csv, os, time, random

# We want data in the form of ID, Name, Spouse Flag, Birth, Death so that all objects (i.e., people) are in a consistent format and we don't need ugly text processing later
def get_single_person_info(family_info, pid, sp_flag):
    res = [pid]

    # I am sure there is bug here, for instance if a person is still alive " - " may not exist
    first_id = family_info.index(pid)
    #res.append(family_info[1][3:]) # Person Name. in the form of "to ..."

    #check for merge or deletion
    res.append(family_info[first_id - 3]) #is this not the name?
    if "Add Spouse" not in family_info or "chevron-down-medium" not in family_info:
        res.append("Merged/Deleted") #replace birth
        res.append("Merged/Deleted") #replace death
        res.append(sp_flag)
        return res
    
    if family_info[first_id - 2].find(" – ") == -1:
        res.append("No Date") #replace birth
        res.append("No Date") #replace death
    else:
        res.append(family_info[first_id - 2].split(" – ")[0])
        res.append(family_info[first_id - 2].split(" – ")[1])

    res.append(sp_flag)

    return res

def get_spouse_ids(family_info, p_id):   
    family_info = family_info[family_info.index("Add Spouse"):]
    family_info = family_info[:family_info.index("chevron-down-medium")]

    # Get all spouse info
    spouse_id_idxs = [idx for idx, element in enumerate(family_info) if (lambda x: "•" in x and p_id not in x)(element)]
    if spouse_id_idxs != None:
        spouse_list = []
        for i in spouse_id_idxs:
            spouse_list.append(family_info[i][4:]) # Spouse ID was losing 1st character
        return spouse_list

# Base URL
FS_URL = "https://www.familysearch.org/tree/person/details/"
# Data and logs will be saved in the script folder for ease of access
# PY_PATH = Path(__file__).parent.resolve()

# Load person of interest IDs. Saved flag is set after all data from a person is saved
# This might cause duplicates if a failure happens mid-save, but prevents skipping data. Duplicate detection is more easily automated.
poi_ids = [] #format of file: fsid, gender, allfourgrandparents, saved
data = []

df = pd.DataFrame()
df["FSID"] = None
df["Name"] = None
df["DOB"] = None
df["DOD"] = None
df["Spouse Of"] = None


# Ask for file name
while True:
    try:
        file_name = input("Please type the file name containing IDs, ignoring \".csv\", then hit enter/return: ") + ".csv"
        poi_ids = list(pd.read_csv(file_name).fsid)
        output_name = "data" + file_name.replace("forspouse", "")
        break
    except FileNotFoundError:
        print("File not found; please type the correct file name")

# Ask for username + password
while True:
    try:
        username = input("Please type your Family Search USERNAME here, then hit enter/return: ")
        password = input("Please type your Family Search PASSWORD here, then hit enter/return: ")
        if not username or not password:
            username = "hgiles2"
            password = "Why12Nokt"
        d = webdriver.Chrome(ChromeDriverManager().install())
        d.get("https://www.familysearch.org/auth/familysearch/login")
        #LOGIN: Each user should enter their own
        d.find_element(By.ID, "userName").send_keys(username)
        d.find_element(By.ID, "password").send_keys(password)
        d.find_element(By.ID, "login").click()
        for person in poi_ids:
            d.get(FS_URL + person)
            time.sleep(random.randint(3, 6))
            s = Shadow(d)
            fs_person_text = d.execute_script("return document.querySelector('fs-person-page')")
            family_text = fs_person_text.text.split("\n")
            #add this person's data to the large data list. Keep an eye on memory use here, in case the batch size gets too large. We can put a limit on batch size. 
            p_data = get_single_person_info(family_text, person, "")
            df.loc[df.shape[0] + 1] = p_data
            df.set_index("FSID").to_csv(output_name)

            #we only want to parse out spouses for people who are not merged or deleted
            if p_data[2] != "Merged/Deleted": 
                spouse_ids = get_spouse_ids(family_text, person)
                if spouse_ids != []:
                    for poi in spouse_ids:
                        #print("poi: |" + poi + "|")
                        d.get(FS_URL + poi)
                        time.sleep(random.randint(3, 6))
                        fs_sp_text = d.execute_script("return document.querySelector('fs-person-page')")
                        family_s_text = fs_sp_text.text.split("\n")
                        s_data = get_single_person_info(family_s_text, poi, person)
                        df.loc[df.shape[0] + 1] = s_data
                        df.set_index("FSID").to_csv(output_name)

        df.set_index("FSID").to_csv(output_name)
        d.quit()
        break

    except AttributeError:
        d.quit()
        print("\n***Wrong username password combination!***\n")
