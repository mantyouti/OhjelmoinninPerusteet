
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:

    muutettu_varaus = []
    muutettu_varaus.append(int(varaus[0]))
    muutettu_varaus.append(str(varaus[1]))
    muutettu_varaus.append(str(varaus[2]))
    muutettu_varaus.append(str(varaus[3]))
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())
    muutettu_varaus.append(int(varaus[6]))    
    muutettu_varaus.append(float(varaus[7]))
    muutettu_varaus.append(varaus[8] == "True")
    muutettu_varaus.append(str(varaus[9]))
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))
    return muutettu_varaus

def hae_varaukset(varaustiedosto: str) -> list:

    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

    print()

def vahvistetut_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if (varaus[8]):
            print(f"- {varaus[1]}, {varaus[9]}, {varaus[4].strftime('%d.%m.%Y')}, klo {varaus[5].strftime('%H:%M')}")
   
    print()

def pitkat_varaukset(varaukset: list):
    for varaus in varaukset[1:]:
        if (varaus[6] >= 3):
            print(f"- {varaus[1]}, {varaus[4].strftime('%d.%m.%Y')}, klo {varaus[5].strftime('%H:%M')}, kesto {varaus[6]} h, {varaus[9]}")
     
    print()

def varausten_vahvistusstatus(varaukset: list):
    for varaus in varaukset[1:]:
        if (varaus[8]): 
            print(f"- {varaus[1]} -> Vahvistettu")
        else:
            print(f"- {varaus[1]} -> EI Vahvistettu")
    
    print()

def varausten_lkm(varaukset: list):
    vahvistetut_varaukset_2 = 0
    ei_vahvistetut_varaukset_2 = 0

    for varaus in varaukset[1:]:
        if (varaus[8]):
            vahvistetut_varaukset_2 += 1
        else:
            ei_vahvistetut_varaukset_2 += 1
    print(f"- Vahvistettuja varauksia: {vahvistetut_varaukset_2} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut_varaukset_2} kpl")

    print()

def varausten_lkm(varaukset: list):
    vahvistetut_varaukset_2 = 0
    ei_vahvistetut_varaukset_2 = 0

    for varaus in varaukset[1:]:
        if (varaus[8]):
            vahvistetut_varaukset_2 += 1
        else:
            ei_vahvistetut_varaukset_2 += 1
    print(f"- Vahvistettuja varauksia: {vahvistetut_varaukset_2} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut_varaukset_2} kpl")

    print()

def vahvistetut_tulot(varaukset: list):
    kokonaistulot = 0.0
    for varaus in varaukset[1:]:
        if (varaus[8]):
            kokonaistulot += varaus[6] * varaus[7]
    muokattu_kokonaistulot = str(round(kokonaistulot, 2)).replace(".", ",")
    print(f"- Vahvistettujen varausten kokonaistulot: {muokattu_kokonaistulot} €")
    
    print()

def main():

    varaukset = hae_varaukset("varaukset.txt")
    print()
    print ("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print(("2) Pitkät varaukset (≥ 3 h)"))
    pitkat_varaukset(varaukset)
    print(("3) Varausten vahvistusstatus"))
    varausten_vahvistusstatus(varaukset)
    print(("4) Yhteenveto vahvistuksista"))
    varausten_lkm(varaukset)
    print(("5) Vahvistettujen varausten kokonaistulot"))
    vahvistetut_tulot(varaukset)


if __name__ == "__main__":
    main()