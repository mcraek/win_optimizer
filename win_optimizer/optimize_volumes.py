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


	File name: optimize_volumes.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

    Description:    Uses PowerShell's Optimize-Volume cmdlet for running its default disk
                    optimization techniques on all non-external drives connected to the
                    system.

                    For example:    PowerShell will perform different optimization actions
                                    depending on the type of drive the cmdlet is run on;
                                    e.g., HDDs will be defragmented while SSDs are retrimmed,
                                    as defragmenting SSDs is not recommended

'''

def optimize_volumes(arguments_received, log_name):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess	                    # Allows running PowerShell / cmd.exe commands
    from    re      import      search      # Allows parsing PowerShell output
    import  threading                      

    # Functions built as part of this project

    from    output_progress     import      output_progress	


    # ============================== Begin Function ============================== #

    def tasks():

        output_progress(arguments_received, 'Performing Disk Optimization for all volumes', log_name)
        optimize_cmdlet = "(get-disk | where BusType -ne USB | Get-Partition | Get-Volume | Where {$_.DriveLetter -ne $null} | Select DriveLetter).DriveLetter | foreach { Optimize-Volume -DriveLetter $_ -Verbose }"
        subprocess.call(['powershell.exe',optimize_cmdlet]) # Show PowerShell output to console

    thread = threading.Thread(target=(tasks))
    thread.start()