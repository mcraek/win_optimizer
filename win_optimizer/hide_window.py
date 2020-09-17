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


	File name: hide_window.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

    Description:    This is used for hiding particular windows that appear on screen by passing the
                    Title that appears at the top of the window to hide to this function.

                    In the context of this program, this function is used for hiding any open
                    PowerShell or cmd prompt windows if the --silent option is passed to the program.

                    Something to keep in mind is this will also hide any other PowerShell / cmd prompts
                    open that may be running other tasks at the same time as well

'''

def hide_window(window):

	# ============================== Import Dependencies ============================== #

	# 3rd party modules installed as part of this project

    import      win32gui		# Used for hiding console for --silent option (installed with pip install pywin32)
                                # win32gui is an installed package to this program


    # ============================== Begin Function ============================== #	

    # Define a function which is used to catch and store a target window for hiding

    def get_windows(window_to_hide, list_of_windows):

        window_text = win32gui.GetWindowText(window_to_hide)
        class_name = win32gui.GetClassName(window_to_hide)

        if window_text.find(window) >= 0:

            list_of_windows.append((window_to_hide, window_text, class_name))	

    # Store all open windows in an array

    all_windows = []
    win32gui.EnumWindows(get_windows, all_windows)

    # Use the function defined above to iterate through all open windows, capture the target
    # Python console for the program, and hide it in case a silent option was specified

    for window_to_hide, window_text, class_name in all_windows:

        win32gui.ShowWindow(window_to_hide, False)