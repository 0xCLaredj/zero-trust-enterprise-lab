# Public and private report editions

[Read the public PDF](rapport_chouaib_zero_trust.pdf). This portfolio edition is synchronized with the October 9 audited report and builds without external image assets. It retains evidence captions and the technical narrative while replacing private screenshots with explicit omission notes. Per-device Tailscale addresses and private workspace evidence paths are removed. Its evidence appendix points to the text summaries included under `../../evidence/`.

The public edition records the scope freeze and the unresolved Windows split-DNS/domain-discovery and shared-router SNAT limitations. It distinguishes user-reported VM shutdown from independently verified cloud state and does not claim zero residual cost. It is a technical portfolio report, not the full visual jury dossier.

The private academic edition remains in the workspace `rapport-chouaib/` directory. Its source retains the private capture macro and should only be built there, where the approved image assets resolve. Do not copy its screenshots or private evidence paths into this repository without separate review.

Build this public edition from this directory with three passes:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error rapport_chouaib_zero_trust.tex
pdflatex -interaction=nonstopmode -halt-on-error rapport_chouaib_zero_trust.tex
pdflatex -interaction=nonstopmode -halt-on-error rapport_chouaib_zero_trust.tex
```

A standard LaTeX installation with the declared packages is required. The cleaned repository application remains a portfolio adaptation, not an exact export of the deployed application. Building the PDF does not publish the repository or imply publication clearance for other files.
