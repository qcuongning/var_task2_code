Convert pdf to markdown, 

** notice function pdfplumber_table_to_markdown **


```
python3 full_pipeline_pdfplumber.py
```

evaluate

```
python3 evaluation/suite_e2e.py --gold_dir data/var_train/markdown --pred_dir output/var_train_namlt/ --result_json sample/gt.json

```

or evaluate difficult sample

```
python3 evaluation/suite_e2e.py --gold_dir sample/gt --pred_dir sample/pred/ --result_json sample/gt.json
```



top 5 lowest edit distance scores:
- Public_257.md: 0.16049538565800048
- Public_017.md: 0.39258546421042984
- Public_264.md: 0.44858299595141704
- Public_255.md: 0.449904809351814
- Public_253.md: 0.5000218245307726