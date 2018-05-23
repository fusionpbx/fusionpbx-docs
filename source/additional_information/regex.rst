####################
Regular Expressions
####################

* ^ Start of the string
* $ End of the string
* ? optional
* \d{10}  10 digits
* ( and ) gets matching digits inside brackets sets a $1 and second set of brackets creates $2
* ^\+?1?(\d{10})$   10 to 11 digits and e164 format sets $1 to 10 digits
**Dialplan Expression**

* **Two digits:** ^(\d{2})$
* **Three digits:** ^(\d{3})$
* **Four digits:** ^(\d{4})$
* **FIve digits:** ^(\d{5})$
* **Six digits:** ^(\d{6})$
* **Seven digits(Local Calling):** ^(\d{7})$  
* **Eight digits:** ^(\d{8})$
* **Ninee digits:** ^(\d{9})$
* **Ten digits(Long Distance):** ^(\d{10})$
* **Eleven digits(Long Distance with a 1):** ^\+?(\d{11})$
* **North America:** ^\+?1?(\d{10})$
* **North America International:** ^(011\d{9,17})$
* **Europe International:** ^(00\d{9,17})$
* **International:** ^(\d{12,20})$
* **311 Information:** ^(311)$
* **711 TTY:** ^(711)$
* **911 Emergency:** ^(911)$






