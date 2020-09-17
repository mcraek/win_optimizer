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


	File name: clean_provisioned_apps.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Uses a combination of PowerShell's Get-AppXPackage, Get-AppXProvisionedPackage -online,
                    Remove-AppXPackage, and Remove-AppXProvisionedPackage -online for removing many of
                    the Windows 10 provisioned applications that install on each new profile.

                    This function uninstalls the apps installed on each profile and prevents them
                    from reinstallling when a new profile is created. This will not account for
                    any new provisioned apps Microsoft decides to push via Windows Updates / New
                    feature packs

                    The following provisioned apps are not removed through this process:

                    Calculator, Calendar, Camera, Mail, Weather, News, StickyNotes, Store, Camera
					
						
'''

def clean_provisioned_apps(arguments_received, log_name):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess	                    # Allows running PowerShell / cmd.exe commands
    import  threading

    # Functions built as part of this project

    from    output_progress     import      output_progress	


    # ============================== Begin Function ============================== #

    def tasks():

        output_progress(arguments_received, 'Initializing Win10 Provisioned Apps Removal...', log_name)
        remove_apps_cmdlet = 'Write-Output “`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`n`r`nRemoving Windows 10 Provisioned Apps. This may take a few minutes…” ; Get-AppXPackage -AllUsers  | Where-Object { $_.Name -NotLike “*calculator*” } | Where-Object { $_.Name -NotLike “*Calendar*” } | Where-Object { $_.Name -NotLike “*Camera*” } | Where-Object { $_.Name -NotLike “*Mail*” } | Where-Object { $_.Name -NotLike “*News*” } | Where-Object { $_.Name -NotLike “*Photos*” } | Where-Object { $_.Name -NotLike “*StickyNotes*” }  | Where-Object { $_.Name -NotLike “*Store*” } | Where-Object { $_.Name -NotLike “*Weather*” } | Where-Object { $_.Name -NotLike “*WindowsCommunicationsApps*” } | Remove-AppXPackage -ErrorAction ‘SilentlyContinue’ | Out-Null ; Get-AppXProvisionedPackage -Online | Where-Object { $_.Name -NotLike “*Calendar*” } | Where-Object { $_.Name -NotLike “*Camera*” } | Where-Object { $_.Name -NotLike “*Mail*” } | Where-Object { $_.Name -NotLike “*News*” } | Where-Object { $_.Name -NotLike “*Photos*” } | Where-Object { $_.Name -NotLike “*StickyNotes*” }  | Where-Object { $_.Name -NotLike “*Store*” } | Where-Object { $_.Name -NotLike “*Weather*” } | Where-Object { $_.Name -NotLike “*WindowsCommunicationsApps*” } | Remove-AppXProvisionedPackage -Online -ErrorAction ‘SilentlyContinue’ | Out-Null ; Write-Output “`r`nFinished removing Windows 10 Provisioned Apps”'
        subprocess.call(['powershell.exe',remove_apps_cmdlet]) # Output results to console
        output_progress(arguments_received, 'Windows 10 Provisioned Apps removal process complete', log_name)
    
    thread = threading.Thread(target=(tasks))
    thread.start()