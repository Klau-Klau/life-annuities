import pandas as pd


def sredni_zysk(x, n, op, type):
    Qx = [0] * (n + 1)

    def read_second_column(file_path):
        Q = []
        with open(file_path, 'r') as file:
            for line in file:
                columns = line.split()
                if len(columns) > 1:
                    Q.append(float(columns[1].replace(',', '.')))
        return Q + [1] * 100
    if type=="V":
        Q = read_second_column("tab_men_vill.txt")
    else:
        Q = read_second_column("tab_men_city.txt")

    Qx[1] = Q[x]
    for i in range(2, n + 1):
        Qx[i] = Qx[i - 1] + (1 - Qx[i - 1]) * Q[n - 1 + x]

    return ((1 + op) ** n) * (1 - Qx[n]) - 1


Wiek = [0,16,33,50,66]
Czas=[10,16,20,24,30]
op = 0.055


results = pd.DataFrame(index=Wiek, columns=Czas)
results2 = pd.DataFrame(index=Wiek, columns=Czas)


# Compute the results and store them in the DataFrame
def przedzialy():
    for i in Wiek:
        for j in Czas:

            sz_c = sredni_zysk(i, j, op,"C")
            sz_v = sredni_zysk(i, j, op, "V")


            if sz_c < -0.57:
                przedzial_c = "duża strata"
            elif sz_c < -0.05:
                przedzial_c = "mała strata"
            elif sz_c < 0.05:
                przedzial_c = "brak zysku"
            elif sz_c<0.5:
                przedzial_c = "mały zysk"
            elif sz_c<1.57:
                przedzial_c = "umiarkowany zysk"
            else:
                przedzial_c="wysoki zysk"

            if sz_v < -0.57:
                przedzial_v = "duża strata"
            elif sz_v < -0.05:
                przedzial_v = "mała strata"
            elif sz_v < 0.05:
                przedzial_v = "brak zysku"
            elif sz_v<0.5:
                przedzial_v = "mały zysk"
            elif sz_v < 1.57:
                przedzial_v = "umiarkowany zysk"
            else:
                przedzial_v="wysoki zysk"



            results.at[i, j] = f"{round(sz_c, 2),round(sz_v,2)}"
            results2.at[i, j] = f"{przedzial_c,przedzial_v}"



    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(results)
    print(results2)

przedzialy()

