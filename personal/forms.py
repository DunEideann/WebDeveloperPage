# from flask_wtf import FlaskForm
# from wtforms import TextField, BooleanField, TextAreaField, SubmitField
# class ContactForm(FlaskForm):
#     name = TextField("Name")
#     email = TextField("Email")
#     subject = TextField("Subject")
#     message = TextAreaField("Message")
#     submit = SubmitField("Send")

from wtforms import Form, TextField, TextAreaField, SubmitField, validators, ValidationError
 
class ContactForm(Form):
  name = TextField("Nombre",  [validators.Required("Por favor ingrese su nombre"), validators.length(max=30, message='Por favor, ingrese un nombre con máximo de 30 caracteres')])
  email = TextField("Email",  [validators.Required("Por favor ingrese su email"), validators.Email("Mail en formato incorrecto")])
  subject = TextField("Título",  [validators.Required("Por favor ingrese un título"), validators.length(max=30, message='Por favor, ingrese un título con máximo de 30 caracteres')])
  message = TextAreaField("Mensaje",  [validators.Required("Por favor ingrese su mensaje"), validators.length(max=500, message='Por favor, ingrese un mensaje con máximo de 500 caracteres')])
  submit = SubmitField("Enviar")