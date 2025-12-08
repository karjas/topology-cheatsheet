---
layout: post
title: Berry Curvature
category: curvatures
---
Berry curvature measures the winding of eigenfunctions [[1]](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.91.015006)



$$\mathcal{B}_n(\mathbf{k}) = \nabla \times \mathcal{A}_n(\mathbf{k})$$



Berry curvature has the following symmetry properties:

| Symm | Behaviour |
| --- | --- |
| TRS | $\hat T \mathcal{B}_n(\mathbf{k}) = -\mathcal{B}_n(-\mathbf{k})$ |
| Inversion | $\hat I \mathcal{B}_n(\mathbf{k}) = \mathcal{B}_n(-\mathbf{k})$|
| Rotation | $\hat R \mathcal{B}_n(\mathbf{k}) = \mathcal{B}_n(\hat R^{-1}\mathbf{k})$|
| Reflection | $\hat \sigma \mathcal{B}_n(\mathbf{k}) = -\mathcal{B}_n(\hat \sigma^{-1}\mathbf{k})$|



## Connected quantities

| Quantity | connection |
| --- | --- |
| [Berry Connection]({{ site.baseurl }}{% link _curvatures/berry_connection.md %}) | $$\mathcal{A}_n(\mathbf{k}) = i\bra{ u_n(\mathbf{k})}\nabla_\mathbf{k}\ket{u_n(\mathbf{k})}$$ |
| [Chern number]({{ site.baseurl }}{% link _global_charges/Chern_number.md %}) | $$C_n = \frac{1}{2\pi}\int_{BZ} d\mathbf{k} \mathcal{B_n}(\mathbf{k})$$ |


### Alternative symbols

| Symbol | Works |
| --- | --- |
| $\Omega(\mathbf{k})$ | [[1]](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.91.015006) |


### Citations
[[1] https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.91.015006](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.91.015006)