# FastPace
A personal project aimed at probing the dark web ("Onionland" to be specific). Dependencies required.

# Installation (Debian)

1. If you do not have it on your system already, install easy_install or pip using your system's package manager.
2. Install Tor using your system's package manager.
3. Use pip to install Stem and pycurl. Ensure that pip is up to date!
4. Clone this repository or otherwise copy the files to your system. Ensure that the file structure is consistent.
5. To use FastPace right away, call 'python run.py' from within the directory. You'll be prompted with a command line prompt into which you will supply a starting .onion service url.
6. All output is saved to fastpace.db. Use sqlite or another utility of your choice, if available, to view the data.

Note: As of FastPace v.0.0.2, BeautifulSoup is no longer required. Only Stem and pycurl are required, both of which are available under the LGPLv3 license through the Python package manager
