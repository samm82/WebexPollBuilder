MAIN_FILE = "src/Webex Poll Builder.pyw"
TEST_PATH = ./test
SRC_PATH  = ./src

.PHONY: $(MAIN_FILE) test

compile: $(MAIN_FILE)
	pyinstaller --onefile $^
	npx embedme README.md

run: $(MAIN_FILE)
	py $^

lint:
	flake8 --ignore=E402,F403,F405,N802,N806,N813,N815,W504 .

test:
	pytest --cov-report term --cov=$(SRC_PATH) $(TEST_PATH)
