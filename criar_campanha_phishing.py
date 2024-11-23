class criar_campanha_phishing:
   def campanha_de_phishing(self):
      from mailersend import emails

# Substitua pela sua chave de API
mailer = emails.NewEmail("CHAVE_DE_API")

# E-mail do remetente fixo
my_mail = "INSIRA_O_EMAIL_GERADO_NO_MAIL_SENDER"

# Função para solicitar dados do e-mail via terminal
def criar_email():
    # Solicitar a lista de destinatários
    subscriber_list_input = input("Digite os e-mails dos destinatários (separados por vírgula): ")
    subscriber_list = [email.strip() for email in subscriber_list_input.split(",")]

    # Solicitar o assunto do e-mail
    subject = input("Digite o assunto do e-mail: ")

    # Solicitar o corpo do e-mail em formato de texto
    text = input("Digite o corpo do e-mail em formato de texto: ")

    # Solicitar o corpo do e-mail em formato HTML
    html = input("Digite o corpo do e-mail em formato HTML: ")

    # Construir o payload para enviar o e-mail
    email_payload = {
        "from": {
            "email": my_mail,
            "name": "NOME_DO_EMAIL"
        },
        "to": [{"email": email} for email in subscriber_list],
        "subject": subject,
        "text": text,
        "html": html
    }

    # Enviar o e-mail
    response = mailer.send(email_payload)

    # Exibir a resposta para debugging
    print(response)

# Chamar a função para criar e enviar o e-mail
criar_email()
