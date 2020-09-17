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


	File name: install_clamwin.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

    Description:    Uses Chocolatey to install ClamWin Free Antivurs if it's
                    not already installed to the system.

                    If ClamWin was not previously installed to the system,
                    this will return that fact so it can be uninstalled
                    following the completion of the scan

'''

def install_clamwin(arguments_received, log_name, remove='False'):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	subprocess	                    # Allows calling PowerShell directly from Python / storing its stdout, stderr
    from    re      import      search      # Allows parsing PowerShell output

    # Functions built as part of this project

    from    output_progress     import      output_progress


    # ============================== Begin Function ============================== #

    # Uninstall ClamWin If Option Was Passed To Remove It Via Chocolatey

    if remove == 'True':

        output_progress(arguments_received, 'Uninstalling ClamWin Via Chocolatey...', log_name)
        print()
        remove_cmd = "& C:\ProgramData\chocolatey\choco.exe uninstall clamwin --force -y"
        subprocess.call(['powershell.exe',remove_cmd]) # Use .call to output PowerShell to console instead of storing results to variable
        output_progress(arguments_received, 'ClamWin successfully removed', log_name)

        return None # Exit function upon uninstalling ClamWin
    
    else:

        # Check to see if ClamWin is already installed via PowerShell HKLM registry check, install ClamWin it if it's not found

        # Note: Absolute filepath for Chocolatey is called instead of just calling "choco" because if Chocolatey is not installed on a system
        # and this program installs it, a new terminal session must be started before the choco command can be run
        # Calling it via absolute filepath is an alternative to doing so

        output_progress(arguments_received, 'Checking to see if ClamWin is installed...', log_name)

        check_cmd = '$clam_check = Get-ItemProperty HKLM:/Software/Wow6432Node/Microsoft/Windows/CurrentVersion/Uninstall/* | Where-Object DisplayName -Like "ClamWin*" | Measure-Object ; $clam_check.count -gt 0'
        check_results = subprocess.Popen(['powershell.exe',check_cmd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT) #stdout accessible via [0], errors via [1]
        clamwin_installed = str(check_results.communicate()[0]) # Store stdout only
        
        # Install if not already installed

        if not search("True", clamwin_installed):
            
            output_progress(arguments_received, 'Installing ClamWin...', log_name)
            print()
            install_cmd = "& C:\ProgramData\chocolatey\choco.exe install clamwin --force -y"
            subprocess.call(['powershell.exe',install_cmd]) # Use .call to output PowerShell to console instead of storing results to variable

            # If ClamWin was not installed originally, store this fact

            clam_existing = False
            

        else:

            output_progress(arguments_received, 'ClamWin is already installed', log_name)
            clam_existing = True

        # Return Whether Or Not ClamWin Was Already Installed On The System

        return clam_existing
