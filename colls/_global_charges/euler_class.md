---
layout: post
title: Euler class
category: global_charges
---

Euler class is a topological invariant for two real bands [[1]](https://doi.org/10.1103/PhysRevX.9.021013), the presence of which is connected to degenerate band-crossings.
It is found by integrating the [Non-Abelian Berry curvature]({{ site.baseurl }}{% link _curvatures/euler_curvature.md %})



$$e_{12} = \frac{1}{2\pi}\oint_{BZ} d\mathbf{k}\cdot \mathbf{F}_{12}(\mathbf{k})$$



It can be connected to the winding-number of a 2D Hamiltonian $N_t$ as 



$$e_{12} = -\frac{1}{2}N_t$$



Alternatively, the Euler class can be evaluated for a patch $\mathcal{P}$ in momentum space [[2]](https://doi.org/10.48550/arXiv.2511.03894)



$$e_{n,n+1}(\mathcal{P}) = \frac{1}{2\pi}\left[\int_\mathcal{P} d\mathbf{k}\cdot \mathbf{F}_{n,n+1}(\mathbf{k}) - \oint_{\partial \mathcal{P}} d\mathbf{k}\cdot \mathcal{A}_{n,n+1}(\mathbf{k}) \right]$$






## Connected quantities

| Quantity | connection |
| --- | --- |
| [Non-Abelian Berry curvature]({{ site.baseurl }}{% link _curvatures/euler_curvature.md %}) | $$e_{12} = \frac{1}{2\pi}\oint_{BZ} d\mathbf{k}\cdot \mathbf{F}_{12}(\mathbf{k})$$ |


### Alternative symbols

| Symbol | Works |
| --- | --- |
| $\chi$ | [[2]](https://doi.org/10.48550/arXiv.2511.03894) |


### Citations
[[1] https://doi.org/10.1103/PhysRevX.9.021013](https://doi.org/10.1103/PhysRevX.9.021013)

[[2] https://doi.org/10.48550/arXiv.2511.03894](https://doi.org/10.48550/arXiv.2511.03894)


