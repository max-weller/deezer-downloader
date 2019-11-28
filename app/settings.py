from credentials import sid

use_mpd = True
mpd_host = "localhost"
mpd_port = 6600

behind_reverse_proxy = False
reverse_proxy_path = "/foo"


mpd_music_dir_root = "/tmp/music"
# TODO: docs: for songs and albums
download_dir_songs = "/tmp/music/deezer/songs"
download_dir_albums = "/tmp/music/deezer/albums"
download_dir_zips = "/tmp/music/deezer/zips"
download_dir_playlists = "/tmp/music/deezer/playlists"
download_dir_youtubedl = "/tmp/music/deezer/youtube-dl"


debug_command = "journalctl -u wpa_supplicant@wlp3s0.service --output=cat -n 50"
#debug_command = "head -n 50 deezer.log"
