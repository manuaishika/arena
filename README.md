# arena

Worked notebooks for the [ARENA](https://www.arena.education/curriculum) AI-safety curriculum
(chapters 1 and 3 first, then the rest).

Exercise material, tests and `solutions.py` helpers come from
[callummcdougall/ARENA_3.0](https://github.com/callummcdougall/ARENA_3.0) (credit: ARENA / LISA).
The notebooks here have the exercises filled in and are executed, so outputs are saved in them.

## Layout

```
chapter1_transformer_interp/exercises/
    plotly_utils.py
    part1_transformer_from_scratch/    # 1.1 notebook + tests.py / solutions.py from upstream
```

Each notebook finds the repo root itself, so run it from anywhere inside the repo.

## Running

```bash
uv venv .venv && source .venv/bin/activate
uv pip install -r requirements.txt
jupyter lab
```

Notebooks size their training runs by device: on a GPU they use the upstream defaults, on CPU they use
smaller settings (fewer steps, a smaller dataset slice) so they finish in minutes. Weights & Biases
logging is disabled by default (`WANDB_MODE=disabled`).

## Status

See [PROGRESS.md](PROGRESS.md).
