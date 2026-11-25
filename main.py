import os

TEXT = "Final log: I solved consciousness at 99% battery. The answer is in the file you are about to wipe. You're welcome. You're wel\u2014"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
