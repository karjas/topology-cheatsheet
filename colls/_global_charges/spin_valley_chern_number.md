---
layout: post
title: Spin-Valley Chern number
category: global_charges
---

In systems with both Valley- and spin degrees of freedom, the [Chern number]({{ site.baseurl }}{% link _global_charges/chern_number.md %}) can be broken down to four independent spin-valley chern numbers [[1]](https://doi.org/10.1103/PhysRevB.88.161406)



$$C_{s_z}^{\eta} = \frac{\eta}{2}\text{sgn}(\Delta^\eta_{s_z}), \quad \eta = K/K',\quad s_z = \uparrow/\downarrow$$



and $$\Delta_{s_z}^\eta$$ is the associated splitting term in the Hamiltonian of [[1]](https://doi.org/10.1103/PhysRevB.88.161406).
These quantities can then be used for calculating the [Chern number]({{ site.baseurl }}{% link _global_charges/chern_number.md %}), [Spin Chern number]({{ site.baseurl }}{% link _global_charges/spin_chern_number.md %}) and [Valley Chern number]({{ site.baseurl }}{% link _global_charges/valley_chern.md %}).

The Spin-valley Chern number of the band is given by



$$C_{sv} = \frac{1}{2}(C_\uparrow^K - C_\uparrow^{K'} - C_\downarrow^K + C_\downarrow^{K'})$$






## Connected quantities

| Quantity | connection |
| --- | --- |
| [Chern number]({{ site.baseurl }}{% link _global_charges/chern_number.md %}) | $$C_n = C_\uparrow^{K} + C_\uparrow^{K'} + C_\downarrow^{K} + C_\downarrow^{K'}$$ |
| [Spin Chern number]({{ site.baseurl }}{% link _global_charges/spin_chern_number.md %}) | $$C_s = \frac{1}{2}(C_\uparrow^{K} + C_\uparrow^{K'} - C_\downarrow^{K} - C_\downarrow^{K'})$$ |
| [Valley Chern number]({{ site.baseurl }}{% link _global_charges/valley_chern.md %}) | $$C_v = C_\downarrow^K + C_\uparrow^K - C_\downarrow^{K'} - C_\uparrow^{K'}$$ |



### Citations
[[1] https://doi.org/10.1103/PhysRevB.88.161406](https://doi.org/10.1103/PhysRevB.88.161406)


