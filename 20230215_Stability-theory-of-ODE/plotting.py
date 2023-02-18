import numpy as np
import matplotlib.pyplot as plt


def plot_matrix(A, title:str):
    A = np.matrix(A)
    fig, ax = plt.subplots(1,2, figsize=(10,5))

    # Streamplot
    x2,x1 = np.mgrid[-10:10, -10:10]
    x_flat = np.matrix([x1.flatten(), x2.flatten()])
    x1_dot = A[0,:] @ x_flat
    x2_dot = A[1,:] @ x_flat

    ax[0].streamplot(x1, x2, x1_dot.reshape(x1.shape), x2_dot.reshape(x2.shape), density=1)
    ax[0].set_title(title)
    evs = np.linalg.eig(A)[0]

    # Eigenvalues
    ax[1].set_title(f"Eigenvalues: $\lambda_1=${evs[0]}   $\lambda_2=${evs[1]}")
    ax[1].set_xlabel("Re", loc="right")
    ax[1].set_ylabel("Im", loc="top")
    ax[1].spines['top'].set_color('none')
    ax[1].spines['right'].set_color('none')
    ax[1].xaxis.set_ticks_position('bottom')
    ax[1].spines['bottom'].set_position(('data',0))
    ax[1].yaxis.set_ticks_position('left')
    ax[1].spines['left'].set_position(('data',0))

    ax[1].scatter([ev.real for ev in evs], [ev.imag for ev in evs])
    ax[1].set_xlim((
        min([ev.real for ev in evs] + [0])-1,
        max([ev.real for ev in evs] + [0])+1,
    ))
    plt.show()