
def register (func): 
print ('running register (%s)' 8 func) ® registry. append (func)
return func
@register def f1() :
print ('running f1()')
@register def f2 ():
pnrit ('running f2()')
def f3():
print ('running f3() ')
def main(): 8
print ('running main ()')
print ('registry -›', registry)
f1)( f2 ()
f3 ()
i f_name = = - _main_': main )(