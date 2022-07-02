%%% Križić kružić igra protiv kompjutera %%%

% predikati koji označavaju pobjedu
pobjeda(Igra, Igrac) :- redak_pobjeda(Igra, Igrac).
pobjeda(Igra, Igrac) :- stupac_pobjeda(Igra, Igrac).
pobjeda(Igra, Igrac) :- dijagonala_pobjeda(Igra, Igrac).

redak_pobjeda(Igra, Igrac) :- Igra = [Igrac, Igrac, Igrac, _, _, _, _, _, _].
redak_pobjeda(Igra, Igrac) :- Igra = [_, _, _, Igrac, Igrac, Igrac, _, _, _].
redak_pobjeda(Igra, Igrac) :- Igra = [_, _, _, _, _, _, Igrac, Igrac, Igrac].

stupac_pobjeda(Igra, Igrac) :- Igra = [Igrac, _, _, Igrac, _, _, Igrac,_ , _].
stupac_pobjeda(Igra, Igrac) :- Igra = [_, Igrac, _, _, Igrac, _, _, Igrac, _].
stupac_pobjeda(Igra, Igrac) :- Igra = [_, _, Igrac, _, _, Igrac, _, _, Igrac].

dijagonala_pobjeda(Igra, Igrac) :- Igra = [Igrac, _, _, _, Igrac, _, _, _, Igrac].
dijagonala_pobjeda(Igra, Igrac) :- Igra = [_, _, Igrac, _, Igrac, _, Igrac, _, _].

%predikati za označavanje polja
oznaci([b,B,C,D,E,F,G,H,I], Igrac, [Igrac,B,C,D,E,F,G,H,I]).
oznaci([A,b,C,D,E,F,G,H,I], Igrac, [A,Igrac,C,D,E,F,G,H,I]).
oznaci([A,B,b,D,E,F,G,H,I], Igrac, [A,B,Igrac,D,E,F,G,H,I]).
oznaci([A,B,C,b,E,F,G,H,I], Igrac, [A,B,C,Igrac,E,F,G,H,I]).
oznaci([A,B,C,D,b,F,G,H,I], Igrac, [A,B,C,D,Igrac,F,G,H,I]).
oznaci([A,B,C,D,E,b,G,H,I], Igrac, [A,B,C,D,E,Igrac,G,H,I]).
oznaci([A,B,C,D,E,F,b,H,I], Igrac, [A,B,C,D,E,F,Igrac,H,I]).
oznaci([A,B,C,D,E,F,G,b,I], Igrac, [A,B,C,D,E,F,G,Igrac,I]).
oznaci([A,B,C,D,E,F,G,H,b], Igrac, [A,B,C,D,E,F,G,H,Igrac]).

% ispis igre
ispis([A, B, C, D, E, F, G, H, I]) :- write([A, B, C]), nl, write([D, E, F]), nl, write([G, H, I]), nl.

%predikati za generiranje odgovora kompjutera
x_moze_pobjediti(Igra) :- oznaci(Igra, x, NovaIgra), pobjeda(NovaIgra, x).

% predikati za igranje kompjutera
potez_kompa(Igra, NovaIgra) :- oznaci(Igra, o, NovaIgra), pobjeda(NovaIgra, o), !.
potez_kompa(Igra, NovaIgra) :- oznaci(Igra, o, NovaIgra), not(x_moze_pobjediti(NovaIgra)).
potez_kompa(Igra, NovaIgra) :- oznaci(Igra, o, NovaIgra).
%potez_kompa(Igra, NovaIgra) :- not(member(b, Igra)), !, write('Izjednaceno!'), nl, NovaIgra = Igra, igraj.

% prevedi brojeve koje igrač unosi u transformacije u igri
potez([b,B,C,D,E,F,G,H,I], 1, [x,B,C,D,E,F,G,H,I]).
potez([A,b,C,D,E,F,G,H,I], 2, [A,x,C,D,E,F,G,H,I]).
potez([A,B,b,D,E,F,G,H,I], 3, [A,B,x,D,E,F,G,H,I]).
potez([A,B,C,b,E,F,G,H,I], 4, [A,B,C,x,E,F,G,H,I]).
potez([A,B,C,D,b,F,G,H,I], 5, [A,B,C,D,x,F,G,H,I]).
potez([A,B,C,D,E,b,G,H,I], 6, [A,B,C,D,E,x,G,H,I]).
potez([A,B,C,D,E,F,b,H,I], 7, [A,B,C,D,E,F,x,H,I]).
potez([A,B,C,D,E,F,G,b,I], 8, [A,B,C,D,E,F,G,x,I]).
potez([A,B,C,D,E,F,G,H,b], 9, [A,B,C,D,E,F,G,H,x]).
potez(Igra, _N, Igra) :- write('Polje je vec popunjeno ili ste unijeli nepostojecu poziciju!'), nl.
potez(Igra, _N, NovaIgra) :- not(member(b, Igra)), !, write('Izjednaceno!'), nl, NovaIgra = Igra, igraj.

% pokretanje igre
igraj :- uvod, pokreniigru([b, b, b, b, b, b, b, b, b]).

uvod :- write('Dobrodosli u igru krizic kruzic protiv racunala'), nl, write('Vi ste x i potrebno je unijeti broj pozicije na koju zelite postaviti svoj x.'), nl, 
	ispis([1, 2, 3, 4, 5, 6, 7, 8, 9]).

pokreniigru(Igra) :- pobjeda(Igra, x), write('x je pobjednik!'), nl.
pokreniigru(Igra) :- pobjeda(Igra, o), write('o je pobjednik!'), nl.
pokreniigru(Igra) :- read(N), nl, potez(Igra, N, NovaIgra), ispis(NovaIgra), nl, 
			(
				pobjeda(NovaIgra, x) ->
				write('x je pobjednik!'), nl;
				write('Kompjuter je na redu:'), nl, potez_kompa(NovaIgra, NajnovijaIgra), ispis(NajnovijaIgra), nl, pokreniigru(NajnovijaIgra)
			), nl.
