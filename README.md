# Booper

Visit the [blog post](http://gradman.com/blog/booper) to learn the inspiration for this little toy.

## Setup

- Get Raspbian installed on a Raspberry Pi.
- Clone this repository into `~/booper`
- `apt-get install rclone` and configure it to connect it to your cloud storage provider of choice (see the documentation for rclone).
  - Modify the Makefile and adjust the sync command to match the name of your rclone configuration.
- `apt-get install sqlite3` if you want to muck with the database (optional)
- Add the following line to the end of `/etc/xdg/lxsession/LXDE-pi/autostart`:

```
@lxterminal -e /usr/bin/make -C /home/pi/booper
```

This line will open a terminal that runs the python script in this repo and accept input from stdin.  Connect your booper, and have fun!
