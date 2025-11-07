#!/usr/bin/env python3
"""
Script para popular o banco de dados com dados de teste.
Execute: python scripts/seed_data.py
"""
import sys
import os
from datetime import datetime, timedelta

# Adiciona o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db, User, FoodItem, FoodEntry
from werkzeug.security import generate_password_hash

def seed_data():
    """Popula o banco de dados com dados de teste."""
    with app.app_context():
        # Verifica se está em modo de teste
        if app.config.get('TESTING', False):
            print("⚠️  Modo de teste detectado. O seed não deve ser executado durante os testes.")
            return
        
        # Limpa o banco de dados
        print("🗑️  Limpando banco de dados...")
        db.drop_all()
        db.create_all()
        
        # Cria usuários de teste
        print("👤 Criando usuários de teste...")
        users = [
            User(
                username='testuser',
                email='test@example.com',
                daily_calorie_goal=2000
            ),
            User(
                username='aluno',
                email='aluno@uni.br',
                daily_calorie_goal=2500
            ),
            User(
                username='visitante',
                email='visitante@uni.br',
                daily_calorie_goal=1800
            )
        ]
        
        # Define senhas
        users[0].set_password('test123')
        users[1].set_password('123456')
        users[2].set_password('123456')
        
        db.session.add_all(users)
        db.session.commit()
        
        # Cria itens de comida
        print("🍎 Criando itens de comida...")
        foods = [
            FoodItem(name='Maçã', calories=52, protein=0.3, carbs=14, fat=0.2, is_public=True),
            FoodItem(name='Frango Grelhado', calories=165, protein=31, carbs=0, fat=3.6, is_public=True),
            FoodItem(name='Arroz Branco', calories=130, protein=2.7, carbs=28, fat=0.3, is_public=True),
            FoodItem(name='Feijão Preto', calories=127, protein=8.8, carbs=22.8, fat=0.5, is_public=True),
            FoodItem(name='Ovo Cozido', calories=155, protein=13, carbs=1.1, fat=11, is_public=True),
            FoodItem(name='Banana', calories=89, protein=1.1, carbs=23, fat=0.3, is_public=True),
            FoodItem(name='Pão Integral', calories=247, protein=13, carbs=41, fat=4.2, is_public=True),
            FoodItem(name='Iogurte Natural', calories=59, protein=10, carbs=3.6, fat=0.4, is_public=True),
            FoodItem(name='Salada Verde', calories=15, protein=1.2, carbs=3, fat=0.2, is_public=True),
            FoodItem(name='Peito de Peru', calories=135, protein=30, carbs=0, fat=1, is_public=True)
        ]
        
        db.session.add_all(foods)
        db.session.commit()
        
        # Cria entradas de comida para hoje
        print("📝 Criando entradas de comida...")
        today = datetime.utcnow().date()
        yesterday = today - timedelta(days=1)
        
        test_user = User.query.filter_by(username='testuser').first()
        aluno_user = User.query.filter_by(username='aluno').first()
        
        entries = [
            # Entradas de hoje para testuser
            FoodEntry(user_id=test_user.id, food_item_id=foods[0].id, quantity=2, date=today),
            FoodEntry(user_id=test_user.id, food_item_id=foods[1].id, quantity=1, date=today),
            # Entradas de ontem para testuser
            FoodEntry(user_id=test_user.id, food_item_id=foods[2].id, quantity=1, date=yesterday),
            # Entradas de hoje para aluno
            FoodEntry(user_id=aluno_user.id, food_item_id=foods[3].id, quantity=1, date=today),
            FoodEntry(user_id=aluno_user.id, food_item_id=foods[4].id, quantity=2, date=today)
        ]
        
        db.session.add_all(entries)
        db.session.commit()
        
        print("✅ Dados de teste criados com sucesso!")
        print(f"\n📊 Resumo:")
        print(f"   - Usuários: {len(users)}")
        print(f"   - Alimentos: {len(foods)}")
        print(f"   - Entradas: {len(entries)}")
        print(f"\n🔑 Credenciais de teste:")
        print(f"   - testuser / test123")
        print(f"   - aluno / 123456")
        print(f"   - visitante / 123456")

def reset_data():
    """Reseta o banco de dados (limpa e recria)."""
    with app.app_context():
        print("🔄 Resetando banco de dados...")
        db.drop_all()
        db.create_all()
        print("✅ Banco de dados resetado!")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'reset':
        reset_data()
    else:
        seed_data()

