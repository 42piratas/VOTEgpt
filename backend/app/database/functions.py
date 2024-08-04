from database.models import Country, ElectionData
from main import db

def insert_election(tipo_eleicao, data_eleicao, country_id):
    """
    Insere uma nova entrada de dados de eleição na tabela ElectionData.
    
    :param tipo_eleicao: Tipo da eleição (e.g., presidencial, estadual)
    :param data_eleicao: Data da eleição (objeto datetime.date)
    :param country_id: ID do país relacionado
    :return: O objeto ElectionData inserido ou None em caso de erro
    """
    try:
        new_election = ElectionData(tipo_eleicao=tipo_eleicao, data_eleicao=data_eleicao, country_id=country_id)
        db.session.add(new_election)
        db.session.commit()
        print(f"Election {tipo_eleicao} added successfully.")
        return new_election
    except Exception as e:
        print(f"Error adding election {tipo_eleicao}: {e}")
        db.session.rollback()
        return None
      
def get_countries():
    """
    Retorna uma lista de todos os países na tabela Country.
    
    :return: Lista de objetos Country ou None em caso de erro
    """
    try:
        countries = Country.query.all()
        return countries
    except Exception as e:
        print(f"Error getting countries: {e}")
        return None