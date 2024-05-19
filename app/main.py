from service import FilmService
from config import load_config

def main():
    config = load_config()
    film_service = FilmService(config)

    if film_service.connect():
        print("Connected to MariaDB")

        while True:
            print("\nMenu :")
            print("1. Voir la liste des films")
            print("2. Ajouter un film")
            print("3. Quitter")

            choice = input("Choisissez une option (1/2/3) : ")

            if choice == '1':
                rows = film_service.get_all_films()
                if rows:
                    print("Liste des films :")
                    for row in rows:
                        print(f"ID: {row[0]}, Nom: {row[1]}, Année: {row[2]}")
                else:
                    print("Aucun film trouvé.")
            elif choice == '2':
                nom = input("Entrez le nom du film : ")
                annee = input("Entrez l'année du film : ")
                try:
                    annee = int(annee)
                    insert_id = film_service.insert_film(nom, annee)
                    if insert_id:
                        print(f"Film ajouté avec l'ID : {insert_id}")
                    else:
                        print("Erreur lors de l'ajout du film.")
                except ValueError:
                    print("Année invalide, veuillez entrer un nombre entier.")
            elif choice == '3':
                print("Déconnexion...")
                film_service.disconnect()
                print("Déconnecté de MariaDB")
                break
            else:
                print("Choix invalide, veuillez réessayer.")
    else:
        print("Failed to connect to MariaDB")

if __name__ == "__main__":
    main()
