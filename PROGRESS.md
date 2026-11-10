# Progress

Executed on a 4-CPU, no-GPU box. "Done" = all exercises filled in, notebook executed top to bottom with no
errors, and every test shipped with the notebook passes.

## Chapter 1 - Transformer interpretability

| Part | Notebook | Status |
|---|---|---|
| 1.1 | Transformer from Scratch | Done (training runs use CPU-sized settings) |
| 1.2 | Intro to Mech Interp | Done |
| 1.3.1 | Linear Probes | Blocked: needs `HF_TOKEN` (gated Llama 3.1 8B / 3.3 70B) and a GPU |
| 1.3.2 | Function Vectors & Model Steering | Blocked: needs `OPENAI_API_KEY` (and a GPU for the larger models) |
| 1.3.3 | Interpretability with SAEs | Partly runnable (GPT-2 small); Gemma-2b part needs `HF_TOKEN` and `OPENAI_API_KEY` for auto-interp |
| 1.3.4 | Activation Oracles | Blocked: needs `HF_TOKEN` and a GPU (8B models) |
| 1.4.1 | Indirect Object Identification | Next - GPT-2 small, CPU-feasible |
| 1.4.2 | SAE Circuits | Blocked: needs `HF_TOKEN` (Gemma) |
| 1.5.1 | Balanced Bracket Classifier | Next - CPU-feasible |
| 1.5.2 | Grokking & Modular Arithmetic | Next - CPU-feasible |
| 1.5.3 | OthelloGPT | Next - to check |
| 1.5.4 | Toy Models of Superposition & SAEs | Next - CPU-feasible |

## Chapter 3 - LLM evaluations

All five notebooks (3.1 to 3.5) call hosted LLMs through `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` or
`OPENROUTER_API_KEY`. Not started: no key is available in the build environment.

## Chapters 0, 2, 4

Not started.

## Notes

- `circuitsvis` comes from PyPI, which lacks the `attention_head_names` argument of ARENA's fork. Affected
  cells have that argument removed (it only labels heads).
- Executed notebooks are large (tens of MB) because plotly and CircuitsVis embed their JS in the outputs.
