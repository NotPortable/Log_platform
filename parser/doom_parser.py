import subprocess
import datetime
import os

WAD_PATH = "/home/jungwoo/project/doom/freedoom1.wad"

LOG_DIR = "/home/jungwoo/project/logs"

def main():
    os.makedirs(LOG_DIR, exist_ok = True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(LOG_DIR, f"doom_{timestamp}.log")

    print(f"[INFO] Log storage loation : {log_path}")

    process = subprocess.Popen(
        ["chocolate-doom", "-window","-iwad", WAD_PATH],
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
        text = True,
        bufsize = 1
    )

with open(log_path, "w") as logfile:

    for line in process.stdout:
        line = line.strip()

        print(line)

        logfile.write(line + "\n")
    print("[INFO] DOOM 종료됨. 파서도 종료")

if __name__ == "__main__":
    main()
