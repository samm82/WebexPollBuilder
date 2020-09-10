MAIN_FILE = "src/Webex Poll Builder.pyw"

.PHONY: $(MAIN_FILE)

compile: $(MAIN_FILE)
		pyinstaller --onefile $^

run: $(MAIN_FILE)
		py $^
lint:
	flake8 --ignore=N802,N806,N813 --exclude=$(TEST_PATH)/* .
	# --per-file-ignores='Input.py,SearchQuery.py:E501' --ignore=E266,N802,N803,N806,N812,W504