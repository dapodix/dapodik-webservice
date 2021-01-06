import click
from sys import exit
from typing import List


from dapodik_webservice import __version__
from dapodik_webservice import DapodikWebservice
from . import (
    pengguna_export,
    peserta_didik_export,
    ptk_export,
    rombongan_belajar_export,
    sekolah_export,
)
from .util import makefilepath


class CustomContext(click.Context):
    obj: DapodikWebservice


@click.group(
    "versi",
    invoke_without_command=True,
    help="Tampilkan versi",
)
def versi():
    print("dapodik-webservice")
    print(f"Versi : {__version__}")


@click.group(
    "export",
    invoke_without_command=True,
    help="Export data ke excel",
)
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.pass_context
def export(ctx: CustomContext, url: str, token: str, npsn: str):
    ctx.ensure_object(DapodikWebservice)
    ctx.obj = DapodikWebservice(token, npsn, url)


@export.command("pengguna", help="Export data Pengguna ke excel")
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.argument("namafile", required=False, nargs=-1, default=None)
@click.pass_context
def export_pengguna(
    ctx: CustomContext,
    url: str,
    token: str,
    npsn: str,
    namafile: List[str],
):
    click.echo("Mengeksport data pengguna...")
    dapodik = ctx.obj or DapodikWebservice(token, npsn, url)
    pengguna = dapodik.pengguna
    if pengguna:
        namafile = namafile or [npsn]
        for nama in namafile:
            filepath = makefilepath(nama)
            wb, ws = pengguna_export(pengguna, filepath)
            wb.save(filepath)
    else:
        click.echo("Data pengguna kosong!")


@export.command("peserta-didik", help="Export data Peserta didik ke excel")
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.argument("namafile", required=False, nargs=-1, default=None)
@click.pass_context
def export_peserta_didik(
    ctx: CustomContext,
    url: str,
    token: str,
    npsn: str,
    namafile: List[str],
):
    click.echo("Mengeksport data peserta didik...")
    dapodik = ctx.obj or DapodikWebservice(token, npsn, url)
    peserta_didik = dapodik.peserta_didik
    if peserta_didik:
        namafile = namafile or [npsn]
        for nama in namafile:
            filepath = makefilepath(nama)
            wb, ws = peserta_didik_export(peserta_didik, filepath)
            wb.save(filepath)
            click.echo(
                f"Berhasil menyimpan data peserta didik sebanyak {len(peserta_didik)} di {filepath}"
            )
    else:
        click.echo("Data peserta didik kosong!")


@export.command("ptk", help="Export data Ptk ke excel")
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.argument("namafile", required=False, nargs=-1, default=None)
@click.pass_context
def export_ptk(
    ctx: CustomContext,
    url: str,
    token: str,
    npsn: str,
    namafile: List[str],
):
    click.echo("Mengeksport data ptk...")
    dapodik = ctx.obj or DapodikWebservice(token, npsn, url)
    ptk = dapodik.ptk
    if ptk:
        namafile = namafile or [npsn]
        for nama in namafile:
            filepath = makefilepath(nama)
            wb, ws = ptk_export(ptk, filepath)
            wb.save(filepath)
            click.echo(f"Berhasil menyimpan data ptk sebanyak {len(ptk)} di {filepath}")
    else:
        click.echo("Data ptk kosong!")


@export.command("rombongan-belajar", help="Export data Rombongan belajar ke excel")
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.argument("namafile", required=False, nargs=-1, default=None)
@click.pass_context
def export_rombongan_belajar(
    ctx: CustomContext,
    url: str,
    token: str,
    npsn: str,
    namafile: List[str],
):
    click.echo("Mengeksport data rombongan belajar...")
    dapodik = ctx.obj or DapodikWebservice(token, npsn, url)
    rombongan_belajar = dapodik.rombongan_belajar
    if rombongan_belajar:
        namafile = namafile or [npsn]
        for nama in namafile:
            filepath = makefilepath(nama)
            wb, ws = rombongan_belajar_export(rombongan_belajar, filepath)
            wb.save(filepath)
            click.echo(
                f"Berhasil menyimpan data rombongan belajar sebanyak {len(rombongan_belajar)} di {filepath}"
            )
    else:
        click.echo("Data rombongan belajar kosong!")


@export.command("sekolah", help="Export data Sekolah ke excel")
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.argument("namafile", required=False, nargs=-1, default=None)
@click.pass_context
def export_sekolah(
    ctx: CustomContext,
    url: str,
    token: str,
    npsn: str,
    namafile: List[str],
):
    click.echo("Mengeksport data sekolah...")
    dapodik = ctx.obj or DapodikWebservice(token, npsn, url)
    sekolah = dapodik.sekolah
    if sekolah:
        namafile = namafile or [npsn]
        for nama in namafile:
            filepath = makefilepath(nama)
            wb, ws = sekolah_export(sekolah, filepath)
            wb.save(filepath)
            click.echo(f"Berhasil menyimpan data sekolah di {filepath}")
    else:
        click.echo("Data sekolah kosong!")


@export.command("semua", help="Export semua data ke excel")
@click.option(
    "--url", required=False, default="http://localhost:5774", help="URL server dapodik"
)
@click.option("--token", required=True, help="Token webservice dapodik")
@click.option("--npsn", required=True, help="NPSN sekolah")
@click.argument("namafile", required=False, nargs=-1, default=None)
@click.pass_context
def export_semua(
    ctx: CustomContext,
    url: str,
    token: str,
    npsn: str,
    namafile: List[str],
):
    click.echo("Mengeksport semua data...")
    ctx.forward(export_sekolah)
    ctx.forward(export_peserta_didik)
    ctx.forward(export_ptk)
    ctx.forward(export_rombongan_belajar)
    ctx.forward(export_pengguna)
    click.echo("Berhasil semua data...")


cli = click.CommandCollection(
    name="dapodik-webservice",
    sources=[versi, export],
)

if __name__ == "__main__":
    exit(cli())
