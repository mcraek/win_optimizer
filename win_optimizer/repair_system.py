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


	File name: repair_system.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Calls DISM and SFC via PowerShell on systems to run a repair
                    of any potentially corrupt system files.

                    DISM /online /cleanup-image /restorehealth is run first to make
                    sure SFC has a copy of healthy system files available to it
                    to run a repair.

                    SFC /scannow is run following DISM to run the repair of system
                    files

'''


def repair_system(arguments_received, log_name):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess	# Allows running PowerShell / cmd.exe commands
    import threading

    # Functions built as part of this project

    from    output_progress     import      output_progress
    

    # ============================== Begin Function ============================== #

    def tasks():

        # Call DISM first to ensure that if SFC finds any issues with the file system, it has the necessary
         # files it needs to run a repair

        output_progress(arguments_received, 'Running DISM to ensure healthy system files are available if needed by SFC scan', log_name)
        dism_cmd = "dism /online /cleanup-image /restorehealth"
        subprocess.call(['powershell.exe',dism_cmd]) # Output results to console

        # Once dism completes, run sfc /scannow to find and replace corrupted system files that may be causing performance or startup issues

        output_progress(arguments_received, 'Running SFC scan to repair system files', log_name)
        repair_cmd = "sfc /scannow"
        subprocess.call(['powershell.exe',repair_cmd]) # Output results to console

    thread = threading.Thread(target=(tasks))
    thread.start()