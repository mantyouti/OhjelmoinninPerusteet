import sys
from pathlib import Path

#!/usr/bin/env python3
# tulosta_sana_v1.py
# Yksinkertainen ohjelma joka lukee tiedoston ja tulostaa sen sisältämän sanan.


def read_word(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8").strip()
    except FileNotFoundError:
        print(f"Virhe: tiedostoa '{path}' ei löydy.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Virhe tiedoston lukemisessa: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    # Voit antaa tiedostopolun komentoriviparametrina, oletus "sana.txt"
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sana.txt")
    sana = read_word(path)
    print(sana)

if __name__ == "__main__":
    main()