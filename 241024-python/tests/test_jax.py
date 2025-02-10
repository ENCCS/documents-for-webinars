import numpy as np
import jax.numpy as jnp
from jax import vmap, random, jit


key = random.key(1701)
key1, key2 = random.split(key)
mat = random.normal(key1, (150, 100))


def apply_matrix(x):
    return jnp.dot(mat, x)


def naively_batched_apply_matrix(v_batched):
    return jnp.stack([apply_matrix(v) for v in v_batched])


@jit
def vmap_batched_apply_matrix(batched_x):
    return vmap(apply_matrix)(batched_x)


def test_equal():
    batched_x = random.normal(key2, (10, 100))
    np.testing.assert_allclose(
        naively_batched_apply_matrix(batched_x),
        vmap_batched_apply_matrix(batched_x),
        atol=1e-4,
        rtol=1e-4,
    )
