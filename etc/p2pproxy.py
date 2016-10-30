'''
P2pProxy plugin configuration file

What is this plugin for?
 It repeats the behavior of p2pproxy to support programs written for using p2pproxy

 Some of examples for what you can use this plugin:
    Comfort TV widget (++ version)
    Official TorrentTV widget for Smart TV
    Kodi (XBMC) p2pproxy pvr plugin
    etc...

!!! It requires some changes in aceconfig.py:
    set the httpport to 8081
    set the vlcoutport to some other port (8082 for example)
'''
__author__ = 'miltador'

# Insert your email on torrent-tv.ru here
email = 'XXXXXXXXXXXXXXXXXXXXXX'

# Insert your torrent-tv account password
password = 'XXXXX'

# Session timeout
sessiontimeout = 1800

# Generate logo with full path (e.g. http://torrent-tv.ru/uploads/ornzQpk6WCW6xk0lyBhlwqH8u2QyU7.png)
# or put only the logo file name (e.g. ornzQpk6WCW6xk0lyBhlwqH8u2QyU7.png)
# This option is only for m3u playlists.
fullpathlogo = True

# TV Guide URL
tvgurl = 'http://api.torrent-tv.ru/ttv.xmltv.xml.gz'

# Shift the TV Guide time to the specified number of hours
tvgshift = 0

# Format of the tvg-id tag or empty string
tvgid='ttv%(id)s'

# Zone id - MSK, SPB, SAM, etc.
# For more details see http://api.torrent-tv.ru/v3/api_v3.html#toc-35-
zoneid=None
