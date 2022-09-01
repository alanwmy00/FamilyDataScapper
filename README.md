# Family Data Scrapper

This script scrapes FamilySearch for each ID's name and their spouse(s)'s IDs, name, birth and death date using Python and Selenium.

Starting with a list of IDs provided by Professor Costa, the script first loads those IDs and logs into FamilySearch.
From there, it saves the ID's name and their spouse(s)'s IDs, then loops through both the ID and their spouse(s)'s pages to get the necessary information (birth and death date) and saves them into a CSV file.

## Table of Contents/ Quick Links
#### [Windows Installation Instructions](https://github.com/h-e-gi/fs_sc#windows-installation-instructions-1)
<details><summary><i>Click to expand</i></summary>
<p>

##### [0. Download Google Chrome](https://github.com/h-e-gi/fs_sc#0-download-google-chrome-1)
##### [1. Create an Account](https://github.com/h-e-gi/fs_sc#1-create-an-account-1)
##### [2. Install Python ](https://github.com/h-e-gi/fs_sc#2-install-python)
##### [3. Check Python Version](https://github.com/h-e-gi/fs_sc#3-check-python-version-1)
##### [4. Install Essential Packages](https://github.com/h-e-gi/fs_sc#4-install-essential-packages-1)
##### [5. Run Code](https://github.com/h-e-gi/fs_sc#5-run-code-1)
   

</p>
</details>

#### [MacOS Installation Instructions](https://github.com/h-e-gi/fs_sc#macos-installation-instructions-1)
<details><summary><i>Click to expand</i></summary>
<p>

##### [0. Download Google Chrome](https://github.com/h-e-gi/fs_sc#0-download-google-chrome-3)
##### [1. Create an Account](https://github.com/h-e-gi/fs_sc#1-create-an-account-3)
##### [2. Install Python ](https://github.com/h-e-gi/fs_sc#2-install-python-1)
##### [3. Check Python Version](https://github.com/h-e-gi/fs_sc#3-check-python-version-3)
##### [4. Install Essential Packages](https://github.com/h-e-gi/fs_sc#4-install-essential-packages-3)
##### [5. Run Code](https://github.com/h-e-gi/fs_sc#5-run-code-3)
</p>
</details>

#### [Input and Output](https://github.com/h-e-gi/fs_sc#input-and-output-1)

#### [FAQ & Troubleshooting](https://github.com/h-e-gi/fs_sc#faq--troubleshooting-1)

## Windows Installation Instructions

