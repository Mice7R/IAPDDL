import random
import sys

if len(sys.argv) < 3:
    print "%s nlibros nlibrosleer [Probabilidad de cadena; default:50]" % sys.argv[0]
    exit(0)

nlibros = int(sys.argv[1])
nlibrosleer = int(sys.argv[2])
if len(sys.argv) == 4:
    P = int(sys.argv[3])
else: P = 50

libros = []
#nlibros = input("numoro de libros:")
#P = input("probabilidad de cadena: 0 <= x <= 100 (ej 50)")
#nlibrosleer = input("numero de libros a leer:")

def dositer(LIST):
    a = iter(LIST)
    b = iter(LIST)

    next(b)
    for c in b:
        yield (a.next(),c)

p=[]
for i in range(0,P):
    p.append(1)
for i in range(P,100):
    p.append(False)

for i in range(0,nlibros):
    libros.append("L%d" % i)

print "(define (problem test-01) (:domain planificador) (:objects %s - libro) (:init " % (" ".join(libros))
i=0
for (a,b) in dositer(libros):
    c = random.choice(p)
    if c: 
        if i == 10:
            print "\n",
            i=0
        print "(predecesor %s %s)" % (a,b),
    else: i=10

print "\n",
for i in range(0, nlibrosleer):
    a = random.choice(libros)
    libros.remove(a)
    print "(leer %s)" % a,
    if i % 10 == 9:
        print "\n",

print ")\n(:goal (forall (?x - libro) (not (leer ?x)))))"
