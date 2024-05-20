from repository import Repository
from config import load_config

class FilmService:
    def __init__(self, config):
        self.repo = Repository(**config)

    def connect(self):
        return self.repo.connect()

    def disconnect(self):
        self.repo.disconnect()

    def insert_film(self, nom, annee):
        insert_query = "INSERT INTO film (nom, annee) VALUES (?, ?)"
        return self.repo.insert(insert_query, (nom, annee))

    def get_all_films(self):
        select_query = "SELECT * FROM film"
        return self.repo.select(select_query)

    # delete film by id
    def delete_film(self, id):
        delete_query = "DELETE FROM film WHERE id =?"
        return self.repo.delete(delete_query, (id,))

    # update film by id
    def update_film(self, id, nom, annee):
        update_query = "UPDATE film SET nom =?, annee =? WHERE id =?"
        return self.repo.update(update_query, (nom, annee, id))

    # get film by id
    def get_film(self, id):
        select_query = "SELECT * FROM film WHERE id =?"
        return self.repo.select(select_query, (id,))
