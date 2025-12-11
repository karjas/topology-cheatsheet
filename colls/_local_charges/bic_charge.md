---
layout: post
title: BIC topological charge
category: local_charges
---
The topological charge $q$ is the winding number of the field polarisation in momentum space



$$q = \frac{1}{2\pi}\oint_{\mathcal{C}} d\mathbf{k}\cdot \nabla \phi(\mathbf{k})$$



where $\phi(\mathbf{k}) = \frac{1}{2}\arctan\left(\frac{S_2(\mathbf{k})}{S_1(\mathbf{k})}\right)$, is the orientation of the electric field polaristaion.
When mapped on Stokes sphere, $q$ measures how many times the polarisation vector rotates around the $S_3$ axis on a closed path in momentum space.

$q$ can be decomposed into [Handedness weighed sub-charges]({{ site.baseurl }}{% link _local_charges/handedness_weighed_sub_charges.md %}), which correspond to phase-singularities in the left- and right-handed field components



$$q = \frac{q_- - q_+}{2}$$



When considering the polarisation vortices over all possible values of $\mathbf{k}$ (torus for periodic systems, sphere for finite), with the [Hairy ball theorem](https://en.wikipedia.org/wiki/Hairy_ball_theorem) one can connect the sum of $q$ to the [Euler Characteristic]({{ site.baseurl }}{% link _global_charges/euler_characteristic.md %}).




## Connected quantities

| Quantity | connection |
| --- | --- |
| [Euler Characteristic]({{ site.baseurl }}{% link _global_charges/euler_characteristic.md %}) | $$\chi = \sum_{i} q(\mathbf{k}_i)$$ |
| [Handedness weighed sub-charges]({{ site.baseurl }}{% link _local_charges/handedness_weighed_sub_charges.md %}) | $$q = \frac{q_- - q_+}{2}$$ |


