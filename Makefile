.PHONY : authors works editions
targets=authors works editions

all : $(foreach target,$(targets),data/processed/$(target).txt)

data/processed/%.txt: data/unprocessed/%.txt
	python3 data/scripts/process.py $< $@

data/unprocessed/%.txt : data/unprocessed/%.txt.gz
	gzip -d -c $< > $@

data/unprocessed/%.txt.gz : $(targets)
	wget -O $@ https://openlibrary.org/data/ol_dump_$*_latest.txt.gz

