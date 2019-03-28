from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, TextAreaField, SubmitField

class newChallenge(Form):
    target = StringField('target:', [validators.DataRequired(message='Wprowadź dane'), validators.Length(min=5, max=25)], render_kw={"placeholder": "Target"})
    budget = StringField('buget:', [validators.DataRequired(message='Wprowadź dane'), validators.Length(min=5, max=25)], render_kw={"placeholder": "Budget"})
    data_adv = StringField('data/advance:', [validators.DataRequired(message='Wprowadź dane')], render_kw={"placeholder": "Data/advanced"})
    wylacznosc = StringField('wyłączność:', [ validators.DataRequired(message='Wprowadź dane')], render_kw={"placeholder": "Wylączność"})
    technology = StringField('technology:', [validators.DataRequired(message='Wprowadź dane')],render_kw={"placeholder": "technology"})
    location = StringField('lokalizacja:', [validators.DataRequired(message='Wprowadź dane')],render_kw={"placeholder": "lokalizacja"})
    wishlist = StringField('wishlist:', [validators.DataRequired(message='Wprowadź dane')],render_kw={"placeholder": "lista"})
    aboutcompany = TextAreaField(u'o firmie/o nas', render_kw={"placeholder": "o firmie"})
    submitnewchallenge=SubmitField('Dodaj')

class RegistrationPrimaryForm(Form):
    firstname = StringField('Imię', [validators.DataRequired(message='Wprowadź imię'), validators.Length(min=5, max=25)], render_kw={"placeholder": "Imię"})
    lastname = StringField('Nazwisko', [validators.DataRequired(message='Wprowadź nazwisko'), validators.Length(min=5, max=25)], render_kw={"placeholder": "Nazwisko"})
    email = StringField('Adres e-mail', [validators.DataRequired(message='Wprowadź adres e-mail'), validators.Email(message='Podaj poprawny adres E-mail')], render_kw={"placeholder": "Adres e-mail"})
    password = PasswordField('Hasło', [ validators.DataRequired(message='Wprowadź hasło')], render_kw={"placeholder": "Hasło"})
    companycheck=BooleanField('Are you representing a company')
    company = StringField('Nazwa firmy',[validators.DataRequired(message='Podaj nazwę firmy'), validators.Length(min=5, max=25)],render_kw={"placeholder": "Firma"})
    submitpr=SubmitField('Dołącz teraz')

class RegistrationAdvForm(Form):
    location = StringField('Lokalizacja', [validators.DataRequired(message='Wprowadź lokalizację'), validators.Length(min=5, max=25)], render_kw={"placeholder": "Lokalizacja"})
    phone = IntegerField('Telefon', [validators.DataRequired(message='Wprowadź telefon'), validators.Length(min=9, max=9)], render_kw={"placeholder": "Telefon"})
    age = IntegerField('Wiek', [validators.DataRequired(message='Wprowadź wiek')], render_kw={"placeholder": "Wiek"})
    description= TextAreaField(u'Opis',  render_kw={"placeholder": "Opis"})
    submitad=SubmitField('Dołącz teraz')

class RegistrationAdvChForm(Form):
    solveChellange = BooleanField('1. I\'m the techpistol, I want to solve chellanges ')
    needTech = BooleanField('2. I want to give chellanges, I need techpistols')
    submitch = SubmitField('Next')

#------------------------------------------------old challange--------------------------------------------------------------------------


class EditProfileForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_l('About me'),
                             validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_('Please use a different username.'))


class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators=[DataRequired()])
    submit = SubmitField(_l('Submit'))


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class MessageForm(FlaskForm):
    message = TextAreaField(_l('Message'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))
