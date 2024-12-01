from pathlib import Path

txt = (Path(__file__).parent / "inputs" / "day01.txt").read_text()

print(sum(abs(int(b) - int(a)) for a, b in zip(*map(sorted, zip(*map(str.split, txt.splitlines()))))))
