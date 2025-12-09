---
layout: post
title: Chern number
category: global_charges
---

[Berry Curvature]({{ site.baseurl }}{% link _curvatures/berry_curvature.md %}) integrated over the Brillouin zone yields the Chern number, a topological charge connected to uni-directional edge bands crossing the band-gap.[ozawa2019topological]



$$C_n = \frac{1}{2\pi}\int_{BZ} d\mathbf{k} \mathcal{B_n}(\mathbf{k})$$



Due to symmetry-properties of [Berry Curvature]({{ site.baseurl }}{% link _curvatures/berry_curvature.md %}), if TRS is present, $C_n = 0$.

In the electromagnetic far-field, the Chern number can be connected to the [Handedness weighed sub-charges]({{ site.baseurl }}{% link _local_charges/handedness_weighed_sub_charges.md %}).
Assuming, that there are paths of linear polarisation surrounding these singularities, we can find the Chern number as the sum



$$C_n = \frac{1}{2\pi}\sum_i q_-(\mathbf{k_i}) + q_+(\mathbf{k_i})$$





## Connected quantities

| Quantity | connection |
| --- | --- |
| [Berry Curvature]({{ site.baseurl }}{% link _curvatures/berry_curvature.md %}) | $$C_n = \frac{1}{2\pi}\int_{BZ} d\mathbf{k} \mathcal{B_n}(\mathbf{k})$$ |
| [Handedness weighed sub-charges]({{ site.baseurl }}{% link _local_charges/handedness_weighed_sub_charges.md %}) | $$C_n = \frac{1}{2\pi}\sum_i q_-(\mathbf{k_i}) + q_+(\mathbf{k_i})$$ |


