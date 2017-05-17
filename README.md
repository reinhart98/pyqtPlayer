# pyqtPlayer
-for Qtmultimedia package lost from pyqt5 you can install :
  1. python3-pyqt5.qtmultimedia
  2. libqt5multimedia-plugins

-for gstreamer error you can install :
  * apt-get install libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev gstreamer-tools gstreamer0.10-plugins-good gstreamer0.10-plugins-bad

-for mpeg problem you can install :
  * apt-get install gstreamer0.10-ffmpeg

note : if for some reason you cant instal the ffmpeg you can do the following :
  1. add this line in /etc/apt/sources.list
      deb http://www.deb-multimedia.org jessie main non-free
  2. apt-get update
  3. then you will need key of this repo :
      apt-get install deb-multimedia-keyring
  4. apt-get-update
  5. apt-get install gstreamer0.10-ffmpeg
