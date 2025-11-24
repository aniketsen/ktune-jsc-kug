import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

ARCHS = ["epyc7742"]
RANKS = [1, 2, 3, 4, 5, 6]
KERNELS = ["copy", "scale", "add", "triad"]
POWERS = {1: 4, 2: 4, 3: 3, 4: 4}

ARCH = "epyc7742"
L2 = 16e6  # 16 MB
L3 = 512e6  # 512 MB
# of = matplotlib.backends.backend_pdf.PdfPages(f'stream_benchmark_{ARCH}_all_ranks_untuned.pdf')
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
for KERNEL in KERNELS:
  ax = axs.flatten()[KERNELS.index(KERNEL)]
  nviews = {"copy":2, "scale":2, "add":3, "triad":3}
  for rank in RANKS:
    dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label=f'rank {rank}')
  ax.axvline(L2*1e-9, color='red', linestyle=':')
  ax.axvline(L3*1e-9, color='red', linestyle=':')
  ax.grid(True, linestyle='--', linewidth=0.5)
  ax.legend(loc='best')
  ax.set_xlabel('Working Size (GB)')
  ax.set_ylabel('Bandwidth (GB/s)')
  ax.set_xscale('log')
  ax.set_title(f'{ARCH} nt128 {KERNEL} Untuned')
plt.tight_layout()
plt.savefig(f'stream_benchmark_{ARCH}_all_ranks_untuned.png', dpi=300)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
for KERNEL in KERNELS:
  ax = axs.flatten()[KERNELS.index(KERNEL)]
  nviews = {"copy":2, "scale":2, "add":3, "triad":3}
  for rank in RANKS:
    dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label=f'rank {rank}')
  ax.axvline(L2*1e-9, color='red', linestyle=':')
  ax.axvline(L3*1e-9, color='red', linestyle=':')
  ax.set_xlim(0.1, 12)
  ax.set_ylim(0, 300)
  ax.grid(True, linestyle='--', linewidth=0.5)
  ax.legend(loc='best')
  ax.set_xlabel('Working Size (GB)')
  ax.set_ylabel('Bandwidth (GB/s)')
  ax.set_xscale('log')
  ax.set_title(f'{ARCH} nt128 {KERNEL} Untuned')
plt.tight_layout()
plt.savefig(f'stream_benchmark_{ARCH}_all_ranks_untuned_zoomed.png', dpi=300)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
rank = 3
for KERNEL in KERNELS:
  ax = axs.flatten()[KERNELS.index(KERNEL)]
  nviews = {"copy":2, "scale":2, "add":3, "triad":3}
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label='Tuned')
  ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label='Untuned')
  ax.axvline(L2*1e-9, color='red', linestyle=':')
  ax.axvline(L3*1e-9, color='red', linestyle=':')
  ax.grid(True, linestyle='--', linewidth=0.5)
  ax.legend()
  ax.set_xlabel('Working Size (GB)')
  ax.set_ylabel('Bandwidth (GB/s)')
  ax.set_xscale('log')
  ax.set_title(f'{ARCH} nt128 rank {rank} {KERNEL}')
  rank += 1
plt.tight_layout()
plt.savefig(f'stream_benchmark_{ARCH}_tuned_vs_untuned.png', dpi=300)

fig, axs = plt.subplots(1, 2, figsize=(12, 4))
KERNEL = "add"
ax = axs[0]
nviews = {"copy":2, "scale":2, "add":3, "triad":3}
for rank in RANKS:
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label=f'rank {rank}')
ax.axvline(L2*1e-9, color='red', linestyle=':')
ax.axvline(L3*1e-9, color='red', linestyle=':')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend(loc='best')
ax.set_xlabel('Working Size (GB)')
ax.set_ylabel('Bandwidth (GB/s)')
ax.set_xscale('log')
ax.set_title(f'{ARCH} nt128 {KERNEL} Tuned')
ax = axs[1]
for rank in RANKS:
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label=f'rank {rank}')
ax.axvline(L2*1e-9, color='red', linestyle=':')
ax.axvline(L3*1e-9, color='red', linestyle=':')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_xlim(0.1, 12)
ax.set_ylim(0, 300)
ax.legend(loc='best')
ax.set_xlabel('Working Size (GB)')
ax.set_ylabel('Bandwidth (GB/s)')
ax.set_xscale('log')
ax.set_title(f'{ARCH} nt128 {KERNEL} Tuned')
plt.tight_layout()
plt.savefig(f'stream_benchmark_{ARCH}_tuned_all_ranks_add.png', dpi=300)


