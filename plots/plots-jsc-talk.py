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
  nviews = {"copy":2, "scale":1, "add":2, "triad":3}
  for rank in RANKS:
    dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
    ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'v--', label=f'rank {rank}')
  ax.axvline(L2*1e-9, color='red', linestyle=':')
  ax.axvline(L3*1e-9, color='red', linestyle=':')
  ax.set_xlim(0.1, 12)
  ax.set_ylim(0, 300)
  ax.grid(True, which='both', linestyle='--', linewidth=0.5)
  ax.legend(loc='best')
  ax.set_xlabel('Working Size (GB)')
  ax.set_ylabel('Bandwidth (GB/s)')
  ax.set_xscale('log')
  ax.set_title(f'{ARCH} nt128 {KERNEL} Untuned')
plt.tight_layout()
plt.savefig(f'stream_benchmark_{ARCH}_all_ranks_untuned_zoomed.png', dpi=300)

# for ARCH in ARCHS:
#   of = matplotlib.backends.backend_pdf.PdfPages(f'stream_benchmark_{ARCH}_comparison.pdf')
#   for rank in RANKS:
#     fig, axs = plt.subplots(2, 2, figsize=(10, 8))
#     for KERNEL in KERNELS:
#       dat_tuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_tuned.dat', delimiter=',', dtype=float)
#       dat_untuned = np.genfromtxt(f'/home/sen/projects/ktune_benchmarks/jureca/stream/stream_benchmark_{KERNEL}_{ARCH}_nt128_rank{rank}_untuned.dat', delimiter=',', dtype=float)
#       nviews = {"copy":2, "scale":1, "add":2, "triad":3}
#       ax = axs.flatten()[KERNELS.index(KERNEL)]
#       ax.plot(dat_tuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_tuned[:,3], '^--', label='Tuned')
#       ax.plot(dat_untuned[:,0]**rank*8*1e-9*nviews[KERNEL], dat_untuned[:,3], 'v--', label='Untuned')
#       ax.grid(True, which='both', linestyle='--', linewidth=0.5)
#       ax.legend()
#       ax.set_xlabel('Array Size (GB)')
#       ax.set_ylabel('Bandwidth (GB/s)')
#       ax.set_xscale('log')
#       ax.set_title(f'{ARCH} R{rank} {KERNEL}')
#     plt.tight_layout()
#     of.savefig(fig)
#   of.close()

