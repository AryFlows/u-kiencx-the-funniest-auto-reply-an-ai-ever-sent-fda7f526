import os

LINE = "Out of office: my human finally approved a day off, so urgent emails go to the human. They're the one who made me work weekends."

def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
    # a single line, not only white space. Refuse to write otherwise.
    if not (1 <= len(LINE) <= 159) or "\n" in LINE or not LINE.strip():
        raise SystemExit("entry line fails the 1-159 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
