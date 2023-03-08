from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/inventory'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    shell_life = db.Column(db.String(15), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    quantity = db.Column(db.Integer)
    height = db.Column(db.Float(precision=2))

    def __init__(self, id, name, shell_life, price, quantity, height):
        self.id = id
        self.name = name
        self.shell_life = shell_life
        self.price = price
        self.quantity = quantity
        self.height = height

    def json(self):
        return {"isbn13": self.id, "Crop Name": self.name, "Shell Life": self.shell_life, "Price": self.price, "Quantity": self.quantity, "Height": self.height}


@app.route("/inventory")
def get_all_crops():
    inventory = Inventory.query.all()
    if len(inventory):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "inventory": [crop.json() for crop in inventory]
                }
            }
        )
    return jsonify(
        {
            "code": 404,
            "message": "There are no crops."
        }
    ), 404

@app.route("/inventory")



if __name__ == '__main__':
    app.run(port=5000, debug=True)
