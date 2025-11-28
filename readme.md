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