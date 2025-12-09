---
layout: post
title: Handedness weighed sub-charges
category: local_charges
---
The handedness weighed sub-charges are phase-singularities in the left- and right-handed electric field components ($E_\pm = E_x \pm iE_y$).
They are defined as [[1]](https://doi.org/10.1103/PhysRevLett.125.053902)



$$q_\pm = \frac{1}{2\pi}\oint_\mathcal{C} d\mathbf{k}\cdot \nabla \phi_\pm (\mathbf{k})$$



where $\phi_\pm(\mathbf{k}) = \text{arg}\left(E_x(\mathbf{k}) \pm iE_y(\mathbf{k})\right)$

They are connected to the [BIC topological charge]({{ site.baseurl }}{% link _local_charges/bic_charge.md %}) as

$$q = \frac{q_- - q_+}{2}$$

At high-symmetry-points of the Brillouin-zone, the sub-charges are connected to the character of the irreducible representation of the mode [[2]](https://doi.org/10.1103/PhysRevLett.129.173901), [[3]](https://urn.fi/URN:ISBN:978-952-64-2676-1)



$$q_\pm = \mp1 - \frac{n}{2\pi}\text{arg}(\chi_{IR}) + m \cdot n$$



Each $q_\pm$ can be shown to correspond to a [Pancharatnam-Berry phase]({{ site.baseurl }}{% link _curvatures/pbphase.md %}) of $-\pi$ [[3]](https://urn.fi/URN:ISBN:978-952-64-2676-1).
As such, the sum of these charges gives the [Chern number]({{ site.baseurl }}{% link _global_charges/chern_number.md %}).





## Connected quantities

| Quantity | connection |
| --- | --- |
| [Pancharatnam-Berry phase]({{ site.baseurl }}{% link _curvatures/pbphase.md %}) | $$\gamma = -\pi(q_- + q_+)$$ |
| [Chern number]({{ site.baseurl }}{% link _global_charges/chern_number.md %}) | $$C_n = \frac{1}{2\pi}\sum_i q_-(\mathbf{k_i}) + q_+(\mathbf{k_i})$$ |
| [BIC topological charge]({{ site.baseurl }}{% link _local_charges/bic_charge.md %}) | $$q = \frac{q_- - q_+}{2}$$ |



### Citations
[[1] https://doi.org/10.1103/PhysRevLett.125.053902](https://doi.org/10.1103/PhysRevLett.125.053902)

[[2] https://doi.org/10.1103/PhysRevLett.129.173901](https://doi.org/10.1103/PhysRevLett.129.173901)

[[3] https://urn.fi/URN:ISBN:978-952-64-2676-1](https://urn.fi/URN:ISBN:978-952-64-2676-1)


