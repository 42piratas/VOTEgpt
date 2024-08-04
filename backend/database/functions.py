from db_setup import db
from models import Country, ElectionData
from flask import jsonify

def get_countries():
    try:
        # Consulta todos os países da tabela
        countries = Country.query.all()
        
        # Serializa os dados para JSON
        countries_list = [
            {
                'id': country.id,
                'label': country.label,
                'code': country.code,
                'is_democracy': country.is_democracy
            } for country in countries
        ]
        
        # Retorna a lista como JSON
        return countries_list, 200
    except Exception as e:
        print(f"Error fetching countries: {e}")
        return jsonify({'error': 'An error occurred while fetching countries'}), 500

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