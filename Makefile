MAIN_FILE = "src/Webex Poll Builder.pyw"

.PHONY: $(MAIN_FILE)

compile: $(MAIN_FILE)
	pyinstaller --onefile $^

run: $(MAIN_FILE)
	py $^

lint:
	flake8 --ignore=N802,N806,N813,W504 --exclude=$(TEST_PATH)/* .
