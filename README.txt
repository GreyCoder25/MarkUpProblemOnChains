# Generalized labelling on chains

## About

Demonstration of generalized labelling algorithm for text recognition task. Generalized labelling means that labelling
is performed for a set of objects, where notion of neighborhood is generalized, so every object can have arbitrary amount
of previous objects as neighbors. Algorithm is based on dynamic programming.

## Requirements

- PIL
- numpy
- matplotlib

## Result

Without noise:

![without_noise](./report/without_noise.png)

Noise 0.5:

![noise_05](./report/noise_05.png)

Noise 0.75:

![noise_075](./report/noise_075.png)

Noise 0.85:

![noise_085](./report/noise_085.png)

Noise 0.95:

![noise_095](./report/noise_095.png)

Noise 0.96:

![noise_096](./report/noise_096.png)


## How to install

$ git clone https://github.com/GreyCoder25/MarkUpProblemOnChains

## How to run

$ python main.py

String to recognize and noise are specified in line 32 of main.py.

