# API de Autenticação e Autorização

## Introdução

Este projeto é uma API de autenticação e autorização desenvolvida com Django e Django REST Framework (DRF). A API fornece funcionalidades essenciais para gerenciar o registro, login, recuperação de senha, verificação de email, e gerenciamento de permissões de usuários. É especialmente útil para integrar em aplicativos de bancos e fintechs para garantir a segurança no acesso às contas e operações financeiras.

## Funcionalidades

- **Registro de Usuário**: Permite novos usuários se registrarem no sistema.
- **Login e Autenticação**: Autenticação de usuários com email e senha utilizando JWT.
- **Recuperação de Senha**: Processo seguro para recuperação de senhas esquecidas.
- **Verificação de Email**: Verificação de email durante o registro e em momentos críticos.
- **Gerenciamento de Sessões**: Monitoração e controle de sessões ativas.
- **Gerenciamento de Permissões**: Controle de acessos baseado em roles.
- **Operações Financeiras Seguras**: Verificação adicional de identidade para operações críticas.
- **Logs de Atividades**: Registro detalhado de atividades para auditoria.

## Tecnologias Utilizadas

- **Django**: Framework web principal.
- **Django REST Framework (DRF)**: Para construção de APIs RESTful.
- **djangorestframework-simplejwt**: Para autenticação baseada em JSON Web Tokens (JWT).


## Requisitos

- Python 3.8+
- Django 3.2+


## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/api-autenticacao-autorizacao.git
   cd api-autenticacao-autorizacao
