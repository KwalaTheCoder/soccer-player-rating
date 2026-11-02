# Audit and refactor

Keeps the six FIFA player attributes from the original experiment, with a deterministic pace-by-physic interaction. Removes global outlier deletion that artificially narrows the test population and supports missing measurements. For repeated players use --group-column sofifa_id; a random split does not establish future-season performance.

Original algorithms and historical outputs remain in legacy/. No production dataset was available during refactoring; new real-data metrics remain unmeasured. See README.md for the reproducible evaluation protocol.
