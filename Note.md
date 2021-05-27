# Note for MCFS	

## Part: Mathematics Methods for Computer Science

#### lecture 1

Mathematically correctly is **not equal **to numerically sound. Instead of using '==' to judge the equivalence of two float point numbers,  use some tolerance.

In C++, we can use:

```cpp
numeric_limit<double>::epsilon
```

Sometimes if we don't need to do calculation very precisely, we can use binary to approximately denote float point number.

The float point is not spaced evenly at the axis.

![float_point_01](.\note images\float_point_01.png)

Bracketing:



The sources of error:

1. Round

2. Discretization 

3. Modeling

4. Input

Condition Number:

The ratio of frontward error and backward error.

**Well-conditioned**: small backward error will lead to small frontward error

For root-finding example, condition number 
$$
K = \frac{1}{|f'(x^*)|}
$$
For matrix, condition number 
$$
K=||A|\ ||A^{-1}||
$$
So Orthogonal matrix is **numerically stable**, for the reality that
$$
A^TA=A^{-1}A=I\rightarrow K=||A||\ ||A^T||=1
$$
Extremely careful implementation can be necessary:

A method to optimize the calculation of  L2 norm：

Original:

```cpp
double normSpuared = 0;
for(int i = 0; i < n; ++i){
	normSquared += x[i] * x[i];
}
return sqrt(normSquared);
```

Optimized:

```cpp
double maxElement = epsilon;
for(int i = 0; i < n; ++i){
	maxElement = max(maxElement, fabs[x[i]]);
}
for(int i = 0; i < n; ++i){
	double scaled = x[i] / maxElement;
	normSquared += scaled * scaled;
}
return sqrt(normSquared) * maxElement;
```

What about calculating the sum?

```cpp
for(int i =0; i<n; ++i)sum += x[i];
```

When calculating float point numbers, sum += x[i] may cause errors, for (a + b) - a -b is not necessarily numerically equal to zero. There are some errors.

Then we can use **Kahan Algorithm**:

The basic program for sum:

```cpp
for(int i = 0; i< n; ++i){
	_x = x[i] + error;
	t = sum + _x;
	error = (t - sum) - _x;
	sum = t;
}
```

#### lecture 2

For linear function Ax = b, we can use gaussian elimination algorithm to solve it, whose time complexity is **O(N^3)**. That means when N is very big, its performance would be awful. 

We can use **LU Factorization** to accelerate the solving process.
$$
Ax = b
$$

$$
\longrightarrow (M_k...M_2M_1)Ax=(M_k...M_2M_1)b
$$

$$
let\ U=(M_k...M_2M_1)A\ and\ L =M^{-1}_1M^{-1}_2...M^{-1}_k
$$

$$
\longrightarrow A=LU 
$$

Then the function has been split into two:
$$
LY=b\ and\ Ux=Y
$$
Solving each of them will cost **O(N^2)** time.

Sometimes when we transform the matrix A, dividing zeros or a very tiny number will occur, which will cause bad effects. We can solve this problem by pivoting, namely exchange two rows or two cols. In the view of matrix, namely multiply a matrix P (referring to permutation) on the left, or on the right. (PA or AP).

![LU_01](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\LU_01.png)

In this way, the A will become: A = LUP (A = PLU is also feasible).  

![LU_02](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\LU_02.png)

Hints: we can store matrix L and U into a singleton matrix. **Don't forget to parse it into two matrices!**

LU Factorization: 

![LU_03](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\LU_03.png)

#### lecture 3

**Linear Regression**

Non-linear functions can also serve as a basic function in a linear function, like fourier series.

To many interpolation or a not proper choice of basic functions will cause overfitting.

**Normal Equation**

What about m > n(Overdetermined problem)?

Find the least square:
$$
A\vec{x}\approx\vec{b}\Longleftrightarrow  \min_{\vec{x}} ||A\vec{x}-\vec{b}||_2\Longleftrightarrow A^TA\vec{x}=A^T\vec{b}
$$
proof: use derivative.

**Gram Matrix **
$$
A^TA\ is\ always\ symmtrical\ and\ semi-definite.
$$
**Tikhonov Regularization**

![regression_01](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\regression_01.png)

**Semi-Definite Matrix**
$$
\forall x\neq 0,\vec{x}^TB\vec{x}>0
$$

$$
\vec{x}^TA^TA\vec{x}\ is\ semi-definite
$$

$$
proof:\vec{x}^TA^TA\vec{x}=(A\vec{x})^TA\vec{x}=||A\vec{x}||_2^2\ge 0
$$

$$
if\ all\ column\ vectors\ of\ A\ is\ linearly\ dependent,\ \vec{x}^TA^TA\vec{x}\ is\ definite
$$

**Symmetric Positive Definite Matrix**
$$
C=\left[
 \begin{matrix}
   c_{11} & \vec{v}^T \\
   \vec{v} & \widetilde{C}\\
  \end{matrix}
  \right]=LL^T
$$

$$
Construct\ E=\left[ \begin{matrix}   1/\sqrt{c_{11}} & \vec{0}^T \\   \vec{r} & I_{(n-1)\times(n-1)}\\  \end{matrix}  \right]
$$

$$
ECE^T=\left[ \begin{matrix}  1 & 0 \\   0 & D\\  \end{matrix}  \right]
$$

$$
E_k...E_2E_1CE_1E_2...E_k=I
$$

So we got **Cholesky Factorization**
$$
C=LL^T
$$
![cholesky_01](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\cholesky_01.png)

![cholesky_02](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\cholesky_02.png)

In contrast with **LU Factorization**:

1. Store less information, only one lower triangular matrix L, while LU Factorization will need to store two different matrices L and U;
2. LU Factorization may not make full use of the attributions of original matrix, like symmetry.
3. Faster than LU Factorization.

**Storing Sparse Matrix**

Some system may use sparse matrix(exists a lot of zeros) to store information, the matrix should be compressed. 

Special matrix may performance better in calculation.(There exists special tricks for them.)

![banded](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\cyclic.png)

![banded](C:\Users\92304\PycharmProjects\mfcs_assignment\note images\banded.png)

#### lecture 5

**QR Factorization**

To solve M > N overdetermined problem. Use least square to fit.
$$
Ax=b(A\in \R^{m\times n},x\in \R^{n\times1},b\in \R^{m\times1})
$$
A can be decomposed into Q and R, where
$$
Q\in \R^{m\times n},R\in \R^{n\times n}
$$
Q is an orthogonal matrix and R is a upper triangular matrix.

QR Factorization can be done by **Gram-Schmidt Orthogonality** or **Householder Transform**

**Least square**
$$
minimize\ ||Ax-b||_2^2
$$
is **equivalent to**:
$$
solve\ A^TA=A^Tb
$$
By using QR Factorization,
$$
R^TQ^TQRx=R^TQ^Tb\rightarrow x=R^{-1}Q^Tb
$$
 
$$
Avoid\ calculating\ A^TA\ or\ (A^TA)^{-1}
$$

#### lecture 6

$$
\vec{x_i}\approx c\vec{v}
$$

$$
minimize\ \Sigma ||\vec{x_i}-proj_\vec{v}\vec{x_i}||_2^2
$$

$$
which\ is\ equivalent\ of\ maximize\ ||X^T\hat{v}||_2^2,\ such\ that\ ||\hat{v}||_2^2=1
$$

**Hermitian Matrix**
$$
\forall A\in C^{n\times n},\ A=\bar{A}^T=A^H
$$
**Matrix Inverse**

A vector can be transformed into a linear combination of the eigenvectors of Hermitian matrix.

A and B are similar matrices when 
$$
\exists T,s.t.A = T^{-1} BT
$$
#### lecture 7

**SVD Factorization**

