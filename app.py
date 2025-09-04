from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "CHANGE_THIS_SECRET"  # nécessaire pour les flash messages

# Configuration du serveur SMTP (ex: Gmail)
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='ton.email@gmail.com',
    MAIL_PASSWORD='ton_mot_de_passe_app',  # mot de passe ou App Password Gmail
    MAIL_DEFAULT_SENDER=('ACROW DZ', 'ton.email@gmail.com')
)

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not name or not email or not message:
            flash("❌ Veuillez remplir tous les champs.", "danger")
            return redirect(url_for('home') + "#contact")

        try:
            msg = Message(subject=f"Nouveau message de {name}",
                          recipients=["ghoriebmohamed9@gmail.com"],  # ton email de réception
                          body=f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}")
            mail.send(msg)
            flash("✅ Merci ! Votre message a été envoyé.", "success")
            return redirect(url_for('home') + "#contact")
        except Exception as e:
            flash(f"❌ Erreur lors de l'envoi : {str(e)}", "danger")
            return redirect(url_for('home') + "#contact")

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)
