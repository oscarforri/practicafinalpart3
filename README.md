# practicafinalpart3
practicafinalpart3

Aquest és un programa que serveix per controlar un concurs de beure cervesa.

Primer de tot es crea la base de dades amb el arxiu sqlalchemy_declarative.py, que contindrà dues taules per tal de guardar la informació de cadascun dels usuaris i els diferents 'kegs'. Aquesta base de dades es diu sqlalchemy_database.db.

Un cop creada la base de dades, per tal de saber la quantitat de cervesa que es serveix i a qui es serveix s'utilitza el arxiu MFRC522.py i readtag.py. Aquest dos arxius no són creats per nosaltres sinó que els utilitzarem en el arxiu client.py.

Aquest arxiu client, per tal de executar-lo s'ha de entrar dos parametres: client i 'kegid'
El client.py el que fa és estar connectat amb la raspberry i, per tant, també connectat amb el lector de NFC i el 'flow meter'. El client.py actua quan li arriba una senyal de que s'està utilitzant el 'flow meter'. Quan això succeeix, agafa la lectura del lector de NFC i la quantitat de cervesa que li correspon i l'envia, juntament amb el kegid, al server.py.

Això és possible perquè previament s'ha creat un socket zmq entre el server.py i el client.py.

Un cop la informació ha arribat al server.py, aquest programa introdueix aquests resultats a la base de dades i d'aquesta manera s'actualitzen les dades.

 Després el altres arxiu important és el webapp.py. Aquest serveix per tal de poder visualitzar a traves de internet les dades de la base de dades on hi ha els resultats del concurs.
 També permet mitjançant una webapp o un webservice afegir usuaris, actualitzar dades manualment o esborrar usuaris.
 Per tant, el webapp.py té les funcions necessaries per tal de fer un CRUD tant amb webapp com amb el webservice (JSON).

Per tal de realitzar els CRUD amb el webservice s'ha de utilitzar una eina externa que ens permeti executar els POST, PUT, GET i DELETE.

Si al buscador web e fica la adreça IP de la raspberry + /ws/uses el programa farà un GET de tots el Usuaris. En canvi si a més a més afegim a la agreça IP /ws/users/<username> podem triar si fer un GET, PUT o DELETE.

 Després també hi ha la carpeta de templates on hi ha els diferents codis .html per tal de que es pugui visualitzar be els diferents paràmetres per webapp.
