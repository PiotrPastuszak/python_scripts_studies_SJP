zad 1
"^[ao]" szukamy liter a lub o na poczatku stringa
".*[ęóąśłżźćń][.,?]?$" szukamy dowolnych znaków po ktorych moze wystąpić znak interpunkcyjny i musi wystąpić koniec stringa
".*[.]$" szukamy dowolnych znaków po których musi wystąpić kropka i koniec stringa
"[ ][ ]\S+" szukamy dwóch spacji i jednego lub więcej symboli niebiałych
"^[^eyuioaęóą\s]*[eyuioaęóą][^eyuioaęóą\s]*[eyuioaęóą][^eyuioaęóą\s]*[eyuioaęóą][^eyuioaęóą\s]*$" szukamy na zmianę dowolnej ilości spółgłosek i jednej samogłoski 3 razy dokładnie pomiędzy początkiem i końcem stringa
zad 2
plik podawany jako wartość argumentu -i
