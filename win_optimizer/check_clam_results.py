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


	File name: check_clam_results.py
	Author: KM
	Date created: 2019 - 09 - 21
	Python Version: 3.7

	Description: 	Where the run_clamwin function kicks off the virus scan, this will
                    wait until the scan completes and check the results of the scan
                    log file.

                    If a threat is detected, this will connect to a GMail account and send
                    a mail alert. Upon completion of the alert, this function will remove
                    the scan results file.

                    GMail account requirements: You must go to the specified GMail accounts
                                                security settings, and enable "Less secure
                                                app access" to allow the program to
                                                authenticate to the account and send mail
                                                through it
					
						
'''

def check_clam_results(arguments_received, log_name, mail_recipient, mail_sender, password, system = 'N/A'):

    # ============================== Import Dependencies ============================== #

    # Built-in functions

    import	    subprocess                              # Allows calling PowerShell directly from Python / storing its stdout, stderr
    import      os                                      # Allows working with files / directories
    from        re              import      search      # Allows parsing PowerShell output
    import      smtplib, ssl                            # Allows sending mail from GMail SMTP server via SSL
    from        getpass		    import		getpass		# Used for hiding password input at console	

    # Functions built as part of this project

    from    output_progress     import      output_progress		


    # ============================== Begin Function ============================== #

    # Prompt for mail account and password to use with GMail account

    # print()
    # mail_recipient = input("Enter the email address to receive any alerts from the virus checker: ")
    # mail_sender = input("Enter the email address of a GMail account to send mail alerts from: ")
    # password = getpass("Enter the password for " + mail_sender + ": ")
    # print()
    # print('Now scanning system for infections')

    # Check if scan is still in progress. run_clamwin generates a scan_complete file when
    # the scan finishes

    still_scanning = True
    scan_complete_file = "C:\\Windows\\Temp\\ClamScan\\scan_complete.txt"

    while still_scanning == True:

        if not os.path.exists(scan_complete_file):

            still_scanning = True

        else:

            still_scanning = False
    

    # Once scan completes, store the results into a variable
   
    output_progress(arguments_received, 'Virus scan complete!', log_name)
    scan_result_file = open("C:\\Windows\\Temp\\ClamScan\\results.txt")
    scan_result_content = scan_result_file.read()
    scan_result_file.close()

    # Check results of scan / alert on any positives found

    if not search("Infected files: 0", scan_result_content):

        output_progress(arguments_received, 'Infection found!', log_name)
        
        # Define server settings for mail alerts to be sent from and mail message

        smtp_server = "smtp.gmail.com"
        port = 587
        sender = mail_sender
        recipient = mail_recipient
        subject = 'Subject: *** ALERT: Infection Found On Host ' + system + '! ***\n\n' # Double line break needed to have message appear properly in email
        quarantine = 'C:\Windows\Temp\ClamScan\Quarantine'
        message =   'ClamScan found infected files on host ' + system + ' They have been quarantined at ' + quarantine + '. Here are the results of the scan: \n\n' + scan_result_content
            
        # Create secure SSL connection to GMail server

        ssl_connection = ssl.create_default_context()

        # Log in to mail server and send message
        
        log_message = 'Attempting to log into GMail account ' + mail_sender + ' to send an alert message to ' + mail_recipient
        output_progress(arguments_received, log_message, log_name)

        try:
           
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            server.starttls(context=ssl_connection)
            server.ehlo()
            server.login(mail_sender, password)
            server.sendmail(sender, recipient, msg=subject + '\n\n' + message)
            output_progress(arguments_received, 'Message sent', log_name)

        except Exception as exception:

            # Print error message
            
            output_progress(arguments_received, 'Failed to connect to mail account. Here is the error: ' + exception, log_name)

            # Remove ClamScan scan complete file and results files
            
            output_progress(arguments_received, 'Removing scan progress files from C:\\Windows\\Temp\\ClamScan', log_name)

        finally:
            
            # Terminate connection with mail server

            output_progress(arguments_received, 'Terminating connection to GMail', log_name)
            server.quit()

            # Remove ClamScan scan complete file and results files

            output_progress(arguments_received, 'Removing scan progress files', log_name)
            os.remove('C:\\Windows\\Temp\\ClamScan\\scan_complete.txt')
            os.remove('C:\\Windows\\Temp\\ClamScan\\results.txt')

    else:

        output_progress(arguments_received, 'System clean, no infections found', log_name)

        # Remove ClamScan scan complete file and results files
        
        output_progress(arguments_received, 'Removing scan progress files', log_name)
        os.remove('C:\\Windows\\Temp\\ClamScan\\scan_complete.txt')
        os.remove('C:\\Windows\\Temp\\ClamScan\\results.txt')

    


    