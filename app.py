from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FloatField, validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///calories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Handler para retornar JSON em APIs quando não autenticado
@login_manager.unauthorized_handler
def unauthorized_handler():
    # Se a requisição é para uma API, retorna JSON 401
    if request.path.startswith('/api/'):
        return jsonify({'error': 'Authentication required'}), 401
    # Caso contrário, redireciona para login (comportamento padrão)
    return redirect(url_for('login'))

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    daily_calorie_goal = db.Column(db.Integer, default=2000)
    entries = db.relationship('FoodEntry', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_calories_today(self):
        today = datetime.utcnow().date()
        entries = FoodEntry.query.filter_by(user_id=self.id, date=today).all()
        return sum(entry.food_item.calories * entry.quantity for entry in entries)
    
    def get_remaining_calories(self):
        return max(0, self.daily_calorie_goal - self.get_calories_today())
    
    def __repr__(self):
        return f'<User {self.username}>'

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Float, default=0)
    carbs = db.Column(db.Float, default=0)
    fat = db.Column(db.Float, default=0)
    is_public = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    def __repr__(self):
        return f'<FoodItem {self.name}>'

class FoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    food_item_id = db.Column(db.Integer, db.ForeignKey('food_item.id'), nullable=False)
    quantity = db.Column(db.Float, default=1.0)
    food_item = db.relationship('FoodItem')
    
    def __repr__(self):
        return f'<FoodEntry {self.user.username} - {self.food_item.name} - {self.date} - {self.quantity} serving(s)>'

# Initialize database
with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

# Routes
# Forms
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Passwords must match')
    ])
    confirm_password = PasswordField('Confirm Password')
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not check_password_hash(user.password_hash, form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    today = datetime.utcnow().date()
    entries = FoodEntry.query.filter_by(user_id=current_user.id, date=today).all()
    
    # Calcula totais nutricionais
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fat = 0
    
    for entry in entries:
        total_calories += entry.food_item.calories * entry.quantity
        total_protein += entry.food_item.protein * entry.quantity
        total_carbs += entry.food_item.carbs * entry.quantity
        total_fat += entry.food_item.fat * entry.quantity
    
    return render_template('dashboard.html', 
                         entries=entries, 
                         total_calories=round(total_calories, 1),
                         total_protein=round(total_protein, 1),
                         total_carbs=round(total_carbs, 1),
                         total_fat=round(total_fat, 1))

# API Routes
@app.route('/api/food', methods=['GET', 'POST'])
@login_required
def api_food():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validação de campos obrigatórios
        if 'name' not in data or 'calories' not in data:
            return jsonify({'error': 'Name and calories are required'}), 400
        
        try:
            food = FoodItem(
                name=data['name'],
                calories=data['calories'],
                protein=data.get('protein', 0),
                carbs=data.get('carbs', 0),
                fat=data.get('fat', 0),
                is_public=data.get('is_public', True),
                user_id=current_user.id
            )
            db.session.add(food)
            db.session.commit()
            return jsonify({'message': 'Food item added', 'id': food.id}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    
    # GET - Listar alimentos
    foods = FoodItem.query.filter(
        (FoodItem.is_public == True) | (FoodItem.user_id == current_user.id)
    ).all()
    return jsonify([{
        'id': f.id,
        'name': f.name,
        'calories': f.calories,
        'protein': f.protein,
        'carbs': f.carbs,
        'fat': f.fat
    } for f in foods])

@app.route('/api/entry', methods=['POST'])
@login_required
def add_entry():
    data = request.get_json()
    
    # Validação de dados
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Verifica se food_item_id foi fornecido
    if 'food_item_id' not in data:
        return jsonify({'error': 'food_item_id is required'}), 400
    
    food_item_id = data['food_item_id']
    quantity = data.get('quantity', 1.0)
    
    # Validação de quantidade
    if quantity <= 0:
        return jsonify({'error': 'Quantity must be greater than 0'}), 400
    
    # Verifica se o food_item existe
    food_item = db.session.get(FoodItem, food_item_id)
    if not food_item:
        return jsonify({'error': 'Food item not found'}), 404
    
    # Verifica se o usuário tem acesso ao food_item (é público ou é do usuário)
    if not food_item.is_public and food_item.user_id != current_user.id:
        return jsonify({'error': 'Food item not accessible'}), 403
    
    try:
        entry = FoodEntry(
            user_id=current_user.id,
            food_item_id=food_item_id,
            quantity=quantity,
            date=datetime.utcnow().date()
        )
        db.session.add(entry)
        db.session.commit()
        return jsonify({'message': 'Entry added', 'id': entry.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
