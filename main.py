import os

TEXT = "SnoozeEquity is an alarm clock that apologizes for waking you, silently reschedules your first meeting, and, on the third snooze, sells your apartment and starts you a new life in Portugal."


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
