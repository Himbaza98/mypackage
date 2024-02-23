from mypackage import myModule
"""
make sure it works well
"""
assert myModule.top_n([9,7,5,2,1],3) == [9,7,5],'incorrect'
assert myModule.top_n([12,4,0,3],2) == [12,4],'incorrect'
assert myModule.top_n([1,2,3,4,5,70],6) == [70,5,4,3,2,1],'incorrect'