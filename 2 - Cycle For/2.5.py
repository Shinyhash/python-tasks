import math

Q = 150 # м3/час
V = 10000 # л
C0 = 10 # г/л
C = 0.1 # г/л

T = -V/Q * math.log(C/C0)

print("Концентрация хлорной извести достигнет безопасной величины через", round(T, 2), "часов")
