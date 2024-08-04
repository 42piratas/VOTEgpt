from main import db
from datetime import datetime

class Country(db.Model):
    __tablename__ = 'countries'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String, nullable=False)
    code = db.Column(db.String(2), nullable=False, unique=True)
    is_democracy = db.Column(db.Boolean, default=False)

class ElectionData(db.Model):
    __tablename__ = 'elections_data'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_eleicao = db.Column(db.String, nullable=False)
    data_eleicao = db.Column(db.Date, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    country = db.relationship('Country', back_populates='elections')

class Candidate(db.Model):
    __tablename__ = 'candidates'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    known_as = db.Column(db.String)
    born = db.Column(db.String)
    nationality = db.Column(db.String)
    religion = db.Column(db.String, default='unknown')
    education = db.Column(db.String, default='unknown')
    bio = db.Column(db.String(420))
    current_party = db.Column(db.String)
    previous_parties = db.Column(db.String)
    platform = db.Column(db.String)
    keywords = db.Column(db.String)
    political_experience = db.Column(db.String)
    notorious_for = db.Column(db.String)
    endorsements = db.Column(db.String)
    funding_sources = db.Column(db.String)
    criminal_records = db.Column(db.String)
    abortion = db.Column(db.String)
    health_care = db.Column(db.String)
    economy = db.Column(db.String)
    immigration = db.Column(db.String)
    gun_control = db.Column(db.String(140))
    gun_control_short = db.Column(db.String(20))
    climate_change = db.Column(db.String)
    education = db.Column(db.String)
    taxes = db.Column(db.String)
    lgbtq_rights = db.Column(db.String(140))
    lgbtq_rights_short = db.Column(db.String(20))
    foreign_policy = db.Column(db.String)
    drug_policy = db.Column(db.String)
    criminal_justice_reform = db.Column(db.String)
    military_spending = db.Column(db.String)
    voting_rights = db.Column(db.String)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
