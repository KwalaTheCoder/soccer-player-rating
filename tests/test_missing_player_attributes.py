"""The six outfield attributes cannot score rows with no measurements."""
import json
from pathlib import Path
import tempfile
import unittest
import numpy as np
import pandas as pd
from mlproject.core import prepare, predict, train


class MissingAttributeTests(unittest.TestCase):
    def test_empty_feature_rows_are_excluded_and_cannot_be_scored(self):
        config = json.loads(Path('project.json').read_text())
        rng = np.random.default_rng(42)
        df = pd.DataFrame({c: rng.uniform(20, 90, 80) for c in config['features']})
        df['overall'] = (df.pace + df.shooting) / 2
        df['player_id'] = np.arange(80)
        df.loc[0, config['features']] = np.nan
        df.loc[1, 'overall'] = np.nan
        X, y, _, _ = prepare(df, config)
        self.assertEqual(len(X), 78)
        self.assertEqual(len(y), 78)
        with tempfile.TemporaryDirectory() as out:
            report = train(df, config, out, folds=2, group_column='player_id')
            self.assertEqual(report['missing_target_rows_removed'], 1)
            self.assertEqual(report['missing_predictor_rows_removed'], 1)
            with self.assertRaisesRegex(ValueError, 'no observed predictor'):
                predict(Path(out) / 'model.joblib', df.iloc[:1])


if __name__ == '__main__':
    unittest.main()
