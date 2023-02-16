import matplotlib.pyplot as plt
import numpy as np


def plot_1D_mesh(node_list: np.ndarray, element_list: list):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    for idx, node in enumerate(node_list):
        ax[0].scatter(node, 0)
        ax[0].annotate(idx, (node, 0))
        ax[0].set_title("Nodes")

    for idx, element in enumerate(element_list):
        ax[1].plot(node_list[element], [0,0], ".-")
        ax[1].annotate(idx, (np.mean(node_list[element]), 0))
        ax[1].set_title("Elements")

    plt.xlabel("$x$")
    plt.show()


def plot_2D_mesh(node_list: np.ndarray, element_list: list) -> None:
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    for idx, node in enumerate(node_list):
        ax[0].scatter(*node)
        ax[1].scatter(*node, c="black")
        ax[0].annotate(idx, node)
        ax[0].set_title("Nodes")
        ax[0].set_xlabel("$x$")
        ax[0].set_ylabel("$y$")

    for idx, element in enumerate(element_list):
        ax[1].plot(node_list[element + element[:1], 0], node_list[element + element[:1], 1], alpha=0.5)
        ax[1].annotate(idx, np.mean(node_list[element], axis=0))
        ax[1].set_title("Elements")
        ax[1].set_xlabel("$x$")
        ax[1].set_ylabel("$y$")

    plt.show()


def plot_1D_results(node_list, element_list, u, f, sigma):
    idx_sorted = np.argsort(node_list)
    fig, ax = plt.subplots(3, 1, figsize=(10, 10))

    ax[0].plot(node_list[idx_sorted], u[idx_sorted], ".-")
    ax[0].set_title("Displacement $u$")

    ax[1].plot(node_list[idx_sorted], f[idx_sorted], ".-")
    ax[1].set_title("Force $f$")

    x_m_e = np.mean([node_list[element] for element in element_list], axis=1)
    idx_sorted = np.argsort(x_m_e)
    ax[2].plot(x_m_e[idx_sorted], sigma[idx_sorted], ".-")
    ax[2].set_title(r"Stress $\sigma$")
    ax[2].set_xlim((min(node_list), max(node_list)))
    plt.show()


def plot_cross_section_area(A, l):
    xpts = np.linspace(0,l,1000)
    plt.plot(xpts, A(xpts))
    plt.ylim((0,max(A(xpts))))
    plt.xlabel("$x$")
    plt.ylabel("Area $A(x)$")
    plt.title("Cross Sectional Area")
    plt.show()
