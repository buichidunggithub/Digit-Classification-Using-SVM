# Digit Classification Using Support Vector Machine (SVM)

In this project, I implement digit classification using `LibSVM` libarary. 

## Datasets

* The MNIST database of handwritten digits: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

## Requirements

* `libsvm`: [https://github.com/cjlin1/libsvm](https://github.com/cjlin1/libsvm)
* `scipy.io` from `scipy`
* `numpy`
* `matplotlib`

## Testing Environment  

* sysname: `Linux`  
* release: `4.15.0-45-generic`  
* machine: `x86_64`  
* python: `3.6.7`

## Results

* [Linear SVM](results/Linear_Results.md)

* [RBF SVM (Radial Basis Function)](results/RBF_Results.md)


## How to reproduce the results

1. Clone the `libsvm` repository:

```
git clone https://github.com/cjlin1/libsvm.git
```

2. Clone my repository:

```
git clone https://github.com/lychengr3x/Digit-Classification-Using-SVM.git
```

3. Move all my codes into directory `python` of `libsvm`:

```
cp -r Digit-Classification-Using-SVM/src/* libsvm/python/
```

4. Follow instructions of README in the libsvm. For linux OS, go to the directory `libsvm/python`:

```
cd libsvm/python
make
```

* Note: If it does not work, go to the directory `libsvm`:
  
```
cd ..
make
```

1. Now, you can execute the `run_linear_svm.py` and `run_rbf_svm.py`:

```
python run_linear_svm.py
python run_rbf_svm.py
```