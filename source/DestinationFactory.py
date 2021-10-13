import destination
import Pointers



NorthPole = destination.Destination(660, 50, "North Pole")

AnnArbor = destination.Destination(275, 305, "Ann Arbor, Michigan")
Vancouver = destination.Destination(145, 250, "Vancouver, Canada")
Logan = destination.Destination(130, 325, "Logan, Utah")
Villa = destination.Destination(190, 425, "Villahermosa, Mexico")

Bogota = destination.Destination(295, 495, "Bogota, Columbia")
Rio = destination.Destination(430, 630, "Rio de Janeiro, Brazil")
Asuncion = destination.Destination(360, 645, "Asuncion, Paraguay")
Lima = destination.Destination(266, 595, "Lima, Peru")

Finland = destination.Destination(725, 205, "Helsinki, Finland")
Rome = destination.Destination(692, 305, "Rome, Italy")
Malaga = destination.Destination(605, 320, "Malaga Spain")
London = destination.Destination(625, 250, "London, England")
Iceland = destination.Destination(560, 180, "Reykjavik, Iceland")

Cairo = destination.Destination(760, 375, "Cairo, Egypt")
Mombasa = destination.Destination(825, 515, "Mombasa, Kenya")
Abidjan = destination.Destination(605, 490, "Abidjan, Cote d'Ivoire")
CapeTown = destination.Destination(725, 697, "Cape Town, South Africa")
Madagascar = destination.Destination(845, 640, "Antananarvio, Madagascar")

Moscow = destination.Destination(800, 225, "Moscow, Russia")
Astana = destination.Destination(920, 275, "Astana, Kazakhstan")
India = destination.Destination(995, 455, "Bangalore, India")
China = destination.Destination(1090, 370, "Xian, China")
Tokyo = destination.Destination(1260, 330, "Tokyo, Japan")
Manila = destination.Destination(1215, 456, "Manila, Philippines")
Sydney = destination.Destination(1310, 710, "Sydney, Australia")
Hawaii = destination.Destination(1390, 415, "Honolulu, Hawaii")

NorthPole.addPointers(Pointers.Pointer(AnnArbor, 3), Pointers.Pointer(Finland, 1), Pointers.Pointer(Moscow, 2))

AnnArbor.addPointers(Pointers.Pointer(NorthPole, 3), Pointers.Pointer(Vancouver, 2), Pointers.Pointer(Villa, 4),
                     Pointers.Pointer(Abidjan, 5))

Vancouver.addPointers(Pointers.Pointer(AnnArbor, 2), Pointers.Pointer(Logan, 1))

Logan.addPointers(Pointers.Pointer(Vancouver, 1), Pointers.Pointer(Villa, 2))

Villa.addPointers(Pointers.Pointer(Logan, 2), Pointers.Pointer(AnnArbor, 4), Pointers.Pointer(Bogota, 2))

Bogota.addPointers(Pointers.Pointer(Villa, 2), Pointers.Pointer(Rio, 2))

Rio.addPointers(Pointers.Pointer(Asuncion, 1), Pointers.Pointer(Lima, 2), Pointers.Pointer(CapeTown, 4),Pointers.Pointer(Bogota, 2))

Lima.addPointers(Pointers.Pointer(Rio, 2), Pointers.Pointer(Hawaii, 6))

Asuncion.addPointers(Pointers.Pointer(Rio, 1))

Finland.addPointers(Pointers.Pointer(NorthPole, 1), Pointers.Pointer(Rome, 2))

Rome.addPointers(Pointers.Pointer(Finland, 2), Pointers.Pointer(Malaga, 1), Pointers.Pointer(Cairo, 2))

Malaga.addPointers(Pointers.Pointer(Rome, 1), Pointers.Pointer(London, 2), Pointers.Pointer(Abidjan, 3))

London.addPointers(Pointers.Pointer(Malaga, 2), Pointers.Pointer(Iceland, 1))

Iceland.addPointers(Pointers.Pointer(London, 1))

Cairo.addPointers(Pointers.Pointer(Rome, 2), Pointers.Pointer(Mombasa, 3), Pointers.Pointer(Astana, 5))

Mombasa.addPointers(Pointers.Pointer(Cairo, 3), Pointers.Pointer(Madagascar, 2), Pointers.Pointer(Abidjan, 2),
                    Pointers.Pointer(CapeTown, 2))

Abidjan.addPointers(Pointers.Pointer(Malaga, 3), Pointers.Pointer(AnnArbor, 5), Pointers.Pointer(Mombasa, 2))

Madagascar.addPointers(Pointers.Pointer(Mombasa, 2))

CapeTown.addPointers(Pointers.Pointer(Mombasa, 2), Pointers.Pointer(Rio, 4), Pointers.Pointer(Sydney, 5))

Moscow.addPointers(Pointers.Pointer(NorthPole, 2), Pointers.Pointer(Astana, 2))

Astana.addPointers(Pointers.Pointer(Moscow, 2), Pointers.Pointer(Cairo, 5), Pointers.Pointer(India, 3),
                   Pointers.Pointer(China, 2))

India.addPointers(Pointers.Pointer(Astana, 3))

China.addPointers(Pointers.Pointer(Astana, 2), Pointers.Pointer(Tokyo, 2), Pointers.Pointer(Manila, 1))

Tokyo.addPointers(Pointers.Pointer(China, 2))

Manila.addPointers(Pointers.Pointer(China, 1), Pointers.Pointer(Hawaii, 2), Pointers.Pointer(Sydney, 2))

Hawaii.addPointers(Pointers.Pointer(Manila, 2), Pointers.Pointer(Lima, 6))

Sydney.addPointers(Pointers.Pointer(Manila, 2), Pointers.Pointer(CapeTown, 5))



