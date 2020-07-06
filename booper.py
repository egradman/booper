import sys
import glob
import sqlite3
import random
import subprocess

silence_code = "009800895007"
conn = sqlite3.connect('data.db')

player_process = None

while True:
  subprocess.call(["/usr/bin/make", "sync"])
  files = glob.glob("audio/*")
  code = sys.stdin.readline()
  code = code.strip()

  c = conn.cursor()
  c.execute('SELECT * FROM codes WHERE code=?', (code,))

  res = c.fetchone()
  if res is None:
    filename = random.choice(files)
    c.execute('INSERT INTO codes VALUES (?, ?)', (code, filename))
    print("creating", code, filename)
    conn.commit()
  else:
    filename = res[1]
    print("fetched", code, filename)


  subprocess.call(["/usr/bin/pkill", "omxplayer"])

  if code != silence_code:
    player_process = subprocess.Popen(["/usr/bin/omxplayer","-o","local",filename], stdin=subprocess.PIPE, stdout=subprocess.DEVNULL)

