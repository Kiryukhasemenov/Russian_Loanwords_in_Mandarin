## This is the previous (2019) term paper files.

| Type        | Filename           | Description  |
| ------------- |:-------------:| :-----:|
| code (.py) | [transliterator.py](../../blob/master/2019/transliterator.py) | Algorithm for generation of Xinhua-based transliterations |
| code (.py) | [data_cleaner.ipynb](../../blob/master/2019/data_cleaner.ipynb) | Cleaning the Wikidata raw data (input: `wikidata_source`, output: `data_preprocessed_with_duplicates.csv`) |
| code (.py) | [dataset_aggregation.ipynb](../../blob/master/2019/dataset_aggregation.ipynb) | Adding Xinhua transliteration and metrics to the clean data (input: `data_preprocessed_with_duplicates.csv`, output: `data_total.csv`). For details, see corresponding [README](../../blob/master/data) file |
| code (.py) | [dataset_study.ipynb](../../blob/master/2019/dataset_study.ipynb) | Study of the dataset, many plots inside (input: `data_total.csv`). For details about the data, see corresponding [README](../../blob/master/data) file |
| code (.py) | [bkrs_processing.ipynb](../../blob/master/2019/bkrs_processing.ipynb) | Creating the subset of proper names with pinyin transcriptions (input: `data_total.csv`, output: `data_with_translit.csv`, for details, see corresponding [README](../../blob/master/data) file) |
| code (.py) | [BKRS_study.ipynb](../../blob/master/2019/BKRS_study.ipynb) | Study of the phonetic adaptation of the Russian consonants (input: `data_with_translit.csv`, `wlc_cd.csv`, for details, see corresponding [README](../../blob/master/data) file) |
| code (.py) | [Wailaici_Cidian_comparison.ipynb](../../blob/master/2019/Wailaici_Cidian_comparison.ipynb) | Comparison of Xinhua prescriptions to data from Chinese Loanword Dictionary (input: `wlc_cd.csv`, for details, see corresponding [README](../../blob/master/data) file) |
| document (.pdf) | [eReL_presentation.pdf](../../blob/master/2019/eReL_presentation.pdf) | Project presentation on "E-dictionaries and E-lexicography" conference, Zagreb, 11.05.2019|
