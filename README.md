# TENABLE SC API - SCAN
![](https://img.shields.io/badge/Language-Python-green) 

------------


**TENABLE SC - SCAN** is a python script that creates and lunches vulnerability Assessment scans on Tenable SC, using Tenable API. 

### How it Works
The script first authenticates the user using authentication key, then it import the required information from Tenable SC to create the scan , such as the scan policy and the used repository. Then, the script creates the scan object, and lunches it. 

The output of the script is a scan object that can be found in **Active Scans** in Tenable SC, and it's result will be found in **Scan Results** after its done.

### Prerequisites
- You should have an access to Tenable SC, that is up and running.
- The API KEY should be generated for the user that is authorized to lunch scans on Tenable SC, its recommended to use Security Manager user or Admin.
- The Scan Policy that will be used in the script must be pre-configured in Tenable SC.
- The Repository that will be used in the script must be pre-configured in Tenable SC.

### How to Use
- Replace all of the text between the hashes symbols ## in the script file with its real value.
 EX: Replace #TENABLESC IP:PORT# with 10.9.0.1:443
 
- The script reads the target IP as a system argument.
  EX: To run the script in Linux terminal console: 
`$ python #PATH TO SCRIPT# #IP#`

### Author

Rawan Alserhani
rawanalserhani@gmail.com

