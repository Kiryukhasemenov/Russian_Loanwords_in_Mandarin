## This is the previous (2019) term paper files.

| Type        | Filename           | Description  |
| ------------- |:-------------:| :-----:|
| document (.pdf) | [eReL_presentation.pdf](eReL_presentation.pdf) | Project presentation on "E-dictionaries and E-lexicography" conference, Zagreb, 11.05.2019|
| document (.pdf) | [Adaptation strategies of Russian phonetic loanwords in Chinese. Phonetic and graphic aspects](https://liber.rsuh.ru/elib/000014960) | Paper on the theme, published in RSUH/RGGU Bulletin. “Literary Theory. Linguistics. Cultural Studies ” Series (abstract - English, full text - Russian). The paper covers the main aspects of this research. |
| code (.py) | [transliterator.py](transliterator.py) | Algorithm for generation of Xinhua-based transliterations |
| code (.py) | [data_cleaner.ipynb](data_cleaner.ipynb) | Cleaning the Wikidata raw data (input: `wikidata_source`, output: `data_preprocessed_with_duplicates.csv`) |
| code (.py) | [dataset_aggregation.ipynb](dataset_aggregation.ipynb) | Adding Xinhua transliteration and metrics to the clean data (input: `data_preprocessed_with_duplicates.csv`, output: `data_total.csv`). For details, see corresponding [README](../data) file |
| code (.py) | [dataset_study.ipynb](dataset_study.ipynb) | Study of the dataset, many plots inside (input: `data_total.csv`). For details about the data, see corresponding [README](../data) file |
| code (.py) | [bkrs_processing.ipynb](bkrs_processing.ipynb) | Creating the subset of proper names with pinyin transcriptions (input: `data_total.csv`, output: `data_with_translit.csv`, for details, see corresponding [README](../data) file) |
| code (.py) | [BKRS_study.ipynb](BKRS_study.ipynb) | Study of the phonetic adaptation of the Russian consonants (input: `data_with_translit.csv`, `wlc_cd.csv`, for details, see corresponding [README](../data) file) |
| code (.py) | [Wailaici_Cidian_comparison.ipynb](Wailaici_Cidian_comparison.ipynb) | Comparison of Xinhua prescriptions to data from Chinese Loanword Dictionary (input: `wlc_cd.csv`, for details, see corresponding [README](../data) file) |
