def main():
    varaukset = "varaukset.txt"
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip().split("\n")
        print(varaus)

if __name__ == "__main__":
    main()