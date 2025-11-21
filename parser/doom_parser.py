import subprocess
import datetime
import os

# ----------------------------------------------------
# 1) DOOM 로그 파일 위치
# ----------------------------------------------------
DOOM_LOG_PATH = "/home/jungwoo/.local/share/chocolate-doom/doom.log"

# ----------------------------------------------------
# 2) 파싱된 로그를 저장할 폴더
# ----------------------------------------------------
SAVE_DIR = "/home/jungwoo/project/logs"


def main():
    # -------------------------------------------
    # logs 폴더 생성
    # -------------------------------------------
    os.makedirs(SAVE_DIR, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    save_path = os.path.join(SAVE_DIR, f"parsed_{timestamp}.log")

    print(f"[INFO] Saving parsed events to: {save_path}")
    print("[INFO] Waiting for DOOM events...\n")

    # -------------------------------------------
    # tail -F 로 doom.log 실시간 감시
    # -------------------------------------------
    process = subprocess.Popen(
        ["tail", "-F", DOOM_LOG_PATH],   # doom.log 실시간 읽기
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    # -------------------------------------------
    # 로그 저장 파일 준비
    # -------------------------------------------
    with open(save_path, "w") as outfile:
        for line in process.stdout:
            line = line.strip()

            # 빈 줄(공백)은 무시
            if not line:
                continue

            print(line)                # 콘솔 출력
            outfile.write(line + "\n") # 파일 저장

            # -------------------------------------------
            # 이벤트 감지 (정우가 원하는 핵심 부분)
            # -------------------------------------------

            lower = line.lower()

            if "damage" in lower:
                print("\n[EVENT] Player Damaged!\n")

            if "killed" in lower or "died" in lower:
                print("\n[EVENT] Monster killed!\n")

            if "picked up" in lower:
                print("\n[EVENT] Item pickup!\n")

            if "completed" in lower:
                print("\n[EVENT] Level Completed!\n")


if __name__ == "__main__":
    main()
