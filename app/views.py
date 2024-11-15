from flask import render_template, Blueprint
from .models import Profile, Certification, Education, Language, Skill, WorkExperience, Projects

# Criando o Blueprint
main_bp = Blueprint('main', __name__)

# Dados de exemplo
portfolio_items = [
    {"name": "BIG GREEN COFFEE & CO", "description": "Import Export Business", "link": "https://biggreentrading.com/", "tech": "Laravel, MySQL", "image":"biggreen.png"},
    {"name": "Farm2u", "description": "NATURAL FOOD", "link": "https://farm2u.com.br/", "tech": "Laravel, MySQL", "image":"farm2u.png"},
    {"name": "AlpinClub Trading", "description": "Export Business", "link": "https://alpinclubtrading.com.br/", "tech": "Laravel, MySQL", "image":"alpinclub.png"},
    {"name": "A Rede de Imóveis", "description": "Real Estate Business", "link": "https://arededeimoveis.com.br/", "tech": "Laravel, MySQL", "image":"arede.png"},
]

# Rotas dentro do Blueprint
@main_bp.route('/')
def home():
    projects = Projects.query.all()
    return render_template('home.html', portfolio_items=portfolio_items, projects=projects)

@main_bp.route('/resume')
def resume():
    # Supondo que você tenha um modelo 'Profile' e outros dados armazenados no banco de dados
    profile = Profile.query.first()  # Ajuste conforme a sua lógica de obtenção dos dados
    certifications = Certification.query.all()
    education = Education.query.all()
    languages = Language.query.all()
    skills = Skill.query.all()
    work_experience = WorkExperience.query.all()

    # Passando os dados para o template
    return render_template(
        'resume.html',
        profile=profile,
        certifications=certifications,
        education=education,
        languages=languages,
        skills=skills,
        work_experience=work_experience
    )

@main_bp.route('/projects')
def projects():
    return render_template('projects.html')
