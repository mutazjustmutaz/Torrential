
This is an updated version of [Fredrik Lundh's bencode parser](https://web.archive.org/web/20200105114449/https://effbot.org/zone/bencode.htm). The original code is, as you'd expect, very well written. However, it's not useful for parsing .torrent files in its current form.

I upgraded the code from python 2 to python 3, and added code to handle the binary data you usually find in .torrent files.

This is the first step in the development of a bittorrent client.
