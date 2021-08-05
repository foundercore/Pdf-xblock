pdfJsXblock
=========

### Description ###


### Customize the XBlock ###


### Install / Update the XBlock ###

    # Move to the folder where you want to download the XBlock
    cd /edx/app/edxapp
    # Download the XBlock
   
    # Install the XBlock
    pip install pdfJsXblock/
    # Upgrade the XBlock if it is already installed, using --upgrade
    pip install --upgarde pdfJsXblock/

    # Remove the installation files
    sudo rm -r pdfJsXblock

### Reboot if something isn't right ###

    sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:

### Activate the XBlock in your course ###
Go to `Settings -> Advanced Settings` and set `advanced_modules` to `["pdfjsxblock"]`.

### Use the XBlock in a unit ###
Select `Advanced -> PDF_JS` in your unit.

### Deploy XBlock Command ###
git clone https://github.com/foundercore/pdfXBlock.git
sudo /opt/bitnami/use_edx
source /opt/bitnami/apps/edx/venvs/edxapp/bin/activate
pip install /home/bitnami/pdfXBlock/
sudo /opt/bitnami/ctlscript.sh restart apache

newrelic - monitoring tool
