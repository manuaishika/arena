"""Minimal stand-in for ARENA's `liveplot` package (not on PyPI).

Supports the small API that part32_goal_misgen/ppo.py uses: iterate over a range of training steps, call `.log(**metrics)`
each step; a progress bar shows the latest metrics and the curves are drawn once when the loop finishes.
"""
from __future__ import annotations

import matplotlib.pyplot as plt
from tqdm.auto import tqdm


class LivePlot:
    def __init__(self, steps, *panels: str, desc: str = "", unit: str = "it", show: bool = True, progress: bool = True, **_):
        self.steps = list(steps)
        self.panels = [p.split("|") if "|" in p else p.split() for p in panels]
        self.panels = [[name.strip() for name in p] for p in self.panels]
        self.desc, self.unit, self.show, self.progress = desc, unit, show, progress
        self.history: dict[str, list[float]] = {}
        self._bar = None

    def __iter__(self):
        self._bar = tqdm(self.steps, desc=self.desc, unit=self.unit, disable=not self.progress)
        try:
            yield from self._bar
        finally:
            self._bar.close()
            if self.show:
                self._draw()

    def log(self, **metrics) -> None:
        for k, v in metrics.items():
            self.history.setdefault(k, []).append(float(v))
        if self._bar is not None and self.progress:
            self._bar.set_postfix({k: f"{float(v):.3g}" for k, v in metrics.items()})

    def _draw(self) -> None:
        fig, axes = plt.subplots(1, len(self.panels), figsize=(5 * len(self.panels), 3.5), squeeze=False)
        for ax, names in zip(axes[0], self.panels):
            for name in names:
                if name in self.history:
                    ax.plot(self.history[name], label=name)
            ax.set_xlabel(self.unit)
            ax.legend()
        fig.tight_layout()
        plt.show()
