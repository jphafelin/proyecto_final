from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)


    

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

# class Evento(db.Model):
#             id = db.Column(db.Integer, primary_key=True)
#             name = db.Column(db.String(80), unique=False, nullable=False)
#             id_participante = db.Column(db.String(80), unique=False, nullable=False)
#             categoria = db.Column(db.String(80), unique=False, nullable=False)
#             fecha = db.Column(db.String(120), unique=True, nullable=False)
#             descripcion = db.Column(db.String(80), unique=False, nullable=False)
#             lugar = db.Column(db.String(80), unique=False, nullable=False)
#             dificultad = db.Column(db.String(80), unique=False, nullable=False)
            

    # def __repr__(self):
    #     return f'<Evento {self.id}>'

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "id_participante": self.participante,
    #         "categoria": self.categoria,
    #         "fecha": self.fecha,
    #         "descripcion": self.descripcion,
    #         "lugar": self.lugar,
    #         "dificultad": self.dificultad,



            # do not serialize the password, its a security breach
    #    }