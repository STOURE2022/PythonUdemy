import logging
import antigravity
import imoji




# Configurer le niveau de logging

#ogging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Ecrire les logs dans un fichier
logging.basicConfig(level=logging.DEBUG,
                    filename='app_1.log',
                    filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug("La fonction a bien été exécutée.")
logging.info("Ceci est un message d'information ?")
logging.warning("ceci est un message d'avertissement.")
logging.error("ceci est un message d'erreur.")
logging.critical("ceci est un message critique.")
