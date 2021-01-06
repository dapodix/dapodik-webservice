from .pengguna import pengguna_export
from .peserta_didik import peserta_didik_export
from .ptk import ptk_export
from .rombongan_belajar import rombongan_belajar_export
from .sekolah import sekolah_export
from .console import cli

__all__ = [
    "pengguna_export",
    "peserta_didik_export",
    "ptk_export",
    "rombongan_belajar_export",
    "sekolah_export",
    "cli",
]

if __name__ == "__main__":
    exit(cli())
