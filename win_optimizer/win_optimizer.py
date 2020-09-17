#!../bin/env python

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


	File name: win_optimizer.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description:	Performs various tasks for optimizing Windows 10 operating systems. Runs in combination
					with ClamWin Free Antivirus for performing virus checks / sending alerts to a GMail account
					and will also perform the following additional tasks:

					DiskCleanup 				- 	Uses the builtin CleanMgr tool to perform a number of the cleanup options for 
													both normal / system file cleans

					System File Repair 			-	Uses the builtin DISM and SFC utilities to repair corrupt system files
													that may be causing performance / startup issues

					Disk Optimization 			-	Uses PowerShell's Optimize-Volume cmdlet for performing disk optimization;
													e.g., disk defragmenting of all non-external drives connected to the system

					Provisioned App Removal 	- 	Removes most of the provisioned apps from the system while keeping the following:
													Calculator, Calendar, Camera, Mail, Weather, News, StickyNotes, Store, Camera
					
					When multiple options are selected; e.g., All - Tasks are run in parallel with each other through threading
						
'''

def win_optimizer():

# //--- Debug --- // #

		# Copy and paste the following line into a PoSh terminal to test running the program using your virtual environment
		# Accepts arguments as well:
		# & "D:\Scripts\Python\win_optimizer\bin\env\Scripts\python.exe" "D:\Scripts\Python\win_optimizer\win_optimizer\win_optimizer.py" -d True -v True

	# //--- Debug --- // #

	# ============================== Import Dependencies ============================== #

	# Built-in functions

	import		ctypes										# Allows checking if program was run with elevated privileges
	import		win32ui										# Used for showing message box if program not run as Administrator
	import		threading									# Allows running multiple tasks as separate threads on the system
	import		socket										# Allows retrieving hostname of system. Used for forming log file name / virus check alert
	from		datetime		import		datetime		# Used for logging current date / time of check
	import									subprocess		# Used for hiding consoles with --silent option
	import		sys											# Allows terminating the program after the Auto option runs all optimization options
	from        getpass		    import		getpass			# Used for hiding password input at console


	# Functions built as part of this project

	from		check_arguments				import			check_arguments			# Parses arguments passed to commandline to check their valditity
	from		output_progress				import			output_progress			# Writes output to console / log file
	from		print_msg					import			print_msg				# Writes to console only
	from		hide_window					import			hide_window				# Used for hiding console windows when --silent option is used
	from		get_chocolatey				import			get_chocolatey			# Installs Chocolatey to the system for VirusCheck option
	from		install_clamwin				import			install_clamwin			# Installs ClamWin to the system for VirusCheck option 
	from		run_clamwin					import			run_clamwin				# Runs the ClamWin scan on the system via PowerShell call
	from		check_clam_results			import			check_clam_results		# Checks scan results file generated by ClamWin / alerts on discovered threats
	from		clean_disk					import			clean_disk				# Runs CleanMgr options via imported registry key
	from		repair_system				import			repair_system			# Runs DISM / SFC to run system file repairs
	from		optimize_volumes			import			optimize_volumes		# Runs PowerShell's Optimize-Volume cmdlet on all non-external drives
	from		clean_provisioned_apps		import			clean_provisioned_apps	# Removes many Win10 provisioned apps from system


	# Check to see if program was run as Administrator, exit if not

	if not (ctypes.windll.shell32.IsUserAnAdmin()):

		win32ui.MessageBox("Please run this program with elevated privileges", "Win Optimizer v. 1.0 - © Kyle McRae, 2020")
		sys.exit()
	
	#  ============================== Check / Handle arguments passed to program, also set default values here for parameters if necessary  ============================== #

	arguments_received = vars(check_arguments()) 	# Parse arguments submitted to program and store them into a variable
													# This is used to pass the arguments to further commands below.
													# If the user executes the program with no arguments passed. This will
													# set default values.
													# Important note: Do not pass sys.argv to argparse. It automatically
													# handles this, and passing sys.argv just confuses / breaks things with it

	# Format Log File Name / Get Hostname

	system_name = str(socket.gethostname())
	date = datetime.now()
	date = date.strftime("%d-%m-%Y %H-%M")
	log_name = system_name + '-' + date + '-win_opt-log.txt' # Set log file name for program results


	# --------------- Output starting messages to user / set initial variables for program --------------- #

	output_progress(arguments_received, '------------------- Win Optimizer v. 1.0 - © Kyle McRae, 2020 -------------------\n', log_name)


	# --------------- Reset variables to values explicitly passed to program /  hide console if silent option passed  --------------- #

	if arguments_received['Debug'] == 'true':
		
		debug = 'true'
		print_msg('Debug logging enabled. Verbose output will be saved to ' + log_name + ' file within program directory')

	if arguments_received['Verbose'] == 'true':

		verbose = 'true'
		print_msg('Verbose option specified. Program progress will be output to console')

	if arguments_received['Silent'] == 'true':

		# Hide Any PowerShell / cmd Windows

		hide_window('Windows PowerShell')
		hide_window('PowerShell 6 (x64)')
		hide_window('C:\Program Files\PowerShell\6\pwsh.exe')
		hide_window('C:\WINDOWS\system32\cmd.exe')
		hide_window('Command Prompt')


	# ============================== Begin Function ============================== #

	# Define function for Virus Check as it invovles several scripts and is called multiple times below (auto option and if explicitly called)

	def virus_check(arguments_received, log_name, system_name):

		output_progress(arguments_received, 'Initializing Virus Check of System', log_name)

		# Query for mail sender / recipient details

		print()
		mail_recipient = input("Enter the email address to receive any alerts from the virus checker: ")
		mail_sender = input("Enter the email address of a GMail account to send mail alerts from: ")
		password = getpass("Enter the password for " + mail_sender + ": ")

		# Query for directory to scan

		target = input("Enter the directories to scan (Default = [C:]); e.g., C:\Windows D: ")

		# Once query is complete, start scan under a separate thread
		
		def tasks():

			# Check if Chocolatey is installed on the system, install it if it isn't found, store whether it was previously installed or not

			chocolatey_exists = get_chocolatey(arguments_received, log_name)

			# Check if ClamWin Installed, Install It Via Chocolatey If Not, store whether it was previously installed or not

			clamwin_exists = install_clamwin(arguments_received, log_name)

			# # Run ClamWin scan in the background, quarantine any infected files found

			run_clamwin(arguments_received, log_name, target)

			# Run continuous check of ClamWin scan in the background, check results once scan completes, email alert on positives found

			check_clam_results(arguments_received, log_name, mail_recipient, mail_sender, password, system = system_name)

			# If ClamWin was not originally on the system, uninstall it

			if clamwin_exists == False:

				install_clamwin(arguments_received, log_name, remove='True')
			
			# If Chocolatey was not originally on the system, uninstall it

			if chocolatey_exists == False:

				get_chocolatey(arguments_received, log_name, remove='True')

		thread = threading.Thread(target=(tasks))
		thread.start()


	# --------------- Run All Optimization Options If Selected, Exit Program --------------- #

	if arguments_received['Auto'] == 'true':

		virus_check(arguments_received, log_name, system_name)
		clean_disk(arguments_received, log_name)
		repair_system(arguments_received, log_name)
		optimize_volumes(arguments_received, log_name)
		clean_provisioned_apps(arguments_received, log_name)

		sys.exit()

	# --------------- If Auto Is Not Chosen, Determine Which Optimization Options To Run / Start The Tasks As Needed In Parallel --------------- #

	else:

		# --------------- Download, Install & Run ClamWin Antivirus Via Chocolatey --------------- #

		if arguments_received['VirusCheck'] == 'true':

			virus_check(arguments_received, log_name, system_name)


		# --------------- Run Disk Cleanup W/ Almost All Options Selected --------------- #

		if arguments_received['DiskClean'] == 'true':

			# Import registry keys which create a Disk Cleanup option called "64" that has all Disk Cleanup options selected
			# and run Disk cleanup with these options selected
			
			clean_disk(arguments_received, log_name)


		# --------------- Run DISM and SFC SCANNOW To Fix Filesystem Errors --------------- #

		if arguments_received['Repair'] == 'true':

			repair_system(arguments_received, log_name)


		# --------------- Optimize Volumes (Includes Defragmentation If Needed) --------------- #

		if arguments_received['Optimize'] == 'true':

			optimize_volumes(arguments_received, log_name)


		# --------------- Remove Win10 Provisioned Apps --------------- #

		if arguments_received['AppClean'] == 'true':

			clean_provisioned_apps(arguments_received, log_name)


# Execute the program

win_optimizer()