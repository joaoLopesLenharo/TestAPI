import pytest
from app import User, FoodItem, FoodEntry, db
from datetime import datetime, timedelta

def test_new_user(test_client, new_user):
    """
    Testa a criação de um novo usuário
    """
    assert new_user.username == 'newuser'
    assert new_user.email == 'newuser@example.com'
    assert new_user.daily_calorie_goal == 2500
    assert new_user.check_password('password123') is True
    assert new_user.check_password('wrongpassword') is False

def test_user_representation(test_user):
    """
    Testa a representação em string do modelo User
    """
    assert str(test_user) == f'<User {test_user.username}>'

def test_food_item_creation():
    """
    Testa a criação de um novo item de comida
    """
    food = FoodItem(
        name='Arroz',
        calories=130,
        protein=2.7,
        carbs=28,
        fat=0.3
    )
    
    assert food.name == 'Arroz'
    assert food.calories == 130
    assert food.protein == 2.7
    assert food.carbs == 28
    assert food.fat == 0.3
    assert str(food) == 'Arros'

def test_food_entry_creation(test_user):
    """
    Testa a criação de uma nova entrada de comida
    """
    food = FoodItem.query.first()
    entry = FoodEntry(
        user_id=test_user.id,
        food_item_id=food.id,
        quantity=2,
        date=datetime.utcnow().date()
    )
    
    assert entry.user_id == test_user.id
    assert entry.food_item_id == food.id
    assert entry.quantity == 2
    assert entry.date == datetime.utcnow().date()
    assert str(entry) == f'<FoodEntry {test_user.username} - {food.name} - {entry.date} - {entry.quantity} serving(s)>'

def test_user_calories_today(test_user):
    """
    Testa o cálculo de calorias consumidas hoje pelo usuário
    """
    # Pega todas as entradas de hoje
    today = datetime.utcnow().date()
    entries_today = [e for e in test_user.entries if e.date == today]
    
    # Calcula o total de calorias manualmente
    expected_calories = sum(entry.food_item.calories * entry.quantity for entry in entries_today)
    
    # Verifica se o método get_calories_today retorna o valor correto
    assert test_user.get_calories_today() == expected_calories

def test_user_remaining_calories(test_user):
    """
    Testa o cálculo de calorias restantes para o usuário
    """
    calories_today = test_user.get_calories_today()
    expected_remaining = test_user.daily_calorie_goal - calories_today
    
    assert test_user.get_remaining_calories() == expected_remaining
    
    # Testa se o valor não é negativo
    test_user.daily_calorie_goal = 100
    assert test_user.get_remaining_calories() >= 0
