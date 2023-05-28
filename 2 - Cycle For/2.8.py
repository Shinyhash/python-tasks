a = 20
b = 0.05
c = 25

year = 0
yieldH = a

while yieldH < c:
    yieldH *= (1 + b)
    year += 1

print(f"Урожайность достигнет {c} ц/га через {year} лет")
