from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, RadioField, SelectField, StringField
from wtforms.validators import Length, NumberRange


class ParamsForm(FlaskForm):
    ticker = StringField("Ticker", validators=[Length(min=1, max=5)])
    strategy = SelectField(
        "Strategy",
        choices=[
            ("SMA crossover", "SMA crossover"),
            ("RSI oscillator", "RSI oscillator"),
        ],
        default="SMA crossover",
    )
    initial_cash = IntegerField("Initial cash", validators=[NumberRange(min=1)])
    commission = DecimalField(
        "Commission", places=5, validators=[NumberRange(min=-10, max=9.99999)]
    )
    leverage_multiple = IntegerField("Leverage", validators=[NumberRange(min=1)])
    trade_on_close = RadioField("Trade on close?", choices=["Yes", "No"], default="No")
    allow_hedging = RadioField("Allow hedging?", choices=["Yes", "No"], default="No")
    exclusive_orders = RadioField(
        "Exlcusive orders?", choices=["Yes", "No"], default="Yes"
    )
