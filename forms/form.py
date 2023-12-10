from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, DecimalField
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    data = SelectField('Metric',
                                choices=[('x1', 'Inexpensive restaurant meal'),
                                         ('x2', 'Mid-range restaurant meal'),
                                         ('x3', 'Combo fast food meal'),
                                         ('x4', 'Domestic beer in restaurants'),
                                         ('x5', 'Imported beer in restaurants'),
                                         ('x6', 'Cappuccino in restaurants'),
                                         ('x7', 'Coke/Pepsi in restaurants'),
                                         ('x8', 'Water in restaurants'),
                                         ('x9', 'Milk'),
                                         ('x10', 'White bread loaf'),
                                         ('x11', 'White rice'),
                                         ('x12', 'Chicken eggs'),
                                         ('x13', 'Local cheese'),
                                         ('x14', 'Chicken fillets'),
                                         ('x15', 'Back leg red meat (beef)'),
                                         ('x16', 'Apples'),
                                         ('x17', 'Banana'),
                                         ('x18', 'Oranges'),
                                         ('x19', 'Tomato'),
                                         ('x20', 'Potato'),
                                         ('x21', 'Onion'),
                                         ('x22', 'Lettuce'),
                                         ('x23', 'Water at the market'),
                                         ('x24', 'Bottle of mid-range wine'),
                                         ('x25', 'Domestic beer at the market'),
                                         ('x26', 'Imported beer at the market'),
                                         ('x27', 'Cigarettes (Marlboro)'),
                                         ('x28', 'One-way transport ticket'),
                                         ('x29', 'Monthly transport pass'),
                                         ('x30', 'Taxi start'),
                                         ('x31', 'Taxi 1km drive'),
                                         ('x32', 'Taxi 1 hour waiting'),
                                         ('x33', 'Gasoline'),
                                         ('x34', 'Volkswagen Golf'),
                                         ('x35', 'Toyota Sedan'),
                                         ('x36', 'Basic services (ЖКХ)'),
                                         ('x37', 'Mobile phone tariff per minute'),
                                         ('x38', 'Internet per month'),
                                         ('x39', 'Monthly fitness club pass'),
                                         ('x40', 'Tennis court rent'),
                                         ('x41', 'Cinema (International release)'),
                                         ('x44', 'Jeans'),
                                         ('x45', 'Summer Dress in a Chain store'),
                                         ('x46', 'Running shoes'),
                                         ('x47', "Business shoes (men's)"),
                                         ('x48', 'Apartment rent in city centre (1bd)'),
                                         ('x49', 'Apartment rent outside city centre (1bd)'),
                                         ('x50', 'Apartment rent in city centre (3bd)'),
                                         ('x51', 'Apartment rent outside city centre (3bd)'),
                                         ('x52', 'Price per m^2 in city centre'),
                                         ('x53', 'Price per m^2 outside city centre'),
                                         ('x54', 'Average monthly net salary (after tax)'),
                                         ('x55', 'Mortgage Interest rate, yearly'),
                                         ('food', 'Middle-class food per month*'),
                                         ('life', 'Middle-class life per month**')])
    top = SelectField('Top #',
                       choices=[(5, '5'),
                                (10, '10'),
                                (15, '15')])
    highlow = SelectField('Highest or lowest?',
                       choices=[('top', 'Highest'),
                                ('btm', 'Lowest')])
    submit = SubmitField('Reload the board')

class MapForm(FlaskForm):
    data = SelectField('Metric',
                                choices=[('x1', 'Inexpensive restaurant meal'),
                                         ('x2', 'Mid-range restaurant meal'),
                                         ('x3', 'Combo fast food meal'),
                                         ('x4', 'Domestic beer in restaurants'),
                                         ('x5', 'Imported beer in restaurants'),
                                         ('x6', 'Cappuccino in restaurants'),
                                         ('x7', 'Coke/Pepsi in restaurants'),
                                         ('x8', 'Water in restaurants'),
                                         ('x9', 'Milk'),
                                         ('x10', 'White bread loaf'),
                                         ('x11', 'White rice'),
                                         ('x12', 'Chicken eggs'),
                                         ('x13', 'Local cheese'),
                                         ('x14', 'Chicken fillets'),
                                         ('x15', 'Back leg red meat (beef)'),
                                         ('x16', 'Apples'),
                                         ('x17', 'Banana'),
                                         ('x18', 'Oranges'),
                                         ('x19', 'Tomato'),
                                         ('x20', 'Potato'),
                                         ('x21', 'Onion'),
                                         ('x22', 'Lettuce'),
                                         ('x23', 'Water at the market'),
                                         ('x24', 'Bottle of mid-range wine'),
                                         ('x25', 'Domestic beer at the market'),
                                         ('x26', 'Imported beer at the market'),
                                         ('x27', 'Cigarettes (Marlboro)'),
                                         ('x28', 'One-way transport ticket'),
                                         ('x29', 'Monthly transport pass'),
                                         ('x30', 'Taxi start'),
                                         ('x31', 'Taxi 1km drive'),
                                         ('x32', 'Taxi 1 hour waiting'),
                                         ('x33', 'Gasoline'),
                                         ('x34', 'Volkswagen Golf'),
                                         ('x35', 'Toyota Sedan'),
                                         ('x36', 'Basic services (ЖКХ)'),
                                         ('x37', 'Mobile phone tariff per minute'),
                                         ('x38', 'Internet per month'),
                                         ('x39', 'Monthly fitness club pass'),
                                         ('x40', 'Tennis court rent'),
                                         ('x41', 'Cinema (International release)'),
                                         ('x44', 'Jeans'),
                                         ('x45', 'Summer Dress in a Chain store'),
                                         ('x46', 'Running shoes'),
                                         ('x47', "Business shoes (men's)"),
                                         ('x48', 'Apartment rent in city centre (1bd)'),
                                         ('x49', 'Apartment rent outside city centre (1bd)'),
                                         ('x50', 'Apartment rent in city centre (3bd)'),
                                         ('x51', 'Apartment rent outside city centre (3bd)'),
                                         ('x52', 'Price per m^2 in city centre'),
                                         ('x53', 'Price per m^2 outside city centre'),
                                         ('x54', 'Average monthly net salary (after tax)'),
                                         ('x55', 'Mortgage Interest rate, yearly'),
                                         ('food', 'Middle-class food per month*'),
                                         ('life', 'Middle-class life per month**')])
    high = DecimalField('highest')
    low = DecimalField('lowest')
    submit = SubmitField('Reload the map')
