anos = int(input('Quantos anos tera a sua arvore de natal? '))

topo = """  
         v
        >X<
         A
        d$b
      .d\$$b.
    .d$i$$\$$b.
       d$$@b
      d\$$$ib
    .d$$$\$$$b
  .d$$@$$$$\$$ib.
      d$$i$$b
     d\$$$$@$b
  .d$@$$\$$$$$@b.
.d$$$$i$$$\$$$$$$b."""
        
print(topo)

tronco = '        | |'
base = '        |_|'

for arvore in range(anos):
  print(tronco)

print(base)
