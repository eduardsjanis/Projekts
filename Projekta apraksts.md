PROJEKTA APRAKSTS

Projekts ir par tīkla informācijas nolasīšanu un saglabāšanu

Projekta uzdevumi:
Projekta galvenais uzdevums ir iegūt man svarīgo informāciju automatizēti bez manas iejaukšanās kad piemēram esmu aizņemts un nevaru apskatīt man vajadzīgās lietas.
Un lai programma saglabā man svarīgākās lietas kuras man interesē excel failā kuru pēc tam es varu jebkurā laikā apskatīt kad vēlos,
kā arī lai prgoramma man paziņo ka ir bijuši jaunumi man parsvarā izmantotākajā programma kuru sauc "discord".
Koda galvenais uzdevums ir no "ss.lv" tīmekļa man pazioņot par portatīvajiem datoriem kuri ir cenā no 300 - 700 Eur jo tas piemēram ir mans budžets.
Bet tākā man galvenais faktors ir cena nevis modelis programma atlasa jaunākos sludinājumus kuri ienāk no ss.lv un atcerās vecos tapēc es redzu tikai jaunumus.
Projektā tika izmantots webhook kas ir "discord" aplikācijas links uz botu kurš var sūtīt ziņas serverī.



Projektā es izmantoju bibliotēkas kā:

reuqests
requests vai kā to sauc latviski pieprasījumu bibliotēka tiek izmantota, lai nosūtītu HTTP pieprasījumus uz noteiktu URL. 
Konkrēti, to izmanto, lai veiktu GET pieprasījumu uz URL 'https://www.ss.lv/lv/electronics/computers/noutbooks/sell/'. 
Šis URL atbilst tīmekļa lapai, kurā tiek parādīta informācija par pārdošanā esošajiem klēpjdatoriem.
Noteiktajā rindā manā kodā ir requests.get(links) Šī rinda nosūta GET pieprasījumu uz norādīto URL un atbilde tiek saglabāta mainīgajā
Atbildē parasti ir ietvertas tīmekļa lapas HTML saturs kas pēc tam tiek parsēts izmantojot nākošo bibliotēku kura ir BeatifulSoup lai iegūtu informāciju.
Pieprasijuma bibliotēka parasti tiek izmantota API kopēšanā lai iegūtu datus no URL manā gadijumā tā ir lapas HTML satura ienešana ko vēlāl parše beatifulsoup.

Beatifulsoup
Šī bibliotēka tika izmantota priekš tīmekļa parsēšanas vai tajā sauktajā "skrāpēšanā" izmantoju šo bibliotēku jo tā ir vislabākā un vieglākā priekš parsēšanas.
Kodā table = soup.find('table', attrs={'align': 'center'})Šajā rindā tiek atrasts pirmais HTML <table> elements ar atribūta līdzinājumu, kas iestatīts uz "centru".
Nākamais kods atkārtojas šīs tabulas rindās un kolonnās, lai iegūtu informāciju par klēpjdatoriem, piemēram, modeli un cenu.
Īsi sakot man BeatifulSoup palīdz analizēt un pārvietoties HTML saturā atvieglojot konkrētu nepieciešamo datu iegūšanu no tīmekļa lapas.

Json
Šis koda bloks ir atbildīgs par redzēto produktu klēpjdatoru kopas saglabāšanu JSON failā ar nosaukumu “seen_products.json”. Funkcijai json.dump ir divi argumenti:
serializējamie dati kas manā gadijumā ir saraksts, kas izveidots no kopas seen_products, un faila objekts, kurā tiks ierakstīti JSON dati.

Time
kodā laika bibliotēka tiek izmantota, lai skripta izpildē ieliktu pauzi.
Konkrēti, to izmanto, lai liktu skriptam pagaidīt vai gulēt noteiktu laiku pirms nākamās"loop"izpildes.
time.sleep(300) manā kodā pauze ir uzlikta uz 5 minūtēm.

openpyxl
openpyxl bibliotēka kodā Openpyxl bibliotēka tiek izmantota darbam ar Excel failiem (XLSX formātā).
Šī bibliotēka ļauj izveidot, modificēt un iegūt datus no Excel izklājlapām.
Konkrēts kods ir paredzēts jaunas Excel darbgrāmatas izveidei, datu pievienošanai un saglabāšanai.

Programmas izmantošanas metodes:
Programma ir izmantojama vienkārši ir jāpalaiž programma un tas sāks savu darbu, ja būs jaunumi par noteiktajiem laptopiem(cena)
tad kods man paziņos aplikācijā "discord" un saglabās informāciju par jaunumiem excel failā
Kods ir parasts un viegls toties ļoti parocīgs :).