*If you are on MacOS, click [here](https://github.com/h-e-gi/fs_sc/#macos-installation-instructions) for instructions.*

### 0. Download Google Chrome
*Skip to [Step 1](https://github.com/h-e-gi/fs_sc/#1-create-an-account) if you already have Chrome installed.*

You **must** have Google Chrome installed in order to scrape the family data. Other browsers will not work.

[Download and Install Google Chrome](https://www.google.com/chrome/)

### 1. Create an Account

Go to <https://www.familysearch.org/en/>. Create an account. You will need to verify your phone or email. Remember your username and password.

<a href="https://user-images.githubusercontent.com/27839519/148659492-8256a3fa-6252-49c5-8108-ac4f44adcb12.png"><img src="https://user-images.githubusercontent.com/27839519/148659492-8256a3fa-6252-49c5-8108-ac4f44adcb12.png" align="center" width="800" ></a>



### 2. Install Python 
*Skip to [Step 4](https://github.com/h-e-gi/fs_sc/#4-install-essential-packages) if Python is already installed on your computer.*

#### 2.1 
Go to <https://www.python.org/downloads/>. Click Download Python 3.10.1.

<a href="https://user-images.githubusercontent.com/27839519/148659505-6082db42-ac12-4f24-a0e4-650f7ef95e2d.png"><img src="https://user-images.githubusercontent.com/27839519/148659505-6082db42-ac12-4f24-a0e4-650f7ef95e2d.png" align="center" width="800" ></a>

#### 2.2

Open the `python-3.10.1-amd64.exe` file you just downloaded. (It may be under a different name if you have a 32-bit system.)

**IMPORTANT:** Make sure to select **Add Python 3.10 to PATH** before clicking **Install Now**.

![image](https://user-images.githubusercontent.com/27839519/148659513-ef802bf8-07dc-4a7c-bcd0-78740b49815e.png)

### 3. Check Python Version
*Run the following steps to make sure you have the correct version of Python and/or installed Python correctly.*
#### 3.1 
**Right click** the **Windows icon** at the bottom-left of your desktop. Click **Run**.

(Or if you are familiar with Windows shortcut, simply use `Win + R`)

![image](https://user-images.githubusercontent.com/27839519/148659640-c008571e-3db5-4beb-a3eb-8062f0d9d244.png)

#### 3.2 
Type `cmd` in the Run window. Then click `OK`.

<a href="https://user-images.githubusercontent.com/27839519/148659540-50573080-c74c-4419-aae7-0ae653471fe2.png"><img src="https://user-images.githubusercontent.com/27839519/148659540-50573080-c74c-4419-aae7-0ae653471fe2.png" align="center" width="500" ></a>

#### 3.3 
In the command window, first type `python -V`, then hit enter. 

Then type `pip -V`, hit enter. 

They should return the version number. If any of these lines returns an **error**, Python was not properly installed.  Revisit [Step 2](https://github.com/h-e-gi/fs_sc/#2-install-python) and reinstall Python.

*It's okay to have a different Python version, as long as it is Python 3.x*

<a href="https://user-images.githubusercontent.com/27839519/148659543-c6f811e5-3121-4b05-aa23-6bdca694c3ac.png"><img src="https://user-images.githubusercontent.com/27839519/148659543-c6f811e5-3121-4b05-aa23-6bdca694c3ac.png" align="center" width="800" ></a>

### 4. Install Essential Packages
Run the following commands in the cmd window, one by one.

`pip install selenium==3.141.0`

`pip install webdriver-manager`

`pip install pyshadow`

`pip install pandas`

### 5. Run Code

#### 5.1

Download all of these files as a ZIP file (or separately into one folder).  Extract files if you downloaded it as a ZIP file.

Download your assigned `forspouse_xxx.csv` from [Box](https://ucla.app.box.com/s/xgvowqrgsux1y43r8ygypwzeqwsqhyk2/folder/154016624276). Move the file to the same folder where `fs_scrape.py` is.

**IMPORTANT:** Make sure to have both `fs_scrape.py`and your assigned file in the same folder.

<a href="https://user-images.githubusercontent.com/97467067/149442733-6feaa1bb-db24-4d38-960b-c1b9eb1b9e9c.png"><img src="https://user-images.githubusercontent.com/97467067/149442733-6feaa1bb-db24-4d38-960b-c1b9eb1b9e9c.png" align="center" width="600" ></a>

#### 5.2

Again, right click windows icon, click **Run**, again type `cmd`.

<details><summary><b>If your folder is located on the desktop</b></summary>
<p>

Type `cd desktop`, hit enter. Jump to [Step 5.4](https://github.com/h-e-gi/fs_sc/#54)
   
<a href="https://user-images.githubusercontent.com/97467067/149431502-29bfbf8d-73dc-4cef-8a71-a611bc2d357a.png"><img src="https://user-images.githubusercontent.com/97467067/149431502-29bfbf8d-73dc-4cef-8a71-a611bc2d357a.png" align="center" width="700" ></a>
   

</p>
</details>

<details><summary><b>If your folder is not located on the desktop</b></summary>
<p>

Go to your folder, click the address bar, select your folder path and copy it.
  
<a href="https://user-images.githubusercontent.com/27839519/148662175-c1148a61-d55a-48ee-be9e-8ab9cdb5d9f9.png"><img src="https://user-images.githubusercontent.com/27839519/148662175-c1148a61-d55a-48ee-be9e-8ab9cdb5d9f9.png" align="center" width="700" ></a>

In the cmd window, type `C:` or `D:` or `E:` or `F:` depending on where drive your folder is in, hit enter.

 Type `cd` and then paste the folder path you just copied, hit enter. 
    
 (Right-click and paste is not available in the cmd window, but you can use `ctrl + v` to paste the path).

  <a href="https://user-images.githubusercontent.com/27839519/148662369-d89a46a6-b8e3-45dd-8b4a-0265e9611a6e.png"><img src="https://user-images.githubusercontent.com/27839519/148662369-d89a46a6-b8e3-45dd-8b4a-0265e9611a6e.png" align="center" width="700" ></a>


Your folder path should now be shown in the cmd window.
   

</p>
</details>




#### 5.3

Type `python fs_scrape.py`. 

The window will ask for the file name you want to use. For instance, if your assigned file is "forspouse11501.csv", please type "forspouse11501". Hit enter.

The window wil ask for your Family Search username and password. Please type them and hit enter after you finish.

Wait several minutes for it to run. A new Google Chrome window should open, automatically log into FamilySearch with your username and password, and begin loading pages. This window should close when the program is finished. 

After the program finishes, a `data.csv` should be saved in the folder.

-------

## MacOS Installation Instructions

If you are using Windows, click [here](https://github.com/h-e-gi/fs_sc/#windows-installation-instructions) for instructions.

### 0. Download Google Chrome
*Skip to [Step 1](https://github.com/h-e-gi/fs_sc#1-create-an-account-1) if you already have Chrome installed.*

You **must** have Google Chrome installed in order to scrape the family data. Other browsers will not work.

[Download and Install Google Chrome](https://www.google.com/chrome/)

### 1. Create an Account

Go to <https://www.familysearch.org/en/>. Create an account. You will need to verify your phone or email. Remember your username and password.

<a href="https://user-images.githubusercontent.com/27839519/148659492-8256a3fa-6252-49c5-8108-ac4f44adcb12.png"><img src="https://user-images.githubusercontent.com/27839519/148659492-8256a3fa-6252-49c5-8108-ac4f44adcb12.png" align="center" width="800" ></a>


## 2. Install Python 
*Skip to [Step 4](https://github.com/h-e-gi/fs_sc/#4-install-essential-packages) if Python is already installed on your computer.*

#### 2.1 
Go to <https://www.python.org/downloads/>. Click Download Python 3.10.1.

<a href="https://user-images.githubusercontent.com/27839519/148659505-6082db42-ac12-4f24-a0e4-650f7ef95e2d.png"><img src="https://user-images.githubusercontent.com/27839519/148659505-6082db42-ac12-4f24-a0e4-650f7ef95e2d.png" align="center" width="800" ></a>

#### 2.2

Open the `python-3.10.1-macos11.pkg` file you just downloaded.

Click `continue` on the instruction, agree to the `Software License Agreement`, and click `Install`.
Once finished, you can click on `Close Installer` and move it to Trash.
Your `Finder` will automatically pop up a window with content in your  `Python 3.10.` folder.

### 3. Check Python Version
*Run the following steps to make sure you have the correct version of Python and/or installed Python correctly.*

#### 3.1 
Open the **Applications** folder in your **Finder**.
**Double-click** the **Utilities** Folder.
Then double-click **Terminal**.

<a href="https://user-images.githubusercontent.com/97487962/149646849-2ab1fa3a-170f-4428-9384-6d3735458d1c.png"><img src="https://user-images.githubusercontent.com/97487962/149646849-2ab1fa3a-170f-4428-9384-6d3735458d1c.png" align="center" width="800" ></a>

### 3.2
At the prompt, type type `python3 -V`, hit enter. (Note: V upper-case)
This should return the version number. If any of these lines returns an **error**, Python was not properly installed.  Revisit [Step 2](https://github.com/h-e-gi/fs_sc#2-install-python) and reinstall Python.

*It's okay to have a different Python version, as long as it is Python 3.x*

<a href="https://user-images.githubusercontent.com/97487962/149650893-22ebffa8-8f63-46bd-9737-bbae0dc063f5.png"><img src="https://user-images.githubusercontent.com/97487962/149650893-22ebffa8-8f63-46bd-9737-bbae0dc063f5.png" align="center" width="800" ></a>

### 4. Install Essential Packages
Run the following commands in the cmd window, one by one.

`pip3 install selenium==3.141.0`

`pip3 install webdriver-manager`

`pip3 install pyshadow`

`pip3 install pandas`

### 5. Run Code

#### 5.1

Download all of these files as a ZIP file (or separately into one folder).  Extract files if you downloaded it as a ZIP file.

Download your assigned `forspouse_xxx.csv` from [Box](https://ucla.app.box.com/s/xgvowqrgsux1y43r8ygypwzeqwsqhyk2/folder/154016624276). Move the file to the same folder where `fs_scrape.py` is.

**IMPORTANT:** Make sure to have both `fs_scrape.py`and your assigned file in the same folder.

<a href="https://user-images.githubusercontent.com/97487962/149651273-0f1dd2d7-c10f-4107-b481-98dc1e85abd6.png"><img src="https://user-images.githubusercontent.com/97487962/149651273-0f1dd2d7-c10f-4107-b481-98dc1e85abd6.png" align="center" width="600" ></a>

#### 5.2

Again, in **Finder**, open **Application** folder, double-click **Utilities** and open **Terminal**.

<details><summary><b>If your folder is located on the desktop</b></summary>
<p>

Type `cd desktop`, hit enter. Then type `cd fs_sc-main`. 
Jump to [Step 5.4](https://github.com/h-e-gi/fs_sc/#54)
   
<a href="https://user-images.githubusercontent.com/97487962/149652093-3718e64b-06ca-41dc-862c-33ab1cd22049.png"><img src="https://user-images.githubusercontent.com/97487962/149652093-3718e64b-06ca-41dc-862c-33ab1cd22049.png" align="center" width="700" ></a>
   

</p>
</details>

<details><summary><b>If your folder is not located on the desktop</b></summary>
<p>

Go to your folder, two-finger tap the folder name and select **New Terminal at Folder**.
  
<a href="https://user-images.githubusercontent.com/97487962/149652253-5a81453f-c4dc-42d8-9dd0-073caa68d63a.png"><img src="https://user-images.githubusercontent.com/97487962/149652253-5a81453f-c4dc-42d8-9dd0-073caa68d63a.png" align="center" width="700" ></a>

You should now be in the path of your folder at your Terminal.
   
<a href="https://user-images.githubusercontent.com/97487962/149652436-493fb635-70a6-4ead-b3f4-08215ce5ceda.png"><img src="https://user-images.githubusercontent.com/97487962/149652436-493fb635-70a6-4ead-b3f4-08215ce5ceda.png" align="center" width="700" ></a>

   

</p>
</details>

#### 5.3

Type `python3 fs_scrape.py`. 

The window will ask for the file name you want to use. For instance, if your assigned file is "forspouse11501.csv", please type "forspouse11501". Hit return.

The window wil ask for your Family Search username and password. Please type them and hit return after you finish.

Wait several minutes for it to run. A new Google Chrome window should open, automatically log into FamilySearch with your username and password, and begin loading pages. This window should close when the program is finished. 

After the program finishes, a `data.csv` should be saved in the folder.

-------


## Input and Output

### persons.csv
This is the **input file** to the script. Each scraper will receive at least one, with one batch of IDs to be scraped per persons.csv file. The current batch's persons.csv file must be in the same folder as the script, and the first column must be the FamilySearch ID of the people being searched for. This file will be opened and read when the script starts, so that the script knows the list of IDs to query FamilySearch for.

### data.csv
This is the **output file** of the script. The scraper will save this line by line as data is scraped from FamilySearch. Each line repreesents one person, whether searched person or a spouse of a searched person. Each line contains the ID, name, birth date and death date of one person.  The Spouse Of flag field is either blank, indicating a person on the original search list in persons.csv, or holds a FamilySearch ID, indicating that the person in that line is a spouse of the person whose FamilySearch ID is the Spouse Of field.

### fs_scrape.py
This is the Python script we are using to scrape data.  No changes should be made to this file specifically except for the FamilySearch username and password and unless stated otherwise.

## FAQ & Troubleshooting

<!--Do not delete the spaces-->
<details><summary><b>Q: I run the script and Chrome opens, but nothing happens!</b></summary>
<p>

###### A: Make sure that all relevant files, such as persons.csv, data.csv, and the Python script, are closed before running the script.

</p>
</details>

<!--END OF SECTION-->

<details><summary><b>Q: I have some other technical question.</b></summary>
<p>

###### A: Please use hgiles@nber.org or the Discord server https://discord.gg/RcdQEnnQCB to reach Heather, who will be happy to talk with you.

</p>
</details>




