a = 20
b = 0.05
c = 25

let = 0
yield_per_hectare = a

while yield_per_hectare < c:
    yield_per_hectare *= (1 + b)
    let += 1

print(f"Урожайность достигнет {c} ц/га через {let} лет")
