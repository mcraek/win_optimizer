# Note there are some things missing from this; e.g., a license section within the classifiers

import setuptools

# Open README when Executing Program

def readme():
    with open('README.md') as r:
        return r.read()

setuptools.setup(
      name='win_optimizer',
      version='1.0',
      scripts=['win_optimizer/check_arguments.py','win_optimizer/check_clam_results.py','win_optimizer/clean_disk.py',
				'win_optimizer/clean_provisioned_apps.py','win_optimizer/get_chocolatey','win_optimizer/get_path',
				'win_optimizer/hide_window','win_optimizer/install_clamwin.py','win_optimizer/optimize_volumes',
				'win_optimizer/output_progress','win_optimizer/print_msg.py','win_optimizer/repair_system.py',
				'win_optimizer/run_clamwin.py','win_optimizer/win_optimizer.py'],
      description='Used for optimizing Windows 10 systems',
      long_description=readme(), # Auto add the README to the long description attribute
      author='Kyle McRae', 
      author_email='kylemcrae770@gmail.com',
      packages=setuptools.find_packages(), 
      include_package_data=True,
      zip_safe=False,	

      classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Windows",
		"License:: OSI Approved :: GNU Lesser General Public License (LGPL 3)+"
      ],  
	  
)