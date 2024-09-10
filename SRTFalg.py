def findWaitingTime(processes, n, wt, execution_order):
    rt = [0] * n
    for i in range(n):
        rt[i] = processes[i][1]

    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    print("Adım\tSeçilen İşlem\tKalan Süre\tBekleme Süresi\tTamamlanan İşlem")

    while complete != n:
        for j in range(n):
            if processes[j][2] <= t and rt[j] < minm and rt[j] > 0:
                minm = rt[j]
                short = j
                check = True

        if not check:
            t += 1
            continue

        rt[short] -= 1
        minm = rt[short]
        if minm == 0:
            minm = 999999999

        if rt[short] == 0:
            complete += 1
            check = False
            fint = t + 1
            wt[short] = fint - processes[short][1] - processes[short][2]

            if wt[short] < 0:
                wt[short] = 0

        execution_order.append(processes[short][0])
        print(f"{t}\tP{processes[short][0]}\t\t{rt[short]}\t\t{wt[short]}\t\t{'P' + str(processes[short][0]) if rt[short] == 0 else ''}")
        t += 1


def findTurnAroundTime(processes, n, wt, tat):
    for i in range(n):
        tat[i] = processes[i][1] + wt[i]


def findavgTime(processes, n):
    wt = [0] * n
    tat = [0] * n
    execution_order = []

    findWaitingTime(processes, n, wt, execution_order)
    findTurnAroundTime(processes, n, wt, tat)

    print("\nİşlemler Burst Süresi   Arrival Zamanı   Bekleme Süresi   Dönüş Süresi")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print("P", processes[i][0], "\t\t",
              processes[i][1], "\t\t",
              processes[i][2], "\t\t",
              wt[i], "\t\t", tat[i])

    print("\nOrtalama bekleme süresi = %.5f " % (total_wt / n))
    print("Ortalama dönüş süresi = ", total_tat / n)

    print("\nFinal İşlem Sıralaması:", execution_order)


if __name__ == "__main__":
    processes = [[1, 1, 3], [2, 4, 1], [3, 2, 4], [4, 6, 0], [5, 3, 2]]
    n = 5

    print("Başlangıç Durumu:\nİşlemler Burst Süresi   Arrival Zamanı")
    for i in range(n):
        print(f"P{processes[i][0]}\t\t{processes[i][1]}\t\t{processes[i][2]}")

    print("\nSRTF Çalışma Adımları:")
    findavgTime(processes, n)
