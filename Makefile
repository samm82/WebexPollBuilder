MAIN_FILE = "src/Webex Poll Builder.pyw"

.PHONY: $(MAIN_FILE)

compile: $(MAIN_FILE)
		pyinstaller --onefile $^

run: $(MAIN_FILE)
		py $^