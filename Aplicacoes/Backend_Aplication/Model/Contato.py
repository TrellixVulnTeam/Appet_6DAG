from peewee import *
from DatabaseCon import database as db
import Usuario

class Contato(Model):
    ##ORM reconhece automaticamente como PK
    id_contato = AutoField()
    ## Enum representante do tipo de contato
    tipo = IntegerField() 
    ## Valor do contato em questao
    descricao = CharField() 
    ## FK relacional com o usuario dono de tal contato
    id_usuario = ForeignKeyField(Usuario)
    class Meta:
        database = db