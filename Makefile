processed: data/processed/elections.csv data/processed/voting_methods.csv
.phony: processed

raw : data/raw/elections.json
.phony : raw

data/processed/elections.csv data/processed/voting_methods.csv &: data/raw/elections.json
	mkdir -p data/processed/
	python -m src.process

data/raw/elections.json :
	mkdir -p data/raw/
	python -m src.download
