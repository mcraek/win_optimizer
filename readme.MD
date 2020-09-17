## Program Name 
win_optimizer

## Requirements
Minimum Python version 3.7.3

## Setup
1) Create and activate your virtual environment
2) Install requirements with pip install -r requirements.txt

## Summary
Performs various tasks for optimizing Windows 10 operating systems, and also runs in combination
with ClamWin Free Antivirus for performing virus checks / sending alerts to a GMail account.

When multiple options are selected; e.g., --auto, optimization options are run in parallel

**Requires elevated privileges**

## Author
Kyle McRae

## Arguments

-a, --auto {true, false}, default = false: Runs all optimization options. Multiple options run at once. Recommended only if running unattended as console output can be difficult to make sense of.

-ac, --appclean {true, false}, default = false: Use with caution. This uses a combination of PowerShell's Get-AppXPackage, 
Get-AppXProvisionedPackage -online, Remove-AppXPackage, and Remove-AppXProvisionedPackage -online 
for removing many of the Windows 10 default provisioned applications that install on each new profile.

This function uninstalls the apps installed on each profile and prevents them
from reinstallling when a new profile is created. This will not account for
any new provisioned apps Microsoft decides to push via Windows Updates / New
feature packs

The following provisioned apps are not removed through this process:

Calculator, Calendar, Camera, Mail, Weather, News, StickyNotes, Store, Camera


-d, --debug {true, false}, default = false: Outputs program progress to a log file in the same
directory as the executable with the following syntax for the filename: system_name-date-win_opt-log.txt


-dc, --discclean {true, false}, default = false: Imports a registry key that was created using cleanmgr /sageset:64
to specify which clean options should be selected when Disk Cleanup
is run using option 64

The imported key is an export of HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\VolumeCaches
where CleanMgr parameters for option 64 are specified.

The following DiskCleanup options are selected for option 64:

Temporary Setup Files
Old Chkdsk files
Setup Log Files
Windows Update Cleanup
Windows Defender Antivirus (non-critical files)
Windows updgrade log files
Diagnostic data viewer database files
Downloaded Program Files (ActiveX / Java temp files)
Temporary Internet Files
System error memory dump files
System error minidump files
Windows error reports and feedback diagnostics
BranchCache
DirectX Shader Cache
Delivery Optimization Files
Language Resource Files
Recycle Bin
RetailDemo Offline Content
Update package Backup Files
Temporary files
Thumbnails
User file history

The following options are omitted for option 64:

Downloads


-o, --optimize {true, false}, default = false: Uses PowerShell's Optimize-Volume cmdlet for running its default disk
optimization techniques on all non-external drives connected to the
system.

For example:    PowerShell will perform different optimization actions
                depending on the type of drive the cmdlet is run on;
                e.g., HDDs will be defragmented while SSDs are retrimmed,
                as defragmenting SSDs is not recommended


-r, --repair {true, false}, default = false: Calls DISM and SFC via PowerShell on systems to run a repair
of any potentially corrupt system files.

DISM /online /cleanup-image /restorehealth is run first to make
sure SFC has a copy of healthy system files available to it
to run a repair.

SFC /scannow is run following DISM to run the repair of system
files


-s, --silent {true, false}, default = false: Hides PowerShell / command prompt (x64)
window while prpogram runs. 

Notes / Warning: 

1) This will not hide additional windows that pop up during some of the other options;
e.g., the Disk Cleanup portion will still display a status bar, installing ClamWin will
show the installer window as well 

2) This will hide any open PowerShell / command prompt windows that may be open performing
other tasks at the time


-v, --verbose {true, false}, default = false: Displays program progress to console while running


-vc, --viruscheck {true, false}, default = false: Scans specified directories using ClamWin Free
Antivirus. If ClamWin is not installed on the system, it will be installed via Chocolatey.

After the scan, if Chocolatey / ClamWin were not originally on the system when the program ran,
they are uninstalled.

Sends alerts on any detected threats using a GMail account specified by the user in the command
prompt. 

When prompted for directories to scan separate them with spaces such as the following format:

C:\Windows C:\Users D: E:\Files


# Requirements for VirusCheck Option Re: Alerting Via Email

-   Alerts are sent using a GMail account

-   In order for this option to run successfully, you must go to the specified GMail accounts
    security settings, and enable "Less secure app access" to allow the program to
    authenticate to the account and send mail through it

## Examples:

python .\win_optimizer.py -a True - Runs all options

python .\win_optimizer.py -dc True -v True - Runs disk check option with verbose output
    
## Meta

Distributed under the GNU Lesser General Public License (LGPL 3)+. See LICENSE file for more information.