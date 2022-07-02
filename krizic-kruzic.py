import kivy
kivy.require('2.1.0')

from kivy.lang import Builder
from kivymd.app import MDApp
from pyswip import Prolog

#Postavljanje potrebnog za komunikaciju s Prologom
prolog = Prolog()
prolog.consult("krizic-kruzic.pl")

class GlavnaApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.theme_primary_palette = "BlueGray"
		return Builder.load_file('krizic-kruzic.kv')

	#Definiranje tko kreće prvi
	na_potezu = "X"

	#Vođenje racuna o pobjedniku
	pobjednik = False

	#Vođenje rezutata
	rezultatX = 0
	rezultatO = 0


	#Funkcija za kraj igre
	def kraj_igre(self, a, b, c):
		self.pobjednik = True
		a.color = "red"
		b.color = "red"
		c.color = "red"

		#onemogućiti klikanje na gumbe
		self.onesposobi_sve_gumbe()

		#postavi labelu za pobjednika
		self.root.ids.rezultat.text = f"{a.text} pobjeđuje!"

		#praćenje trenutnog rezultata
		if a.text == 'X':
			self.rezultatX = self.rezultatX + 1
			self.root.ids.rezultat_za_X.text = str(self.rezultatX)
		if a.text == 'O':
			self.rezultatO = self.rezultatO + 1
			self.root.ids.rezultat_za_O.text = str(self.rezultatO)



	#Funkcija ako nema pobjednika
	def nema_pobjednika(self):
		if self.pobjednik == False and \
		self.root.ids.btn1.disabled == True and \
		self.root.ids.btn2.disabled == True and \
		self.root.ids.btn3.disabled == True and \
		self.root.ids.btn4.disabled == True and \
		self.root.ids.btn5.disabled == True and \
		self.root.ids.btn6.disabled == True and \
		self.root.ids.btn7.disabled == True and \
		self.root.ids.btn8.disabled == True and \
		self.root.ids.btn9.disabled == True:
			self.root.ids.rezultat.text = "Izjednačeno!"



	#Funkcija za onemogućavanje klikanja svih gumba nakon pobjede
	def onesposobi_sve_gumbe(self):
		self.root.ids.btn1.disabled = True
		self.root.ids.btn2.disabled = True
		self.root.ids.btn3.disabled = True
		self.root.ids.btn4.disabled = True
		self.root.ids.btn5.disabled = True
		self.root.ids.btn6.disabled = True
		self.root.ids.btn7.disabled = True
		self.root.ids.btn8.disabled = True
		self.root.ids.btn9.disabled = True



	#Funkcija za omogućavanje klikanja svih gumba
	def omoguci_klikanje_svih_gumba(self):
		self.root.ids.btn1.disabled = False
		self.root.ids.btn2.disabled = False
		self.root.ids.btn3.disabled = False
		self.root.ids.btn4.disabled = False
		self.root.ids.btn5.disabled = False
		self.root.ids.btn6.disabled = False
		self.root.ids.btn7.disabled = False
		self.root.ids.btn8.disabled = False
		self.root.ids.btn9.disabled = False



	#Funkcija za vraćanje jednake boje gumbima
	def vrati_boju(self):
		self.root.ids.btn1.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn2.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn3.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn4.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn5.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn6.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn7.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn8.background_color = (1.72, 1.74, 1.73, 1)
		self.root.ids.btn9.background_color = (1.72, 1.74, 1.73, 1)



	#Funkcija za micanje teksta s gumba
	def makni_tekst(self):
		self.root.ids.btn1.text = ""
		self.root.ids.btn2.text = ""
		self.root.ids.btn3.text = ""
		self.root.ids.btn4.text = ""
		self.root.ids.btn5.text = ""
		self.root.ids.btn6.text = ""
		self.root.ids.btn7.text = ""
		self.root.ids.btn8.text = ""
		self.root.ids.btn9.text = ""



	#Funkcija za postavljanje boje (rješenje problema da nekad ne oboja u crveno nakon pobjede)
	def oboji_gumbe(self):
		self.root.ids.btn1.color = "blue"
		self.root.ids.btn2.color = "blue"
		self.root.ids.btn3.color = "blue"
		self.root.ids.btn4.color = "blue"
		self.root.ids.btn5.color = "blue"
		self.root.ids.btn6.color = "blue"
		self.root.ids.btn7.color = "blue"
		self.root.ids.btn8.color = "blue"
		self.root.ids.btn9.color = "blue"



	#Funkcija za spremanje trenutnog stanja igre
	def spremi_najnovije_stanje_igre(self):

		stanje_za_vracanje = ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
		#Gumb 1
		if self.root.ids.btn1.text != "":
			stanje_za_vracanje[0] = self.root.ids.btn1.text.lower()
		
		#Gumb 2
		if self.root.ids.btn2.text != "":
			stanje_za_vracanje[1] = self.root.ids.btn2.text.lower()

		#Gumb 3
		if self.root.ids.btn3.text != "":
			stanje_za_vracanje[2] = self.root.ids.btn3.text.lower()

		#Gumb 4
		if self.root.ids.btn4.text != "":
			stanje_za_vracanje[3] = self.root.ids.btn4.text.lower()

		#Gumb 5
		if self.root.ids.btn5.text != "":
			stanje_za_vracanje[4] = self.root.ids.btn5.text.lower()

		#Gumb 6
		if self.root.ids.btn6.text != "":
			stanje_za_vracanje[5] = self.root.ids.btn6.text.lower()

		#Gumb 7
		if self.root.ids.btn7.text != "":
			stanje_za_vracanje[6] = self.root.ids.btn7.text.lower()

		#Gumb 8
		if self.root.ids.btn8.text != "":
			stanje_za_vracanje[7] = self.root.ids.btn8.text.lower()

		#Gumb 9
		if self.root.ids.btn9.text != "":
			stanje_za_vracanje[8] = self.root.ids.btn9.text.lower()

		#Vratit najnovije stanje igre
		return stanje_za_vracanje



	#Funkcija za određivanje poteza kojeg je komp odigra iz odgovora koji dobijemo od prologa
	def odredi_potez_kompa(self, odgovor_prologa, stanje):

		komp_odigrao_vratiti = 0

		for i in range(9):
		#Komp je odigrao polje i + 1
			if str(odgovor_prologa[0]['NovaIgra'][i]) != stanje[i]:
				if str(odgovor_prologa[0]['NovaIgra'][i]) == 'o':
					komp_odigrao_vratiti = i + 1
 
		return komp_odigrao_vratiti



	#Funkcija za bojanje polja koje igra komp, tj. O
	def oboji_zeljeno(self, komp_odigrao):
		
		if komp_odigrao == 1:
			self.root.ids.btn1.background_color = "yellow"

		if komp_odigrao == 2:
			self.root.ids.btn2.background_color = "yellow"

		if komp_odigrao == 3:
			self.root.ids.btn3.background_color = "yellow"

		if komp_odigrao == 4:
			self.root.ids.btn4.background_color = "yellow"

		if komp_odigrao == 5:
			self.root.ids.btn5.background_color = "yellow"

		if komp_odigrao == 6:
			self.root.ids.btn6.background_color = "yellow"

		if komp_odigrao == 7:
			self.root.ids.btn7.background_color = "yellow"

		if komp_odigrao == 8:
			self.root.ids.btn8.background_color = "yellow"

		if komp_odigrao == 9:
			self.root.ids.btn9.background_color = "yellow"



	#Funkcija za provjeru da li je ploča puna
	def provjera_pune_ploce(self, stanje):
		brojac = 0

		for i in range(9):
			if stanje[i] == 'b':
				brojac = brojac + 1

		return brojac



	#Funkcija da se odigra potez koji komp želi
	def odigraj_kompovo(self, btn):
		btn.text = "O"
		btn.disabled = True
		self.root.ids.rezultat.text = "X - križić je na redu!"
		self.na_potezu = "X"

		#pročitaj najnovije stanje na ploči
		stanje_komp = self.spremi_najnovije_stanje_igre()

		#Provjera da li je netko pobjedio --> pozivanje Prologa
		self.pobjeda_prolog(stanje_komp, 'o')



	#Funkcija za određivanje gumba kojeg treba odigrati za komp
	def komp_igra(self, komp_odigrao):
		if komp_odigrao == 1:
			self.odigraj_kompovo(self.root.ids.btn1)

		if komp_odigrao == 2:
			self.odigraj_kompovo(self.root.ids.btn2)

		if komp_odigrao == 3:
			self.odigraj_kompovo(self.root.ids.btn3)

		if komp_odigrao == 4:
			self.odigraj_kompovo(self.root.ids.btn4)

		if komp_odigrao == 5:
			self.odigraj_kompovo(self.root.ids.btn5)

		if komp_odigrao == 6:
			self.odigraj_kompovo(self.root.ids.btn6)

		if komp_odigrao == 7:
			self.odigraj_kompovo(self.root.ids.btn7)

		if komp_odigrao == 8:
			self.odigraj_kompovo(self.root.ids.btn8)

		if komp_odigrao == 9:
			self.odigraj_kompovo(self.root.ids.btn9)



	#Funkcija za provjeru da li je došlo do pobjede --> provjera se u Prologu
	def pobjeda_prolog(self, stanje, igrac):
		#pozivanje prologa da provjerimo da li je došlo do pobjede
		odgovor_prologa = bool(list(prolog.query("pobjeda(%s, %s)" %(stanje, igrac))))

		if odgovor_prologa == True:
			#određivanje gumba koji se šalju funkciji kraj_igre da oboja pobjedu
			#redak
			if stanje[0] != 'b' and stanje[0] == stanje[1] and stanje[1] == stanje[2]:
				self.kraj_igre(self.root.ids.btn1, self.root.ids.btn2, self.root.ids.btn3)

			if stanje[3] != 'b' and stanje[3] == stanje[4] and stanje[4] == stanje[5]:
				self.kraj_igre(self.root.ids.btn4, self.root.ids.btn5, self.root.ids.btn6)

			if stanje[6] != 'b' and stanje[6] == stanje[7] and stanje[7] == stanje[8]:
				self.kraj_igre(self.root.ids.btn7, self.root.ids.btn8, self.root.ids.btn9)

			#stupac
			if stanje[0] != 'b' and stanje[0] == stanje[3] and stanje[3] == stanje[6]:
				self.kraj_igre(self.root.ids.btn1, self.root.ids.btn4, self.root.ids.btn7)

			if stanje[1] != 'b' and stanje[1] == stanje[4] and stanje[4] == stanje[7]:
				self.kraj_igre(self.root.ids.btn2, self.root.ids.btn5, self.root.ids.btn8)

			if stanje[2] != 'b' and stanje[2] == stanje[5] and stanje[5] == stanje[8]:
				self.kraj_igre(self.root.ids.btn3, self.root.ids.btn6, self.root.ids.btn9)

			#dijagonala
			if stanje[0] != 'b' and stanje[0] == stanje[4] and stanje[4] == stanje[8]:
				self.kraj_igre(self.root.ids.btn1, self.root.ids.btn5, self.root.ids.btn9)

			if stanje[2] != 'b' and stanje[2] == stanje[4] and stanje[4] == stanje[6]:
				self.kraj_igre(self.root.ids.btn3, self.root.ids.btn5, self.root.ids.btn7)

		#ako nema pobjednika, a sva polja su puna
		self.nema_pobjednika()



	#Funkcija koja implementira pritisak igrača, tj. potez igrača X
	def pritisak(self, btn):

		if self.na_potezu == 'X':
			btn.text = "X"
			btn.disabled = True
			self.root.ids.rezultat.text = "O - kružić je na redu!"
			self.na_potezu = "O"

			#Priprema za potez kompa da nam da do znanja koje polje želi odigrati
			stanje = self.spremi_najnovije_stanje_igre()

			#Provjera da li je netko pobjedio --> pozivanje Prologa
			self.pobjeda_prolog(stanje, 'x')

			#Provjeri da li je ploca puna
			puna = self.provjera_pune_ploce(stanje)

			if puna != 0 and self.root.ids.rezultat.text == 'O - kružić je na redu!':
				#pozivanje prologa da komp odluči za svoj potez 
				odgovor_prologa = list(prolog.query("potez_kompa(%s, NovaIgra)" %stanje))
				#spremi stanje koje mi je vratio prolog, uključen potez kompa
				komp_odigrao = self.odredi_potez_kompa(odgovor_prologa, stanje)
				self.oboji_zeljeno(komp_odigrao)
				self.komp_igra(komp_odigrao)



	#Funkcija koja implementira resetiranje igraće ploče nakon klika na gumb Resetiraj igru!
	def restart(self):
		#Postavi tko opet kreće prvi
		self.na_potezu = "X"
		self.root.ids.rezultat.text = "X je prvi na redu!"

		#Ponovno omogući klikanje gumba
		self.omoguci_klikanje_svih_gumba()


		#Makni tekst s gumba
		self.makni_tekst()

		#Oboji gumbe nakon pobjede (rješenje problema s bojama)
		self.oboji_gumbe()

		#Vrati jednaku boju svim gumbima
		self.vrati_boju()

		#Resetiranje varijable pobjednik
		self.pobjednik = False



GlavnaApp().run()
		