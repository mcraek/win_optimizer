'''

						//----------// LICENSING //----------//

			This file is part of the test_internet_speed program and is free software:
			you can redistribute it and/or modify it under the terms of the
			GNU General Public License as published by the Free Software Foundation,
			either version 3 of the License, or (at your option) any later version.
			This program is distributed in the hope that it will be useful,
			but WITHOUT ANY WARRANTY; without even the implied warranty of
			MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
			GNU General Public License for more details.
			You should have received a copy of the GNU General Public License
			along with this program. If not, see <https://www.gnu.org/licenses/>.

						//----------// LICENSING //----------//


	File name: run_clamwin.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Calls clamscan.exe to run a virus check on the system where the target is
                    specified by the user from the commandline if the -vc option is called

                    clamscan can be a bit slow so the following options are specified when
                    running the scan to mitigate this a bit:

                    1)  Only filetypes commonly associated with threats are scanned; e.g., .bat, 
                        .com, etc. The full list of filetypes scanned can be reviewed below

                    2)  A maximum filesize of 5MB is specified for files that are scanned in
                        order to speed up clamscan which can be rather slow otherwise

                    Infections are moved to C:\Windows\Temp\ClamScan\Quarantine

                    When the scan completes  scan_complete.txt file is created at
                    C:\Windows\Temp\ClamScan which check_clam_results.py actively
                    searches for

'''


def run_clamwin(arguments_received, log_name, target = 'C:'):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess      # Allows calling PowerShell directly from Python / storing its stdout, stderr
    import  os              # Allows working with files / directories

    # Functions built as part of this project

    from    output_progress     import      output_progress


    # ============================== Begin Function ============================== #

    # Create Scan Results Directory

    results_dir = "C:\Windows\Temp\ClamScan\Quarantine"

    if not os.path.exists(results_dir):

        output_progress(arguments_received, 'Creating scan results and quarantine directories at C:\\Windows\\Temp\\ClamScan', log_name)
        os.makedirs(results_dir)

    # Run ClamScan in Background, hide output, create scan_complete.txt file when scan is done

    if target == 'C:':

        location = 'C:'
    
    else:

        location = target
    
    # Define common infection filetypes                            
    filetypes = "--include='^.*.(bin|class|cmd|com|cpl|dll|doc|docx|eml|exe|htm|html|inf|jar|js|lnk|ocx|pdf|pif|ppt|rar|rtf|scr|swf|tmp|vbs|xls|xlsx|zip|plus|aspx|cab|drv|job|msi|pptx|reg|sys|url|vbe|py)$'"

    output_progress(arguments_received, 'Scanning the following location(s): ' + location, log_name)
    output_progress(arguments_received, 'Infected files will be moved to C:\\Windows\\Temp\\ClamScan\\Quarantine', log_name)
    print()
    
    # Define scan command to run silently and scan files of a maximum 5MB size and only those matching filetypes defined above for common threats
    
    # --log='C:\\Windows\\Temp\\ClamScan\\results.txt'
    scan_cmd = "Set-Location 'C:\\Program Files (x86)\ClamWin\\bin'; .\clamscan.exe " + location + " " + filetypes + " --max-filesize=5M" + " -v --show-progress -r --database='C:\\ProgramData\\.clamwin\\db' --infected --move='C:\\Windows\\Temp\\ClamScan\\Quarantine' --log='C:\\Windows\\Temp\\ClamScan\\results.txt'; New-Item 'C:\\Windows\\Temp\\ClamScan\\scan_complete.txt'"
    # start_scan = subprocess.Popen(['powershell.exe',scan_cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # Start scan / hide output from console
    subprocess.call(['powershell.exe',scan_cmd]) # Uncomment / call this to see scan results on console