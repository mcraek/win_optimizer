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
    
    File name: output_progress.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7


    Description: 	Used for outputting verbose messages to console as well as log file.
                    Is dependent on useage of the --verbose, and --debug options for main program.
					
'''


def output_progress(arguments_received, message, log_name):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import      os      # Used for writing output to text 

    # Functions built as part of this project

    from        print_msg       import      print_msg		# Print messages to console with auto time.sleep
    from	    datetime		import		datetime		# Used for logging current date / time of check & setting log file name


    # ============================== Begin Function ============================== #
    
    # Define function for writing log messages to text file in same directory as program

    def write_log(log_msg):

        # First check if log file already exists, create it if it doesn't

        log_check = os.path.exists('./' + log_name)

        if log_check == False:

            log_file = open(log_name,'w')
            log_file.close()
            
        # Append message to log file
            
        log_file = open(log_name,'a')
        log_file.write('\n' + message)
        log_file.close()

    # Receive / handle arguments passed to main program via commandline

    if arguments_received['Debug'] == 'true':
		
        write_log(message)

    if arguments_received['Verbose'] == 'true':

        print_msg(message)