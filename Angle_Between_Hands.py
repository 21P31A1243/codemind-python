x = input()
xs = x.split(":")
ho = int(xs[0])
mi = int(xs[1])
mint = (mi*6.0)
hour = (((ho+mi/60)/12.0)*360)%360
res = min(abs(mint-hour),360-(abs(mint-hour)))
print(res)