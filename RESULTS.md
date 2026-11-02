# Real-data evaluation — 2026-11-02

Input: `Soccer/players_20.csv`. Dataset SHA-256: `09309ea19750af6a3db973a20ff44fde7917f55c9a6dd19bdb4a29a35f47d6f9`.

Model selection used only training-fold CV. One final holdout was reserved before preprocessing. The full CV leaderboard, dependency versions, seed, feature schema and split sizes are in [experiments/report.json](experiments/report.json).

- Model: **ExtraTreesRegressor**
- Training rows: **12993**; holdout rows: **3249**
- Selection metric: `neg_mean_absolute_error`; selected CV score: **-0.972978**
- Dummy baseline CV score on the same folds: **-5.417494**
- Five CV folds; seed 42; tuning: **False**
- Identical raw predictor rows grouped: **True**

| Metric | Holdout value |
|---|---:|
| mae | 0.973818 |
| rmse | 1.263262 |
| r2 | 0.964987 |


## Dataset-specific interpretation

Scope is players with at least one observed value among pace, shooting, passing, dribbling, defending and physic. Exactly 2036 rows with all six missing are excluded before the split using a target-independent rule. The model rejects entirely unobserved predictor rows at inference. Partially missing attributes are imputed inside folds. This single-season result does not establish performance for goalkeepers or future seasons.

## Reproduce

Activate an environment with the project's requirements, change to the repository root, and run:

```cmd
python -m mlproject train --data "D:\data\Soccer\players_20.csv" --output artifacts --folds 5 --seed 42
```

Results were obtained with the dependency versions recorded in the JSON report. Different versions can change results slightly. Negative MAE selection scores are higher-is-better. CV scores are selection estimates and optimistic; the holdout is the final internal result. Hyperparameter tuning is enabled on the smaller datasets and diabetes; for credit, soccer, student and churn the default bounded candidate comparison is used. Scores are not directly comparable across datasets or tasks.

Do not tune against the now-observed holdout or claim improvement over the legacy notebooks: leakage, split policies and preprocessing differ. Raw data, row-level predictions and trained pickle artifacts are not included in this evidence commit.
