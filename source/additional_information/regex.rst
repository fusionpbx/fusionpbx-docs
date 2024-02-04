####################
Regular Expressions
####################

* ^ Start of the string
* $ End of the string
* ? optional example 1? makes the 1 optional
* \\d{10}  10 digits
* ( and ) gets matching digits inside brackets sets a $1 and second set of brackets creates $2
* ^\\+?1?(\\d{10})$   10 to 11 digits and e164 format sets $1 to 10 digits
* [0-9]   Any number between 0 to 9
* [2-9]   Any number between 2 to 9
* \| The pipe works like an OR. Example ^101$|^102$ matches 101 or 102
* ^9(\\d{10})$ This strips off the 9 and the $1 value is the remaining 10 digits

**Dialplan Expression**

* **Two digits:** ^(\\d{2})$
* **Three digits:** ^(\\d{3})$
* **Four digits:** ^(\\d{4})$
* **FIve digits:** ^(\\d{5})$
* **Six digits:** ^(\\d{6})$
* **Seven digits(Local Calling):** ^(\\d{7})$  
* **Eight digits:** ^(\\d{8})$
* **Nine digits:** ^(\\d{9})$
* **Ten digits(Long Distance):** ^(\\d{10})$
* **Eleven digits(Long Distance with a 1):** ^\\+?(\\d{11})$
* **North America:** ^\\+?1?(\\d{10})$
* **North America International:** ^(011\\d{9,17})$
* **Caribbean:** ^(?:\+1|1)((?:684|264|268|242|246|441|284|345|767|809|829|849|473|876|664|670|787|939|869|758|784|721|868|649)\\d{7})$
* **Europe International:** ^(00\\d{9,17})$
* **International:** ^(\\d{12,20})$
* **311 Information:** ^(311)$
* **711 TTY:** ^(711)$
* **911 Emergency:** ^(911)$
* **Toll Free:** ^1?(8(00|55|66|77|88)[2-9]\\d{6})$
* **INUM:** ^0118835100\\d{8}$
* **Dial 9 then Two digits:** ^9(\\d{2})$
* **Dial 9 then Three digits:** ^9(\\d{3})$
* **Dial 9 then Four digits:** ^9(\\d{4})$
* **Dial 9 then Five digits:** ^9(\\d{5})$
* **Dial 9 then Six digits:** ^9(\\d{6})$
* **Dial 9 then Seven digits:** ^9(\\d{7})$
* **Dial 9 then Eight digits:** ^9(\\d{8})$
* **Dial 9 then Nine digits:** ^9(\\d{9})$
* **Dial 9 then Ten digits:** ^9(\\d{10})$
* **Dial 9 then Eleven digits:** ^9(\\d{11})$
* **Dial 9 then International:** ^9(\\d{12,20})$

**Links**

* https://regex101.com/
* https://regex101.com/r/QmOZiH/3/
* https://regexr.com/
* https://extendsclass.com/regex-tester.html
* https://softwium.com/regex-explainer/
