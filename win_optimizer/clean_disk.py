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


	File name: clean_disk.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Imports a registry key that was created using cleanmgr /sageset:64
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

						
'''

def clean_disk(arguments_received, log_name):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess	# Allows importing registry keys to local system, running PowerShell cmdlets
    import  threading

    # Functions built as part of this project

    from    get_path    import      get_path    # Depending on whether this file is run in development or production, this will return the proper path of
                                                # a resource such as an image, .dll, data file, etc. this script might reference

    from    output_progress     import      output_progress		


    # ============================== Begin Function ============================== #

    def tasks():

        # Import registry keys for creating Disk Cleanup option 64 which has all cleanup options selected

        output_progress(arguments_received, 'Importing registry key settings for configuring Disk Cleanup options', log_name)
        reg_keys = get_path('win_optimizer\\resources\clean_mgr_reg_keys.reg') # Define path within project files to registry key file to import
        print()
        subprocess.call(['reg', 'import', reg_keys]) # Import registry keys for creating Disk Cleanup Option 64

        # Run Disk Cleanup with our selected options

        output_progress(arguments_received, 'Running Disk Cleanup', log_name)
        clean_cmd = "cleanmgr /sagerun:64"
        subprocess.call(['powershell.exe',clean_cmd]) # Output results to console

    thread = threading.Thread(target=(tasks))
    thread.start()

    








    




