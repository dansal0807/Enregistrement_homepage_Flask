Do que se trata esta aplicação?
-------------

This is a simple Python/Flask application intended to provide a working example of Uber's external API. The goal of these endpoints is to be simple, well-documented and to provide a base for developers to develop other applications off of.

Este projeto é uma aplicação simples de Python por meio do framework Flask. O objetivo desta aplicação é o cadastramento
em um banco de dado por meio de formulários que indicam o nome de usuário, CPF, PIS, assim como o endereço do usuário.
É preciso colocar um CPF válido para que a aplicação funcione. A aplicação também conta com uma página do usuário onde
ele pode verificar sua informações pessoais, assim como também existe uma página para edição de tais informações. 

How To Use This
---------------

1. Navigate over to https://developer.uber.com/, and sign up for an Uber developer account.
2. Register a new Uber application and make your Redirect URI `http://localhost:7000/submit` - ensure that both the `profile` and `history` OAuth scopes are checked.
3. Fill in the relevant information in the `config.json` file in the root folder and add your client id and secret as the environment variables `UBER_CLIENT_ID` and `UBER_CLIENT_SECRET`.
4. Run `export UBER_CLIENT_ID="`*{your client id}*`"&&export UBER_CLIENT_SECRET="`*{your client secret}*`"`
5. Run `pip install -r requirements.txt` to install dependencies
6. Run `python app.py`
7. Navigate to http://localhost:7000 in your browser


Testing
-------

1. Install the dependencies with `make bootstrap`
2. Run the command `make test`
3. If you delete the fixtures, or decide to add some of your own, you’ll have to re-generate them, and the way this is done is by running the app, getting an auth_token from the main page of the app. Paste that token in place of the `test_auth_token` at the top of the `test_endpoints.py` file, then run the tests.


Development
-----------

If you want to work on this application we’d love your pull requests and tickets on GitHub!

1. If you open up a ticket, please make sure it describes the problem or feature request fully.
2. If you send us a pull request, make sure you add a test for what you added, and make sure the full test suite runs with `make test`.
