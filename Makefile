include ./Makefile.in.mk


.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	$(RUN) isort --virtual-env="$(DIR_VENV)" "$(DIR_SRC)" "$(DIR_SCRIPTS)" "$(DIR_TESTS)"
	$(RUN) black "$(DIR_SRC)" "$(DIR_SCRIPTS)" "$(DIR_TESTS)"


.PHONY: test
test:
	$(call log, running tests)
	$(RUN) pytest
	$(RUN) isort --virtual-env="$(DIR_VENV)" --check-only "$(DIR_SRC)" "$(DIR_SCRIPTS)" "$(DIR_TESTS)"
	$(RUN) black --check "$(DIR_SRC)" "$(DIR_SCRIPTS)" "$(DIR_TESTS)"


.PHONY: run
run:
	$(call log, starting local web server)
	$(PYTHON) src/manage.py runserver


.PHONY: run-prod
run-prod:
	$(call log, starting local web server)
	$(RUN) gunicorn --config="$(DIR_SCRIPTS)/gunicorn.conf.py" project.wsgi:application


.PHONY: sh
sh:
	$(call log, starting Python shell)
	$(PYTHON) src/manage.py shell


.PHONY: venv
venv:
	$(call log, installing packages)
	$(PIPENV_INSTALL)


.PHONY: venv-dev
venv-dev:
	$(call log, installing development packages)
	$(PIPENV_INSTALL) --dev


.PHONY: pycharm
pycharm:
	$(call log, setting pycharm up)
	$(PYTHON) $(DIR_SCRIPTS)/setup_pycharm.py


.PHONY: db
db: resetdb
	$(call log, setting db up)


.PHONY: data
data: static
	$(call log, preparing data)


.PHONY: static
static:
	$(call log, collecting static)
	$(PYTHON) src/manage.py collectstatic --noinput


.PHONY: su
su:
	$(call log, starting Python shell)
	$(PYTHON) src/manage.py createsuperuser

.PHONY: resetdb
resetdb:  dropdb createdb migrations migrate
	$(call log, resetting db to initial state)


.PHONY: dropdb
dropdb:
	$(call log, dropping database)
	psql \
		--echo-all \
		--username=$(shell $(PYTHON) $(DIR_SCRIPTS)/get_db_user.py) \
		--no-password \
		--host=localhost \
		--dbname=postgres \
		--command="DROP DATABASE IF EXISTS \"$(shell $(PYTHON) $(DIR_SCRIPTS)/get_db_name.py)\";"


.PHONY: createdb
createdb:
	$(call log, creating database)
	psql \
		--echo-all \
		--username=$(shell $(PYTHON) $(DIR_SCRIPTS)/get_db_user.py) \
		--no-password \
		--host=localhost \
		--dbname=postgres \
		--command="CREATE DATABASE \"$(shell $(PYTHON) $(DIR_SCRIPTS)/get_db_name.py)\";"


.PHONY: migrations
migrations:
	$(call log, generating migrations)
	$(PYTHON) src/manage.py makemigrations



.PHONY: migrate
migrate:
	$(call log, applying migrations)
	$(PYTHON) src/manage.py migrate
