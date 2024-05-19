import configparser
import os

def load_config(filename='app/config.ini'):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Le fichier {filename} n'a pas été trouvé.")

    config = configparser.ConfigParser()
    if not config.read(filename):
        raise ValueError(f"Échec de la lecture du fichier {filename}.")

    # Vérification de l'existence de la section 'database' et des clés nécessaires
    if 'database' not in config:
        raise ValueError("La section 'database' est manquante dans le fichier de configuration.")

    required_keys = ['user', 'password', 'host', 'port', 'database']
    db_config = {}

    for key in required_keys:
        if key in config['database']:
            if key == 'port':  # Convertir le port en entier
                db_config[key] = config.getint('database', key)
            else:
                db_config[key] = config.get('database', key)
        else:
            raise ValueError(f"La clé '{key}' est manquante dans la section 'database'.")

    return db_config

try:
    config = load_config()
    print("Configuration chargée avec succès :", config)
except Exception as e:
    print("Erreur lors du chargement de la configuration :", e)
