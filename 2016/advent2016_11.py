import time
import sys

if __name__ == '__main__':
    start = time.time()
    floor_plan = [
        [{'PRO':['GEN','CHIP']},{'COB':[]},{'CUR':[]},{'PLU':[]},{'RUT':[]}],  
        [{'COB':['GEN']},{'CUR':['GEN']},{'RUT':['GEN']},{'PLU':['GEN']}, {'PRO':[]}],
        [{'COB':['CHIP']},{'CUR':['CHIP']},{'RUT':['CHIP']},{'PLU':['CHIP']},{'PRO':[]}],
        [{'PRO':[]},{'COB':[]},{'CUR':[]},{'PLU':[]},{'RUT':[]}]
    ]
    print(floor_plan)
    for i in floor_plan:
        floor = i 
            
    print('runtime: %f seconds' % (time.time() - start))