# MIE_group_26
## Introduction：
Group26 Dashboard is a comprehensive dashboard focused on prescription-related information, designed to offer extensive visualization and analysis of prescription drug data. 
This project combines medical data with a user-friendly interface, supporting healthcare professionals and analysts in gaining insights into prescription drug usage patterns.


## Installation:
1.Install Anaconda [Download Anaconda](https://www.anaconda.com/download) 

2.Set the environment for using anaconda.  
  Install the Flask framework for Python and its related extensions:  
  Type the following commands into the Anaconda prompt or Terminal window (pressing the Enter key after each command). When installing these modules,  
  type (y) for yes when prompted.

```
conda install -c anaconda flask
conda install -c conda-forge flask-sqlalchemy
conda install -c anaconda sqlalchemy
```

3.Using pycharm as IDE
  a. Download and install pycharm [PyCharm](https://www.jetbrains.com/pycharm/)
  b. Path to Anaconda Executable: 
Python for **Mac/Linux**- using the terminal (Mac)
Python for **windows** - Anaconda prompt/powershell (Windows) type
For example C:\Users\Administrator\anaconda3\python.exe (it depend on where you install anaconda in your machine)

In PyCharm click **File** -> **Settings** (or preferences for Mac) and choose the **Project: bcmicrosite** from the left hand side of the window. 
Open and click on the **Project Interpreter**. Then, using the plus button or add depending on your version of PyCharm type/paste the Anaconda path. 
You can also choose to do this just for this project if you already use PyCharm for other projects with the default interpreter. 
 
## Usage Instructions:
a. Click on the **'Code'** button, and copy the **'HTTPS'** option
b. Create a folder for the project on your machine, and
  For windows: Open Git bash
  For Mac: Open Terminal
c. Naviagte to the create folder using the command of **cd **
d. Type 

```
git init
```
Once in the folder, and type

```
 git clone <pasted HTTPS link here>
```

e. open the folder of cloned git code.
f. Run **run.py** in Pycharm
c. Access [http://127.0.0.1:5000/dashboard/home] in a browser to view the dashboard.

## Function:
Prescribing dashboard allows customers to clearly obtain the cost of drugs and the drugs with the highest sales volume, and provides the drugs prescribed by each PCT. 
The dashboard also calculates Serum creatinine based on a patient's height and weight,giving patients more flexibility.

## Contribution:
1. Average ACT cost developing & test --Fatima
2. Max quantity Item description & percentage bar showing of all prescriptions developing & test-- yutong&longdan
3. number of unique items in datasets developing &test --Michael
4. visualize the outcome on the interface -enze
5. Calculator & about pop-up --Michael & Longdan
6. Front-end and Back-end linkage --Yutong
7. Infection percentage --Fatima
8. Test suite --Enze

## FAQ:
There are different branches in this project. Tasks are submitted according to different task division and finally merged into the master. Viewers can enter different 
branches to view codes according to different requirements.


