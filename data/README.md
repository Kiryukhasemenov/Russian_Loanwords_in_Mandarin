# Research Data

Here you will find a comprehensive overview of the data files.

|Year | Doc type | Filename | Description  |
| --- | ------------- |:-------------:| -----:|
| 2019 | directory, .tsv files     | [wikidata_source](../../blob/master/data/wikidata_source) | Tables in .tsv format, which are downloaded from Wikidata |
| 2019 | .csv | [data_preprocessed_with_duplicates.csv](../../blob/master/data/data_preprocessed_with_duplicates.csv)      | All data from Wikidata, cleared from noise |
| 2019 | .csv | [data_with_duplicates_pre_final.csv](../../blob/master/data/data_with_duplicates_pre_final.csv)      |    All data from Wikidata, cleared from noise (supporting data, necessary for aggregation purposes) |
| 2019 | .csv | [data_total.csv](../../blob/master/data/data_total.csv)      | Main dataset for the statistic analysis |
| 2019 | .txt | [reference_corpus.txt](../../blob/master/data/reference_corpus.txt)      | Reference corpus of 5 modern Chinese novels (necessary for N-gram analysis in `dataset_study.ipynb`  |
| 2019, 2020 | .csv | [data_translit_cleared.csv](../../blob/master/data/data_translit_cleared.csv)      | Subset of Wikidata dataset with transcriptions |
| 2019, 2020 | .csv | [wlc_cd.csv](../../blob/master/data/wlc_cd.csv)      | Dataset from the Chinese Loanword Dictionary*  |
| 2020 | .csv | [wlc_epentheses.csv](../../blob/master/data/wlc_epentheses.csv)  | Dataset with all epenthetic entries from the Chinese Loanword Dictionary |
| 2020 | .csv | [bkrs_epentheses.csv](../../blob/master/data/bkrs_epentheses.csv)  | Dataset with all epenthetic entries from the Wikidata + BKRS subset |
| 2020 | .txt | [long_propers_list.txt](../../blob/master/data/long_propers_list.txt) | List of proper names, aggregated from two transliteration guidelines - [辛华, 1997], [周俊英, 2003]* |



\* [Liu 1985] - Liu, Zh.-T. (ed.). Hanyu wailaici cidian (汉语外来词词典). Shanghai: Shanghai cishu chubanshe. 1985. 449 p.  
  [辛华, 1997] - 辛华. 俄语 姓名 译名 手册. 北京: 商务印书馆, 1997.  
  [周俊英, 2003] - 周俊英. 新编俄罗斯地名译名手册. 北京: 商务印书馆, 2003.
