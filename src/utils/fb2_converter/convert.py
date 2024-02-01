import subprocess
import platform
from os.path import join
from pathlib import Path

from src.core import settings


def convert(fb_abs_path: str | Path, output_dir: str | Path) -> None:
    system_platform = platform.system()

    if system_platform == "Linux":
        fb2c = "src/utils/fb2_converter/fb2c"
    elif system_platform == "Windows":
        fb2c = "src/utils/fb2_converter/fb2c_win64/fb2converter/fb2c.exe"
    else:
        raise OSError("Unsupported platform")

    fb2c_path = join(
        settings.base_dir,
        fb2c,
    )
    conf_path = join(
        settings.base_dir,
        fb2c,
    )

    command = f"{fb2c_path} -c {conf_path} convert --to epub {fb_abs_path} {output_dir}"
    result = subprocess.run(command)
