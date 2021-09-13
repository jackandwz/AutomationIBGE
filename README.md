# IBGE Automation

This file should guide you through the configuration for running correctly this automation in any environment.

## UiPath Solution

The solution was projected to navigate inside IBGE Concla Web page and scrap information under each section of CNAE economic code and description, save in excel file and transform the data inside of it using Python script.

Each section will be acessed and scrapped 

## Prerequisites - Assumptions
Environment/System: 
\
Windows only.
\
Excel need to be installed.
\
Chrome need to be installed and in Portuguese-BR language.
\
Python3.6 need to be installed 
\
unidecode Imports need to be installed on Python.


Uipath Dependences:
\
Uipath.Excel.Activities
\
Uipath.Python.Activities
\
Uipath.System.Activities
\
Uipath.UiAutomation.Activities
\
UipathTeam.Excel.Extensions.Activities.

Config file:
\
variable strPythonFolder need to be a valid folder with valid Python root folder installation (Userprofile is dynamic placed).
\
variable strIBGEUrl need to be a valid URL for IBGE Concla site.
\
variable strLocalArquivo need to be a valid path. File don't necessary need to exist (userprofile variable is dynamic placed).

# UiPath Project Folder Structure
AutomacaoIBGE\Component: root folder for the main activities used in project:
* AutomacaoIBGE\Component\IBGE: In this folder, has the main "Get" activities for scraping data from the urls. 
They will be called from Main\Process in chain, each on depending on the level of the page.
\
Following this sequence: Main>Process>GetDivisoes>GetGrupo>GetClasse>GetSubClasse


* AutomacaoIBGE\Component\Python: In this folder, has 2 important files: Functions.py and Python.xaml. 

Python folder:
* Functions.py contains the main methods used inside UiPath to transform data inside excel file: 
\
*UpToLower function will place all chars from Uper to Lower case. 
\
*CodCorrections function will take off all non-numerical chars from section codes.
\
*FixColumnNames will take all the acents from column names of the dataset.

* Python.xaml contains the main methods for calling and running Python scripts for each row of the dataset.

AutomacaoIBGE\Data: this folder contain the config file, with variables of the project:
* strIBGEUrl: Valid url for accesing IBGE portal and scrap infos.
* strSecao: Sections to be scaped, default is "A,B,C", will be deserialized as array and work in a for each loop.
* strLocalArquivo: This string will be complemented with userprofile environment variable "%userprofile%" in the begining of the string. The default folder for downloading and working with the file containing scrapped information.
* strPythonFolder: Python default folder, depending of the user running it, default folder is \AppData\Local\Programs\Python\Python36-32 and the start of the string will be replaced with the environment variable userprofile.

AutomacaoIBGE\Framework:
* InitAllApplications: This sequence is responsable for initializing Chrome and cleaning old excel file.
* InitAllSettings: This sequence read the configuration file and get the core variables for running the automation.
* KillAllProcess: This sequence is used to kill Chrome and Excel process before start and after finishe the process.
# Root Project Folder Structure
* AutomacaoIBGE: Previous defined in UiPath Project Folder Structure.
* Python: This folder contain a cmd responsable for installing imports needed for running this automation (unidecode).
* Raw: This folder is the temp folder where excel file will be stored and transformed.
