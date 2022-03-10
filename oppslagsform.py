from wtforms import Form, StringField, SubmitField, validators, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.fields import TextAreaField, HiddenField


class OppslagsForm(Form):
    kategori = SelectField('Kategori', choices=[(0, 'Nyheter'), (1, 'Livsstil'), (2, 'Kultur'), (3, 'Annonser')])
    brukernavn = StringField('Brukernavn', validators=[DataRequired()])
    tittel = StringField('Tittel', validators=[DataRequired()])
    ingress = TextAreaField('Ingress', [validators.Length(min=6, max=300)])
    oppslagstekst = TextAreaField('Oppslagstekst', [validators.Length(min=6, max=1000)])
    submit = SubmitField('Update')
    id = HiddenField()
