from wtforms import Form, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



# Article Form Class
class experimentForm(Form):
    endpoint = StringField('Sparql Endpoint',render_kw={"placeholder": "e.g. Spareql Endpoint : http://dbpedia.org/sparql"})
    graph = StringField('Graph',validators=[DataRequired(),Length(max=20)])
    className = StringField('Class Name',validators=[DataRequired(),Length(max=20)])

