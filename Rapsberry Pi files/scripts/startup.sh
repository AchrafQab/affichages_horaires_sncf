#!/bin/bash

connecte=0;
image=0;
while [ $connecte -ne 1 ]; do
        ping -c 3 hsncf.g-ny.org
        if [ $? -eq  0 ]; then  # ping OK
                pkill feh ;     # Tuer le viewer d'image (sans vérifier s'il est actif)
                connecte=1 ;    # Sortie du while 
        else    # pas de connexion
                # Afficher l'image (si elle ne l'est pas déjà, d'où la variable image)
                if [ $image -ne 1 ]; then
                        image=1 ;
                        feh -Z -F ~/images/noconnection.jpg &
                fi
                sleep 5 ;	# pause de 5 secondes
        fi
done
pkill feh # on tue feh, des fois qu'il serait encore là

# Lancer Chromium ou Kweb en mode kiosque
#chromium --noerrdialogs --kiosk http://hsncf.g-ny.org/depart.php &
kweb -CZJK http://hsncf.g-ny.org/depart.php &