ARCH = "a100"
KERNEL = "add"
RANKS = [2, 3, 4]

fig, axs = plt.subplots(1, 2, figsize=(12, 8))
nviews = {"copy":2, "scale":2, "add":3, "triad":3}
ax = axs[0]
for rank in RANKS:
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label=f'rank {rank} Tuned')
  ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label=f'rank {rank} Untuned')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend(loc='best')
ax.set_xlabel('Working Size (GB)')
ax.set_ylabel('Bandwidth (GB/s)')
ax.set_xscale('log')
ax.set_title(f'{ARCH} {KERNEL}')
ax = axs[1]
ARCH = "mi250"
for rank in RANKS:
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/lumi/stream/stream_benchmark_{KERNEL}_{ARCH}_nt6_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/lumi/stream/stream_benchmark_{KERNEL}_{ARCH}_nt6_rank{rank}_untuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label=f'rank {rank} Tuned')
  ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label=f'rank {rank} Untuned')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.legend(loc='best')
ax.set_xlabel('Working Size (GB)')
ax.set_ylabel('Bandwidth (GB/s)')
ax.set_xscale('log')
ax.set_title(f'{ARCH} {KERNEL}')
plt.tight_layout()
plt.savefig(f'stream_benchmark_gpu_all_ranks_add.png', dpi=300)

fig, axs = plt.subplots(1, 2, figsize=(12, 8))
nviews = {"copy":2, "scale":2, "add":3, "triad":3}
ARCH = "a100"
ax = axs[0]
for rank in RANKS:
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label=f'rank {rank} Tuned')
  ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label=f'rank {rank} Untuned')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_xlim(0.1, 12)
ax.set_ylim(850, 1500)
ax.legend(loc='best')
ax.set_xlabel('Working Size (GB)')
ax.set_ylabel('Bandwidth (GB/s)')
ax.set_xscale('log')
ax.set_title(f'{ARCH} {KERNEL}')
ax = axs[1]
ARCH = "mi250"
for rank in RANKS:
  dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/lumi/stream/stream_benchmark_{KERNEL}_{ARCH}_nt6_rank{rank}_tuned.dat', delimiter=',', dtype=float)
  dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/lumi/stream/stream_benchmark_{KERNEL}_{ARCH}_nt6_rank{rank}_untuned.dat', delimiter=',', dtype=float)
  ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label=f'rank {rank} Tuned')
  ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label=f'rank {rank} Untuned')
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_xlim(0.1, 10)
ax.set_ylim(650, 1400)
ax.legend(loc='best')
ax.set_xlabel('Working Size (GB)')
ax.set_ylabel('Bandwidth (GB/s)')
ax.set_xscale('log')
ax.set_title(f'{ARCH} {KERNEL}')
plt.tight_layout()
plt.savefig(f'stream_benchmark_gpu_all_ranks_add_zoomed.png', dpi=300)

RANKS = [2, 3, 4]

NS = [3, 6]
KS = [3, 3]
MS = [3, 4]

ARCH = "a100"

