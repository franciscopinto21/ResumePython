from app import create_app, db
from app.models import Skill  # Certifique-se de que você está importando o modelo correto

def testar_conexao():
    """Testa a conexão com o banco de dados."""
    app = create_app()
    with app.app_context():
        try:
            # Testa a conexão com o banco de dados
            with db.engine.connect() as connection:
                print("Conexão com o banco de dados bem-sucedida!")
        except Exception as e:
            print(f"Erro ao conectar no banco de dados: {e}")

def testar_consulta():
    """Testa uma consulta simples ao banco de dados."""
    app = create_app()
    with app.app_context():
        try:
            # Tenta consultar a tabela 'Skill'
            resultados = Skill.query.all()
            print(f"Dados encontrados: {resultados}")
        except Exception as e:
            print(f"Erro ao consultar o banco de dados: {e}")

if __name__ == "__main__":
    opcao = input("Escolha uma opção:\n1: Testar conexão\n2: Testar consulta\nDigite o número da opção: ")
    
    if opcao == '1':
        testar_conexao()
    elif opcao == '2':
        testar_consulta()
    else:
        print("Opção inválida.")
