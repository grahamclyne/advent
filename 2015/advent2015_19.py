rep = [('H','HO'),('H','OH'),('O','HH')]
start = 'CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRnCaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiBCaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArTiTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiRnTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl'
rep = """Al => ThF
Al => ThRnFAr
B => BCa
B => TiB
B => TiRnFAr
Ca => CaCa
Ca => PB
Ca => PRnFAr
Ca => SiRnFYFAr
Ca => SiRnMgAr
Ca => SiTh
F => CaF
F => PMg
F => SiAl
H => CRnAlAr
H => CRnFYFYFAr
H => CRnFYMgAr
H => CRnMgYFAr
H => HCa
H => NRnFYFAr
H => NRnMgAr
H => NTh
H => OB
H => ORnFAr
Mg => BF
Mg => TiMg
N => CRnFAr
N => HSi
O => CRnFYFAr
O => CRnMgAr
O => HP
O => NRnFAr
O => OTi
P => CaP
P => PTi
P => SiRnFAr
Si => CaSi
Th => ThCa
Ti => BP
Ti => TiTi
e => HF
e => NAl
e => OMg"""
x = rep.split('\n')
x = [y.replace(' ', '').split('=>') for y in x]


# outputs = {"",""}
# for pair in x:
#     let = pair[0]
#     replacement = pair[1]
#     for index in range(len(start)):
#         if(start[index:index+len(let)] == let):
#             print(start[index:index+len(let)], let,replacement,len(let))
#             print(start)
#             out = start[:index] + replacement + start[index+len(let):]
#             print(out)
#             outputs.add(out)
# print(len(outputs))
x = sorted(x, key=lambda tup:len(tup[1]), reverse=True)
count = 0
for j in range(100):
    for i in x:
        for index in range(len(start)):
            if(i[1] == start[index:index+len(i[1])]):
                start = start[:index] + i[0] + start[index+len(i[1]):]
                count += 1
print(count)

#193 too low, 519 too high, answer is 518

