Convert pdf to markdown 

```
python3 baseline_pymupdf4llm.py --pdf_dir data/var_test/pdf/ --md_dir output/var_test_pymu
```

Post process  by running post_process.ipynb

Create submission file by running:

```
python3 create_submission.py -s output/var_test_pymu_post
```

tham khao them repo sau https://github.com/icip-cas/READoc cho pdf to markdown process


evaluate

```
python3 evaluation/suite_e2e.py --gold_dir data/var_train/markdown --pred_dir output/var_train_1/ --result_json output/var_train_1/var_train_1.json
```