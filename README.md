# Implement Digit Classification with Support Vector Machine (SVM)


---

## Datasets

* The MNIST database of handwritten digits: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

---

## Requirements

* `libsvm`: [https://github.com/cjlin1/libsvm](https://github.com/cjlin1/libsvm)
* `scipy.io` from `scipy`
* `numpy`
* `matplotlib`

---

## Testing Environment  

* sysname: `Linux`  
* release: `4.15.0-45-generic`  
* machine: `x86_64`  
* python: `3.6.7`

---

## Results

* [Linear SVM](results/Linear_Results.md)

* [RBF SVM (Radial Basis Function)](results/RBF_Results.md)

---

## How to reproduce the results

1. Clone the `libsvm` repository: 

```
git clone https://github.com/cjlin1/libsvm.git
```

2. Clone my repository:

```
git clone 
```

3. Move all my codes into directory `python` of `libsvm`

```
mv xxx/* libsvm/python/
```

4. Follow instructions of README in the libsvm. For linux OS, in the `libsvm/python`:

```
make
```

5. Now, you can execute the `run_linear_svm.py` and `run_rbf_svm.py`:

```
python run_linear_svm.py
python run_rbf_svm.py
```