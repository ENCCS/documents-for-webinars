import math
import numpy as np
import numba

numba.config.CUDA_ENABLE_MINOR_VERSION_COMPATIBILITY = True


# a simple version without using numba
def func_cpu(x, y):
    return math.pow(x, 3.0) + 4 * math.sin(y)


@numba.vectorize([numba.float64(numba.float64, numba.float64)], target="cpu")
def func_numba_cpu(x, y):
    return math.pow(x, 3.0) + 4 * math.sin(y)


@numba.vectorize([numba.float64(numba.float64, numba.float64)], target="cuda")
def func_numba_gpu(x, y):
    return math.pow(x, 3.0) + 4 * math.sin(y)


def test_cpu_gpu_equal():
    N = 100
    mx = np.random.rand(N)
    numpy_result = np.empty_like(mx)

    for i in range(100):
        numpy_result[i] = func_cpu(mx[i], mx[i])

    cpu_result = func_numba_cpu(mx, mx)
    gpu_result = func_numba_gpu(mx, mx)

    np.testing.assert_allclose(cpu_result, gpu_result)


# test_cpu_gpu_equal()
