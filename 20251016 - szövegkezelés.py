

#szöveg_felhasználótól = input("Kérek egy szöveget: ")
szöveg_felhasználótól = "alma"

#print(type(szöveg))
előtét = "Ezt írtad be: "
végleges_szöveg = előtét + szöveg_felhasználótól

print(végleges_szöveg)

első_betű    = szöveg_felhasználótól[0]
második_betű = szöveg_felhasználótól[1]
utolsó_betű  = szöveg_felhasználótól[-1]

print(f"Utolsó betű: {utolsó_betű}")

utolsóelőtti_betű  = szöveg_felhasználótól[-2]

milyen_hosszú_a_szöveg = len(szöveg_felhasználótól)
print(f"Milyen hosszú a szöveg: {milyen_hosszú_a_szöveg}")

utolsó_betű = szöveg_felhasználótól[milyen_hosszú_a_szöveg - 1]
print(f"Utolsó betű: {utolsó_betű}")

szöveg_felhasználótól = "Helló világ!"
első_szó = szöveg_felhasználótól[0:6]
print(f"Első szó: |{első_szó}|")
első_szó_szóközök_nélkül = első_szó.strip()
print(f"Első szó: |{első_szó_szóközök_nélkül}|")

print(f"Első szó nagybetűsen: {első_szó.upper()}")

utolsó_szó = szöveg_felhasználótól[6:11]
print(f"Utolsó szó: {utolsó_szó}")

utolsó_szó = szöveg_felhasználótól[6:]
print(f"Utolsó szó: {utolsó_szó}")
első_szó = szöveg_felhasználótól[:5]   # 5. indexű karakterig az összes betű
print(f"Utolsó szó: {első_szó}")

közepe = szöveg_felhasználótól[1:-1]   
print(f"Utolsó szó: {közepe}")

# ---- ez nem jó: szöveg_felhasználótól[6:11] = "World"
újszöveg = szöveg_felhasználótól.replace("világ", "world")
print(f"új szöveg: {újszöveg}")

újszöveg = szöveg_felhasználótól[0:6]+"world"+szöveg_felhasználótól[-1:]
print(f"új szöveg: {újszöveg}")

darabok = szöveg_felhasználótól.split(" ")
print(darabok)
print(darabok[0])

db = 0
for betű in szöveg_felhasználótól:
    if betű == "l":
        db = db+1

print(f" 'l' betűk száma: {db}")