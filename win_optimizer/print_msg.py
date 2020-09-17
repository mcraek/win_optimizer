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


	File name: print_msg.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Receives a message to output to console and auto-formats it / allows for a 
                    brief pause as well before continuing

'''

def print_msg(message):

    # ============================== Import Built-in Dependencies ============================== #

    import      time

    # ============================== Begin Function ============================== #

    time.sleep(1)
    print()
    print(message)
    time.sleep(1)