pi = 0
fig, axs = plt.subplots(2, 3, figsize=(10, 8))
for ii in range(2):
  for rank in RANKS:
    N = NS[ii]
    K = KS[ii]
    M = MS[ii]
    dat_AoS = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/mm-AoS/mm_AoS_N{N}K{K}M{M}_{ARCH}_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    dat_views = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/mm-views/mm_views_N{N}K{K}M{M}_{ARCH}_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    ax = axs.flatten()[pi]
    ax.plot(dat_AoS[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_AoS[:,1], '^--', label='AoS Untuned')
    ax.plot(dat_views[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_views[:,1], 'v--', label='Views Untuned')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_xlabel('Working Size (GB)')
    ax.set_ylabel('Bandwidth (GB/s)')
    ax.set_xscale('log')
    ax.set_title(f'{ARCH} rank {rank} N{N}K{K}M{M}')
    pi += 1
    plt.tight_layout()
plt.savefig(f'mm_benchmark_{ARCH}_AoS_vs_Views_untuned.png', dpi=300)

pi = 0
fig, axs = plt.subplots(2, 3, figsize=(10, 8))
for ii in range(2):
  for rank in RANKS:
    N = NS[ii]
    K = KS[ii]
    M = MS[ii]
    dat_AoS_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/mm-AoS/mm_AoS_N{N}K{K}M{M}_{ARCH}_rank{rank}_tuned.dat', delimiter=',', dtype=float)
    dat_AoS_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/mm-AoS/mm_AoS_N{N}K{K}M{M}_{ARCH}_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    dat_views_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/mm-views/mm_views_N{N}K{K}M{M}_{ARCH}_rank{rank}_tuned.dat', delimiter=',', dtype=float)
    dat_views_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/mm-views/mm_views_N{N}K{K}M{M}_{ARCH}_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    ax = axs.flatten()[pi]
    ax.plot(dat_AoS_tuned[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_AoS_tuned[:,1], '^--', label='AoS Tuned')
    ax.plot(dat_AoS_untuned[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_AoS_untuned[:,1], 'x--', label='AoS Untuned')
    ax.plot(dat_views_tuned[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_views_tuned[:,1], '^--', label='Views Tuned')
    ax.plot(dat_views_untuned[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_views_untuned[:,1], 'x--', label='Views Untuned')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_xlabel('Working Size (GB)')
    ax.set_ylabel('Bandwidth (GB/s)')
    ax.set_xscale('log')
    ax.set_title(f'{ARCH} rank {rank} N{N}K{K}M{M}')
    pi += 1
    plt.tight_layout()
plt.savefig(f'mm_benchmark_{ARCH}_AoS_vs_Views_tuned.png', dpi=300)

ARCH = "mi250"
pi = 0
fig, axs = plt.subplots(2, 3, figsize=(10, 8))
for ii in range(2):
  for rank in RANKS:
    N = NS[ii]
    K = KS[ii]
    M = MS[ii]
    dat_AoS = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/lumi/mm-AoS/mm_AoS_N{N}M{M}K{K}_{ARCH}_rank{rank}_tuned.dat', delimiter=',', dtype=float)
    dat_views = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/lumi/mm-AoS/mm_AoS_N{N}M{M}K{K}_{ARCH}_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    ax = axs.flatten()[pi]
    ax.plot(dat_AoS[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_AoS[:,1], '^--', label='AoS Tuned')
    ax.plot(dat_views[:,0]**rank*(N*K+K*M+N*M)*8*1e-9, dat_views[:,1], 'x--', label='AoS Untuned')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    ax.set_xlabel('Working Size (GB)')
    ax.set_ylabel('Bandwidth (GB/s)')
    ax.set_xscale('log')
    ax.set_title(f'{ARCH} rank {rank} N{N}K{K}M{M}')
    pi += 1
    plt.tight_layout()
plt.savefig(f'mm_benchmark_{ARCH}_AoS_tuned_vs_untuned.png', dpi=300)

# for ARCH in ARCHS:
#   of = matplotlib.backends.backend_pdf.PdfPages(f'stream_benchmark_{ARCH}_comparison.pdf')
#   for rank in RANKS:
#     fig, axs = plt.subplots(2, 2, figsize=(10, 8))
#     for KERNEL in KERNELS:
#       dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
#       dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
#       nviews = {"copy":2, "scale":2, "add":3, "triad":3}
#       ax = axs.flatten()[KERNELS.index(KERNEL)]
#       ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label='Tuned')
#       ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'x--', label='Untuned')
#       ax.grid(True, linestyle='--', linewidth=0.5)
#       ax.legend()
#       ax.set_xlabel('Array Size (GB)')
#       ax.set_ylabel('Bandwidth (GB/s)')
#       ax.set_xscale('log')
#       ax.set_title(f'{ARCH} R{rank} {KERNEL}')
#     plt.tight_layout()
#     of.savefig(fig)
#   of.close()

