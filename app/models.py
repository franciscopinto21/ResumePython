# models.py

from . import db  # Importa a instância de db do __init__.py

class Profile(db.Model):
    __tablename__ = 'Profile'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    title = db.Column(db.String(100))
    description = db.Column(db.Text)

class Certification(db.Model):
    __tablename__ = 'Certifications'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    provider = db.Column(db.String(100))
    completion_date = db.Column(db.Date)

class Education(db.Model):
    __tablename__ = 'Education'
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(100))
    degree = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.String(500))

class Language(db.Model):
    __tablename__ = 'Languages'
    id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(50))
    proficiency = db.Column(db.String(50))

class Skill(db.Model):
    __tablename__ = 'Skills'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    skill_name = db.Column(db.String(100))

class WorkExperience(db.Model):
    __tablename__ = 'WorkExperience'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    company = db.Column(db.String(100))
    location = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    description = db.Column(db.String(500))

class Projects(db.Model):
    __tablename__ = 'Projects'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    description = db.Column(db.String(800))
    link = db.Column(db.String(300))
    tech = db.Column(db.String(300))
    image = db.Column(db.String(300))