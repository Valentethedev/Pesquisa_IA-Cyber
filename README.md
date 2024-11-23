# Uira.AI Documentação
## Apresentação
Uira.AI é um protótipo criado em parceria entre diversos alunos do grupo Ânima Educação, gerado a partir de uma pesquisa onde percebemos que o avanço das IA's Generativas. Também foi evidente que no mundo da cibersegurança, esse avanço ocorreu com as ferramentes. Porém, nos voltando para a maior problemática da cibersegurança, percebemos uma lacuna que a IA poderia contribuir para preencher, mesmo que parcialmente, esse espaço. E assim nasceu o projeto Uira.AI, um software desenvolvido em torno de um modelo llm, que auxilia os times de segurança a criar campanhas de phishing, monitorar e extrair insights. Ainda é possível produzir campanhas de conscientização em cima das próprias campanhas. Permitindo um treinamento alinhado ao negócio.

A feature criar_campanha_email é onde ocorre toda a lógica das campanhas, a Uira está sendo projetada em cima do llama3. Onde foi passado diversos estudos de caso de criação de campanha de phishing e derivados. Através do processamento de linguagem natural nativo do llama3, também é possível extrair materiais textuais de conscientização.

A parte do software que não está disponível no repositório é o modelo de llm propriamente dito, porém, é possivel baixar o llama3 pelo [ollama](https://ollama.com/download) e personaliza-lo. A feature de menu e a feature de criar email não estão operando em conjunto.

>[!NOTE]
> Próximas etapas a serem feitas no projeto:
> * Integrar feature de criação de links e espelhamento de telas, para criar telas que simulam sites reais, afim de avaliar a capacidade do colaborador de identificar sites falsos;
> * Hospedagem do modelo Uira na Nuvem;
> * Fine tuning do modelo para aperfeiçamento;
> * Mudando de plataforma de rastreio de emails(para extrair insights ainda mais detalhados).
## Reposítório com artigo científico e parecer jurídico relacionados ao projeto.
O repositório pode ser encontrado [aqui](https://drive.google.com/drive/folders/1218Zs7UdzvOnecOGUhzh44NA6JUsUbB8).
### Também temos um vídeo de apresentação do projeto.
Realizamos o vídeo com o intuito de apresentar nosso projeto para todos que tenham curiosidade, o link do vídeo pode ser encontrado no nosso canal do [YouTube](https://www.youtube.com/watch?v=AWap_AUYXsU).
## Recursos utilizados no protótipo.
### Linguagem utilizada
* Python3 Versão 3.12;
### Bibliotecas utilizadas

* mailSender;
* OS;
* Time;
* pip;
> [!IMPORTANT]
> Bibliotecas do python que foram utilizadas.
### IDE utilizada
* VSCode;
### Plataforma para consumo de LLM's
* OLlama;
### Modelo de LLM usado como base
* llama3.1 8b;
### Envio e monitoramento do e-mails
* API MailSender;
* Plataforma MailSender;
## Resposáveis pelo projeto
* [Gabriel](https://www.linkedin.com/in/gabrielgideonmartins)
* [Artur](https://www.linkedin.com/in/artur-valente-0765a4273/)
* [Mazille](https://www.linkedin.com/in/mazille-mafra)
