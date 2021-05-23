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
