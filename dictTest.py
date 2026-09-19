dict = {"wlh":{"bm":"kjb","工资":3000,"级别":1},
        "sss":{"bm":"kjb","工资":4000,"级别":1},
        "www":{"bm":"kjb","工资":5000,"级别":3},
        "qqq":{"bm":"kjb","工资":6000,"级别":2},}
# print(dict)
for i in dict:
    if dict[i]["级别"] == 1:
        dict[i]["工资"] = dict[i]["工资"]+1000

print(dict)