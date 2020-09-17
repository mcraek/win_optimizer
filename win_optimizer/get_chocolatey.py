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


	File name: get_chocolatey.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Chocolatey is a popular Windows package manager used for simplifying downloading / installing
                    software on Windows systems similar to how you would in Linux environments via apt-get / rpm

                    This function utilizes a PowerShell script that is downloaded from the Chocolatey docs at
                    https://chocolatey.org/docs/installation and is run on the system for installing Chocolatey

                    Chocolatey itself installs to C:\ProgramData\chocolatey

                    If Chocolatey was not previously installed on the sytem, this function will return that fact
                    so it can be removed upon completion of the program running
					
						
'''


def get_chocolatey(arguments_received, log_name, remove='False'):

# ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess	                    # Allows calling PowerShell directly from Python / storing its stdout, stderr
    from    re      import      search      # Allows parsing PowerShell output
    import  shutil                          # Allows removing non-empty directories. Used for uninstalling Chocolatey

    # Functions built as part of this project

    from    output_progress     import      output_progress


# ============================== Begin Function ============================== #

    # Uninstall Chocolatey if it wasn't previously installed on the system

    if remove == 'True':

        output_progress(arguments_received, 'Uninstalling Chocolatey...', log_name)
        print()
        shutil.rmtree('C:\\ProgramData\\chocolatey')
        output_progress(arguments_received, 'Chocolatey successfully removed from system', log_name)
        
    else:

        # Check if Chocolatey is already installed
        
        output_progress(arguments_received, 'Checking to see if Chocolatey is installed...', log_name)

        check_cmd = "Test-Path $env:ProgramData\chocolatey\choco.exe"
        check_results = subprocess.Popen(['powershell.exe',check_cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #stdout accessible via [0], errors via [1]
        chocolatey_installed = str(check_results.communicate()[0]) # Store stdout only
        
        # Install if not already installed

        if not search("True", chocolatey_installed):
            
            output_progress(arguments_received, 'Installing Chocolatey', log_name)
            print()
            install_cmd = "Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
            subprocess.call(['powershell.exe',install_cmd]) # Use .call to output PowerShell to console instead of storing results to variable

            choco_existing = False

        else:

            output_progress(arguments_received, 'Chocolatey is already installed', log_name)

            choco_existing = True

        # Return if Chocolatey was already isntalled on the system or not

        return choco_existing