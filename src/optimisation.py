"""Reference implementation of the BBO approach, reconstructed for this repository.

This code is not the original historical notebook. Proposed new points do not reproduce
all historical submissions, which included manual review and changing heuristics.
"""
from pathlib import Path
import numpy as np
from scipy.stats import norm
from scipy.stats import qmc
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern, WhiteKernel


def read_function_data(base_dir, function):
    """Read starter arrays and the 12 subsequently evaluated queries."""
    import csv
    base_dir = Path(base_dir)
    initial_dir = base_dir / "data" / "initial_data" / f"function_{function}"
    X = np.load(initial_dir / "initial_inputs.npy")
    y = np.load(initial_dir / "initial_outputs.npy").ravel()
    with (base_dir / "data" / "processed" / "query_history.csv").open(newline="") as fh:
        rows = [r for r in csv.DictReader(fh) if int(r["function"]) == function]
    new_X = np.asarray([[float(r[f"x{i}"]) for i in range(1, X.shape[1] + 1)] for r in rows])
    new_y = np.asarray([float(r["output"]) for r in rows])
    return np.vstack([X, new_X]), np.r_[y, new_y]


def expected_improvement(mean, std, best, xi=0.01):
    """Expected improvement for a maximisation task."""
    std = np.asarray(std)
    gain = mean - best - xi
    Z = np.divide(gain, std, out=np.zeros_like(gain), where=std > 1e-12)
    return np.where(std > 1e-12, gain * norm.cdf(Z) + std * norm.pdf(Z), 0.0)


def propose_query(X, y, *, seed=42, n_candidates=4096, lower=0.005, upper=0.995):
    """Fit an ARD Matérn GP and maximise EI across Sobol/local candidates.

    Function 5 (large positive outputs) uses log1p targets as a practical heuristic.
    Outputs are standardised by scikit-learn for numerical stability.
    """
    X, y = np.asarray(X, float), np.asarray(y, float)
    d = X.shape[1]
    target = np.log1p(y) if np.all(y >= 0) and np.max(y) > 100 else y
    kernel = ConstantKernel(1.0, (1e-2, 1e2)) * Matern(
        length_scale=np.ones(d), length_scale_bounds=(1e-2, 5), nu=2.5
    ) + WhiteKernel(noise_level=1e-5, noise_level_bounds=(1e-9, 1e-1))
    gp = GaussianProcessRegressor(kernel=kernel, normalize_y=True, n_restarts_optimizer=2, random_state=seed)
    gp.fit(X, target)
    m = int(np.ceil(np.log2(n_candidates)))
    space = qmc.Sobol(d, scramble=True, seed=seed).random_base2(m)[:n_candidates]
    space = lower + (upper - lower) * space
    rng = np.random.default_rng(seed)
    best_x = X[np.argmax(y)]
    local = np.clip(best_x + rng.normal(0, 0.06, size=(n_candidates//2, d)), lower, upper)
    candidates = np.vstack([space, local])
    mean, std = gp.predict(candidates, return_std=True)
    ei = expected_improvement(mean, std, np.max(target), xi=0.01)
    # Avoid exact repeats of previously evaluated inputs.
    distances = np.linalg.norm(candidates[:, None] - X[None, :], axis=-1).min(axis=1)
    ei[distances < 1e-5] = -np.inf
    idx = int(np.argmax(ei))
    return candidates[idx], dict(acquisition=float(ei[idx]), kernel=str(gp.kernel_))
