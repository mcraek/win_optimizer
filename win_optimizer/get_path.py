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


	File name: get_path.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

    Description:    Used for returning the proper file path to a resource such as an image, dll, data file, etc. for a script to reference
                    when a program is compiled to a single exe using PyInstaller. This allows a program to obtainthe proper filepath
                    to a resource regardless if it's run in Production as a its single exe form, or if it's run in development /
                    called as a script instead.
                    
    To use:         Pass the filepath of an item to this function. The filepath should be relative to the project's root directory.

    Example:        There is an image within project_name/project_name/images your GUI uses. Within the GUI build script add the following:
		     
                        from get_path import get_path
		                image = get_path(project_name/images/image.PNG)
		    
                    Note: Above we reference the path to the image relative to the project’s root directory. Not sure why this is a requirement, but it is

'''

def get_path(file_relative_path):

    import os # Needed for referencing relative paths of images used in GUI
    import sys # Used for referencing sys.MEIPASS (Temp directory PyInstaller creates for executable version of program in Production)

    try:
    
        # MEIPASS is an an attribute which stores the location of the tmp dir PyInstaller creates when a Python program is compiled to exe

        root_path = sys._MEIPASS

    # If MEIPASS doesn't exist, the program is not being executed from a compiled exe, return the file path of the file relative to the project
    # root dir instead of looking at the MEIPASS directory at all

    except Exception:
    
        root_path = os.path.abspath('.')

    return os.path.join(root_path, file_relative_path)