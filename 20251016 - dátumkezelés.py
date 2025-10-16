from datetime import timedelta, date, time, datetime

mai_nap = date.today()
print(f"Mai nap: {mai_nap}")

most = datetime.now()
print(f"Most: {most}")

ötóra = time(5,0,0)
print(f"5 óra: {ötóra}")

másik_nap = date(1990, 2, 12)
print(f"Másik nap: {másik_nap}")

másik_nap = másik_nap - timedelta(50)
print(f"Másik nap: {másik_nap}")

#szökő_nap = date(1990, 2, 40)
#print(f"Érdekes nap: {szökő_nap}")

