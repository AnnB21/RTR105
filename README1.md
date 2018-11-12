ē# RTR105
## Datormācības kursa elektroniskā klāde
 
***
*Ctrl+Shift+T* - jauns logs  
*Ctrl+Alt+T* - iestartet terminalu  
*U+Tab2x* - paradit visas terminala iespejas 
*Ctrl+L* - notirit ekranu  
*Ctrl+Alt+F1* - uz visu ekranu  
*Ctrl+Alt+F7* - iziet no visa ekrana  
*Q* - atgriezties pe **man** izmantošanas  
*uname* - komanda (print system information)  
*man* - nosaukums, apraksts 
*uname -burts* - atrast komandu pec pirma burta  
*echo $0* - display a line of text  
*sh* - shell valoda (nedraudziga valoda)  
*bash* - shell valoda (draudziga valoda)  
*whoami* - kas es esmu (print effective userid)  
*who* - show who is logged on  
*pwd* - kur es atrodos attiecība pret failu sistemu (print name of current/working directory)   
*ls* -  atvert mapes (list directory contents) 
*ls -l* -  apskatit mapes (use a long listing format)   
*ls -a* - apskatit visus objektus, kas sakas ar punktu  
*ls -la* - detalizets apraksts visiem objektiem  
*history* - paskatities vesturi   
*ls -ls* - parskatit mapes, tas vardu, kad bija instaleti vai modificeti  
*history > nosaukums.txt* - saglabat kada konkreta mapē  
*cd (pilnas adreses nosaukums)* - parvietoties kadā konkretā mapē  
. - tekoša direktorija (solis uz vietas)  
.. - saknes apgabals  
*cd* ~ - relativa adrese (tilde)  
*cd /* -absoluta adrese (iziet uz home)  
*mkdir* -uztaisit mapi  
*rmdir* - nodzest mapi  
*rm -r ManaMape/* -nodzest mapi  
*echo* - attelot tekstu   
**Piemērs:   
echo "Teksts"  
Teksts**  
*echo -e* **nosukums/nnosaukums** - jauna linija  
**Piemērs:   
echo -e "Teksts/nTeksts/nTeksts"   
Teksts  
Teksts  
Teksts**  
*>* - saglabat kaut kada mapē    
*cat nosaukums.txt  
more nosaukums.txt  
less nosaukums.txt* -apskatit failu  
*>>* - papildinat failu  
**Piemērs:  
  echo "Teksts" . fails1.txt  
  cat fails1.txt  
Teksts  
  echo "papild teksts" >> fails1.txt  
  cat gails1.txt  
Teksts 
papild tekst**   
*nano nosaukums.txt* - papildinat failu   
*chmod* - mainit tiesibas   
*Ctrl+X* - saglabat izmaiņas  
*cp (vards, kuru kopejam)(vards kopetam(jaunam) failam)* - kopēt  
*mv *1*.*txt Music/* - parcelt ko? kur?  
*../* - limenis augstāk  
*ls mapes_nosaukums/* - apskatit mapes saturu  
*nano mans_skripts.sh* - izveidot jaunu skriptu  
*#!/bin/bash* - norada ar kādu valodu talāk rakstisim  
*echo $PATH* - svarigas adreses, ceļi  
*PATH=$PATH:*~  
*or  
PATH=$PATH:/home/user* - add directory to $PATH    
*git clone https://github.com/AnnB21/RTR105* - clone a repositary into a new directory  


































