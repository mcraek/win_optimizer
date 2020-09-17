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


	File name: check_arguments.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Receives / validates arguments passed to the main program and sets defaults in the event
                    certain arguments are not passed to the program.
					
                    Arguments passed are case insensitive
					
						
'''


def check_arguments():

    import argparse # Used for parsing arguments passed to program
    import sys      # Allows use of sys.exit() to end program in the event of an error

    # Specify valid arguments for program and set default values accordingly.

    parser = argparse.ArgumentParser(description='Set options for win_optimizer')

    parser.add_argument('-a', '--auto', dest='Auto', choices=['true','false'], type=str.lower,
                        help='if true, will run all optimizer options on the system',
                        default='false')

    parser.add_argument('-ac', '--appclean', dest='AppClean', choices=['true','false'], type=str.lower,
                        help='if true, will remove Windows 10 provisioned apps',
                        default='false')

    parser.add_argument('-d', '--debug', dest='Debug', choices=['true','false'], type=str.lower,
                        help='if true, outputs progress to a log file',
                        default='false')

    parser.add_argument('-dc', '--diskclean', dest='DiskClean', choices=['true','false'], type=str.lower,
                        help='if true, runs Disk Cleanup on system with almost all options selected',
                        default='false')

    parser.add_argument('-o', '--optimize', dest='Optimize', choices=['true','false'], type=str.lower,
                        help='if true, runs Optimize-Volume PowerShell cmdlet on all non-external drives with default options selected for the drive type; e.g., SSD / HDD', default='false')
    
    parser.add_argument('-r', '--repair', dest='Repair', choices=['true','false'], type=str.lower,
                        help='if true, runs DISM and SFC to repair file system',
                        default='false')

    parser.add_argument('-s', '--silent', dest='Silent', choices=['true','false'], type=str.lower,
                        help='if true, runs selected options on system without displaying console',
                        default='false')

    parser.add_argument('-v', '--verbose', dest='Verbose', choices=['true','false'], type=str.lower,
                        help='if true, outputs verbose messages to console as program runs',
                        default='false')

    parser.add_argument('-vc', '--viruscheck', dest='VirusCheck', choices=['true','false'], type=str.lower,
                        help='if true, runs a virus check on the system using ClamWin',
                        default='false')

    passed_arguments = (parser.parse_args())    # Validate arguments passed to program against above permitted arguments
                                                # vars returns the arguments as a dictionary which can be parsed as key > value
    
    # Return validated arguments to main program so it can pass them to other functions that may use them

    return passed_arguments