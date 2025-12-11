---
layout: post
title: Valley Chern number
category: global_charges
---

Valley Chern numbers are found in $\mathbf{C}_3$-symmetric structures and are caused by the accumulation of [Berry Curvature]({{ site.baseurl }}{% link _curvatures/berry_curvature.md %}) at the $K,K'$ points of the Brillouin Zone.
A typical way of generating them is to start with a $\mathbf{C}_6$-symmetric structure and break inversion symmetry.
As Time-reversal symmetry is still present, the [Chern number]({{ site.baseurl }}{% link _global_charges/chern_number.md %}) of the band is zero.
However, due to broken inversion symmetry, the two valleys can carry opposite, non-trivial curvatures $$\mathcal{B}(\mathbf{k}_K) = -\mathcal{B}(-\mathbf{k}_K)= -\mathcal{B}(\mathbf{k}_{K'})$$.

The Valley Chern numbers are given by 

$$C_{K/K'} = \frac{1}{2\pi}\int_{K/K'} d\mathbf{k} \mathcal{B}(\mathbf{k})$$

The Valley-Chern number of the band is then taken as



$$C_v = C^K - C^{K'}$$



If the spin-operator commutes with the Hamiltonian, the Valley-Chern can be further broken down [[1]](https://doi.org/10.1103/PhysRevB.88.161406)



$$C_v = C_\downarrow^K + C_\uparrow^K - C_\downarrow^{K'} - C_\uparrow^{K'}$$





## Connected quantities

| Quantity | connection |
| --- | --- |
| [spin_valley_chern_number.md] | $$C_v = C_\downarrow^K + C_\uparrow^K - C_\downarrow^{K'} - C_\uparrow^{K'}$$ |



### Citations
[[1] https://doi.org/10.1103/PhysRevB.88.161406](https://doi.org/10.1103/PhysRevB.88.161406)


