'''
A mai ora anyaga az objektum orientalt programozas
Az ora soran egy amoba jatekot fogunk elkesziteni pythonban objektum orientalt
elvek betartasaval.
'''

#Eloszor hozzunk letre egy babu osztalyt, a jatekban ketto tipusu babu van
#kor es X ezek legyenek a valtozoi a babu osztalyunknak elvegre a jatekban 
#megegyezik a ketto viselkedese

#hozzunk letre egy transponalo fv.-t

def transpon(X):
    result = []
    for i in range(len(X)):
        result.append([None] * len(X[0]))
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[j][i] = X[i][j]
    return result

class Babu:
    #az osztalyunkon belul ay innit metoduson belul hozhatjuk letre az osztaly konstruktorat
    def __init__(self, jatekos):
        self.jatekos = jatekos
    #hozzunk letre egy methodot, ami ellenorzi, hogy megteheto e a kivant lepes
    #egyreszt ellenoriznunk kell, hogy lehet e oda lepni masreszt pedig,
    #hogy a lepes egyaltalan a tablan van e
    def lepes(self, tabla, lepes):
        sor, oszlop = lepes
        #ellenorizni kell hogy a kapott szam az ertelmezett tartomanyon belul van e
        if ((0 <= sor < 3) and (0 <= oszlop < 3)):
            if tabla[sor][oszlop] is None:
                return True
        return False

class AmobaJatek:
    #hozzuk letre a konstruktorat az osztalynak
    def __init__(self):
        self.jelenlegi_jatekos = "O"
        self.tabla = self.tabla_letrehoz()
        self.jatek_vege_bool = False
    #irjuk meg a methodust, ami letrehozza a tablat
    def tabla_letrehoz(self):
        tabla = []
        for i in range(3):
            #hozzuk letre a sorokat
            sor = [None] * 3
            #hozzuk letre a tablat
            tabla.append(sor)
        return tabla
    
    #hozzuk letre a sajat kiirato metodusunkat
    def print_board(self):
        print('   A B C')
        print('--------------')
        ssz = 1
        for sor in self.tabla: #eloszor vegigmegyunk soronkent
            #ures mezoket feltoltjuk - jellel a babukat a megszokott szimbolummal jeloljuk    
            print(str(ssz), end=" ") # sor ele oda irjuk a megfelelo sorszamot
            ssz += 1 #sorszamot megfeleloen noveljuk
            for babu in sor: #vegigmegyunk oszloponkent
                if babu is None:
                    print("--", end=" ")
                else:
                    print(babu.jatekos, end=" ") #kiirjuk minden babunak  a jelet megfeleloen
            print()
        print('----------------')
    
    #huzzuk letre a metodosunkat a lepesek feldolgozasra nevezzuk lepes()-nek (ez egy polimorfizmus 
    #hisz mar a babu osztalyunknak is volt egz lepes metodusa)   
    def lepes(self):
        #huzzunk letre egy szotarat, ami a megfelelo betukhoz szamokat rendel
        alphabet = {"A": 0, "B": 1, 'C': 2}
        #kerjunk be egy lepest (pl.:"1 A")
        lepes_r = input('Adja meg a kovetkezo lepest: ')
        lepes = [int(lepes_r[0]) - 1, alphabet.get(lepes_r[2])]
        if self.jelenlegi_jatekos == "O":
            print("Ez O kore!")
        else:
            print('Ez X kore!')
        
        if Babu(self.jelenlegi_jatekos).lepes(self.tabla, lepes):
            self.tabla[lepes[0]][lepes[1]] = Babu(self.jelenlegi_jatekos)
            return True
        else:
            print("Hibas lepes!")
            return False
    
    #hozzunk letre egy methodust a jatekosok valtasara
    def jatekos_valtas(self):
        if self.jelenlegi_jatekos == "O":
            self.jelenlegi_jatekos = "X"
        else:
            self.jelenlegi_jatekos = "O"
    
    #irjunk egy metodust ami ellenorzi hogy vege van e a jateknak
    #sor ellenorzes
    def sor_ell(self, tabla):
        for row in tabla:
            if all(cell and cell.jatekos == self.jelenlegi_jatekos for cell in row):
                return True
        else:
            return False
    
    #atlok ellenorzese
    def atlo_ell(self):
        if self.tabla[0][0] and self.tabla[1][1] and self.tabla[2][2]:
            if all(self.tabla[i][i].jatekos == self.jelenlegi_jatekos for i in range(3)):
                return True
        if self.tabla[0][2] and self.tabla[1][1] and self.tabla[2][0]:
            if all(self.tabla[i][2 - i].jatekos == self.jelenlegi_jatekos for i in range(3)):
                return True
        else:
            return False
    
    #oszlopok ellenorzese
    def oszlop_ell(self):
        tabla = transpon(self.tabla)
        return self.sor_ell(tabla)
    
    def jatek_vege(self):
        return (self.oszlop_ell() or self.sor_ell(self.tabla) or self.atlo_ell())
    
    #irjuk meg a metodust, ami vegrehajtja az eddigi osszes metodusunkat
    def jatek(self):
        while not self.jatek_vege_bool:
            self.print_board()
            if self.lepes():
                if self.jatek_vege():
                    self.print_board()
                    print(f"A {self.jelenlegi_jatekos} nyerte a jatekot!")
                    self.jatek_vege_bool = True
                else:
                    self.jatekos_valtas()

jatek = AmobaJatek()
jatek.jatek()
