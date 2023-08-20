# Sat-Watcher
Shell script for installing Satdump and other programs for receiving and decoding satelite images from Meteor M2-3 or the NOAA Satelites.
This is script is currently not complete!
# Usage
First make sure the script is executable with ```chmod +x sat-watcher.sh```.   
Based on your linux distribution, run it with ```./sat-watcher.sh install_debian``` or ```./sat-watcher.sh install_rh()```.  
The script does:
  - Download all dependencies for Satdump
  - Builds Satdump
  - Installs python dependencies
  - Sets up a cron entry for getting the time of the next pass
  - Cron executes python script, which retrives data from the N2YP API
  - (Not complete) Run Satdump in recorder mode at the passing time with at
    

