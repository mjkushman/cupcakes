"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

from forms import AddCupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secretsauce"

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['TESTING'] = True

connect_db(app)

# API Routes


@app.route('/api/cupcakes', methods=['GET'])
def list_cupcakes():
    """ returns a list of all cupcakes in the database"""

    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes) 


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def get_cupcake(cupcake_id):
    """ returns a single cupcake by id"""

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes',methods=['POST'])
def add_cupcake():
    flavor = request.json.get('flavor')
    size = request.json.get('size')
    rating = request.json.get('rating')
    image = request.json.get('image')
    cupcake = Cupcake(flavor=flavor, size=size, rating=rating, image=image)
    db.session.add(cupcake)
    db.session.commit()

    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def update_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
    cupcake = Cupcake.query.get_or_404(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message='successfully deleted')


# frontend display

@app.route('/')
def show_home():
    cupcakes = Cupcake.query.all()
    form = AddCupcake()
    return render_template('index.html', cupcakes=cupcakes, form=form)