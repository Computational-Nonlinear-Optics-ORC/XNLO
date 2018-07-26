import numpy as np
from matplotlib import pyplot as plt

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:17:18 2017

@author: sms1n16
"""


def get_number_of_lines(file):
    with open(file) as input_file:
        n_lines = 0
        n_data_per_line = 0
        for line in input_file:
            line = line.strip()
            n_data_per_line = 0
            for number in line.split():
                n_data_per_line += 1
            n_lines += 1
        return n_lines, n_data_per_line


def get_data(file, n_lines, n_data_per_line):
    with open(file) as input_file:
        data = np.zeros([n_data_per_line, n_lines])
        i = 0
        for line in input_file:
            line = line.strip()
            j = 0
            for number in line.split():
                data[j, i] = number
                j += 1
            i += 1
        return data


def plot(data, n_plots,
         title, axis_titles,
         xlim, ylim,
         figsize=(12, 4), dpi=80):
    fig = plt.figure(figsize=figsize, dpi=dpi)
    if n_plots == 1:
        ax1 = fig.add_subplot(1, 1, 1)
        ax1.plot(data[0])
        ax1.set_xlim([xlim[0], xlim[1]])
        ax1.set_ylim([ylim[0], ylim[1]])
        ax1.set_xlabel(axis_titles[0])
        ax1.set_ylabel(axis_titles[1])
        plt.title(title)
        plt.tight_layout()
    else:
        for i in range(n_plots):
            ax1 = fig.add_subplot(1, n_plots, i+1)
            ax1.plot(data[i])
            ax1.set_xlim([xlim[i][0], xlim[i][1]])
            ax1.set_ylim([ylim[i][0], ylim[i][1]])
            ax1.set_xlabel(axis_titles[i][0])
            ax1.set_ylabel(axis_titles[i][1])
            plt.title(title[i])
            plt.tight_layout()
    plt.show()


def plot_w_2_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/w_2atoms.txt")
    print("Data per line: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    w_data = get_data("output/w_2atoms.txt", n_lines, n_data_per_line)

    n_plots = 1
    title = r"w_2atoms.txt"
    axis_titles = (r"Step", r"w")
    xlim = (0, n_lines)
    ylim = (np.amin(w_data)*1.05, np.amax(w_data)*1.05)
    figsize = (8, 5)
    dpi = 320
    plot(w_data, n_plots, title, axis_titles, xlim, ylim, figsize, dpi)


def plot_dipole_2_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/dipole_2atoms.txt")
    print("Number of atoms: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    dipole_data = get_data("output/dipole_2atoms.txt",
                           n_lines, n_data_per_line)

    for i in range(0, n_data_per_line, 2):
        n_plots = 2
        title = (r"dipole_2atoms.txt",
                 r"dipole_2atoms.txt")
        axis_titles = ((r"Step", r"dipole"), (r"Step", r"dipole"))
        xlim = ((0, n_lines), (0, n_lines))
        ylim = ((np.amin(dipole_data[0+i])*1.05,
                 np.amax(dipole_data[0+i])*1.05),
                (np.amin(dipole_data[1+i])*1.05,
                 np.amax(dipole_data[1+i])*1.05))
        figsize = (15, 7)
        dpi = 320
        plot(dipole_data[i:i+2], n_plots,
             title, axis_titles,
             xlim, ylim, figsize, dpi)


def plot_w_4_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/w_4atoms.txt")
    print("Data per line: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    w_data = get_data("output/w_4atoms.txt", n_lines, n_data_per_line)

    n_plots = 1
    title = r"w_4atoms.txt"
    axis_titles = (r"Step", r"w")
    xlim = (0, n_lines)
    ylim = (np.amin(w_data)*1.05, np.amax(w_data)*1.05)
    figsize = (8, 5)
    dpi = 320
    plot(w_data, n_plots, title, axis_titles, xlim, ylim, figsize, dpi)


def plot_dipole_4_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/dipole_4atoms.txt")
    print("Number of atoms: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    dipole_data = get_data("output/dipole_4atoms.txt",
                           n_lines, n_data_per_line)

    for i in range(0, n_data_per_line, 2):
        n_plots = 2
        title = (r"dipole_4atoms.txt",
                 r"dipole_4atoms.txt")
        axis_titles = ((r"Step", r"dipole"), (r"Step", r"dipole"))
        xlim = ((0, n_lines), (0, n_lines))
        ylim = ((np.amin(dipole_data[0+i])*1.05,
                 np.amax(dipole_data[0+i])*1.05),
                (np.amin(dipole_data[1+i])*1.05,
                 np.amax(dipole_data[1+i])*1.05))
        figsize = (15, 7)
        dpi = 320
        plot(dipole_data[i:i+2], n_plots,
             title, axis_titles,
             xlim, ylim, figsize, dpi)


def plot_w_6_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/w_6atoms.txt")
    print("Data per line: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    w_data = get_data("output/w_6atoms.txt", n_lines, n_data_per_line)

    n_plots = 1
    title = r"w_6atoms.txt"
    axis_titles = (r"Step", r"w")
    xlim = (0, n_lines)
    ylim = (np.amin(w_data)*1.05, np.amax(w_data)*1.05)
    figsize = (8, 5)
    dpi = 320
    plot(w_data, n_plots, title, axis_titles, xlim, ylim, figsize, dpi)


def plot_dipole_6_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/dipole_6atoms.txt")
    print("Number of atoms: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    dipole_data = get_data("output/dipole_6atoms.txt",
                           n_lines, n_data_per_line)

    for i in range(0, n_data_per_line, 2):
        n_plots = 2
        title = (r"dipole_6atoms.txt",
                 r"dipole_6atoms.txt")
        axis_titles = ((r"Step", r"dipole"), (r"Step", r"dipole"))
        xlim = ((0, n_lines), (0, n_lines))
        ylim = ((np.amin(dipole_data[0+i])*1.05,
                 np.amax(dipole_data[0+i])*1.05),
                (np.amin(dipole_data[1+i])*1.05,
                 np.amax(dipole_data[1+i])*1.05))
        figsize = (15, 7)
        dpi = 320
        plot(dipole_data[i:i+2], n_plots,
             title, axis_titles,
             xlim, ylim, figsize, dpi)


def plot_w_8_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/w_8atoms.txt")
    print("Data per line: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    w_data = get_data("output/w_8atoms.txt", n_lines, n_data_per_line)

    n_plots = 1
    title = r"w_8atoms.txt"
    axis_titles = (r"Step", r"w")
    xlim = (0, n_lines)
    ylim = (np.amin(w_data)*1.05, np.amax(w_data)*1.05)
    figsize = (8, 5)
    dpi = 320
    plot(w_data, n_plots, title, axis_titles, xlim, ylim, figsize, dpi)


def plot_dipole_8_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/dipole_8atoms.txt")
    print("Number of atoms: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    dipole_data = get_data("output/dipole_8atoms.txt",
                           n_lines, n_data_per_line)

    for i in range(0, n_data_per_line, 2):
        n_plots = 2
        title = (r"dipole_8atoms.txt",
                 r"dipole_8atoms.txt")
        axis_titles = ((r"Step", r"dipole"), (r"Step", r"dipole"))
        xlim = ((0, n_lines), (0, n_lines))
        ylim = ((np.amin(dipole_data[0+i])*1.05,
                 np.amax(dipole_data[0+i])*1.05),
                (np.amin(dipole_data[1+i])*1.05,
                 np.amax(dipole_data[1+i])*1.05))
        figsize = (15, 7)
        dpi = 160
        plot(dipole_data[i:i+2], n_plots,
             title, axis_titles,
             xlim, ylim, figsize, dpi)


def plot_w_10_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/w_10atoms.txt")
    print("Data per line: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    w_data = get_data("output/w_10atoms.txt", n_lines, n_data_per_line)

    n_plots = 1
    title = r"w_10atoms.txt"
    axis_titles = (r"Step", r"w")
    xlim = (0, n_lines)
    ylim = (np.amin(w_data)*1.05, np.amax(w_data)*1.05)
    figsize = (8, 5)
    dpi = 320
    plot(w_data, n_plots, title, axis_titles, xlim, ylim, figsize, dpi)


def plot_dipole_10_atoms():
    n_lines, n_data_per_line = get_number_of_lines("output/dipole_10atoms.txt")
    print("Number of atoms: {}, number of steps: {}".format(n_data_per_line,
          n_lines))
    dipole_data = get_data("output/dipole_10atoms.txt",
                           n_lines, n_data_per_line)

    for i in range(0, n_data_per_line, 2):
        n_plots = 2
        title = (r"dipole_10atoms.txt",
                 r"dipole_10atoms.txt")
        axis_titles = ((r"Step", r"dipole"), (r"Step", r"dipole"))
        xlim = ((0, n_lines), (0, n_lines))
        ylim = ((np.amin(dipole_data[0+i])*1.05,
                 np.amax(dipole_data[0+i])*1.05),
                (np.amin(dipole_data[1+i])*1.05,
                 np.amax(dipole_data[1+i])*1.05))
        figsize = (15, 7)
        dpi = 320
        plot(dipole_data[i:i+2], n_plots,
             title, axis_titles,
             xlim, ylim, figsize, dpi)

plot_w_2_atoms()
plot_dipole_2_atoms()
plot_w_4_atoms()
plot_dipole_4_atoms()
plot_w_6_atoms()
plot_dipole_6_atoms()
plot_w_8_atoms()
plot_dipole_8_atoms()
plot_w_10_atoms()
plot_dipole_10_atoms()
