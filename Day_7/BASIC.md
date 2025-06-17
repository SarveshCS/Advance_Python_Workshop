# Day 7

## Libraries in python

- Numpy
- Pandas
- MatPlotLib
- Seaborn
- Plotly
- SciPy

## File, package, module, library

> File -> file
>
> 2+ Files -> module -> (in a folder wrapped in another code) -> package (init file) -> library

## Numpy

It stands for numeric python.

- Package for scientific computing in python.
- Numoy is library thatprovides n-dimensionall array object.
- Fast operations on arrays including logical, shape manupulation, sorting, selecting, discrete mathametics, fourier tranforms, basc linear alzebra, stastical operation, random simulation and many more.

### Reshaping

- As long as element required for reshaping are equal in both shape.

### Resizing

It is used to create a new array with a specific shape.
If the new array is larger thanthe original array than the new array is filled with repeaded copies of original array.

> Difference between resize and reshape
>
> `ndarray.resize(row, column)` does not return but `numpy.resize(arr, (row, column))` does return the resized array
>
> where as reshape does return.

## Attributes in numpy

- `ndim`- Dimension of the array
- `shape` - Order of the matrix
- `nbytes` - Number of bytes occupied by an array
- `itemsize` - Bytes occupied by each element of the array
- `dtype` - Gives the type of element

## Funcitiosn to create common matrices

`np.zeros((3, 4), dtype='int16')`: 3x4 matrix of zeros (integers)
`np.ones((3, 4), dtype='int16')`: 3x4 matrix of ones (integers)
`np.full((3, 4), 5)`: 3x4 matrix filled with 5
`np.full((3, 4), np.nan)`: 3x4 matrix filled with NaN
`np.diag([10, 20, 30, 40, 50])`: Diagonal matrix with given values
`np.eye(5, dtype='int16')`: 5x5 identity matrix (integers)

## Array functions

- `flatten`, `ravel`
