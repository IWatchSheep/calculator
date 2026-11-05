"""Shared test package configuration and headless virtual display support."""
import os
import shutil
import subprocess

_virtual_display = None


def setUpModule():
    """Start a virtual display on headless Linux/POSIX systems if no display is active."""
    global _virtual_display
    if os.name == "posix" and not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
        try:
            from pyvirtualdisplay import Display
            _virtual_display = Display(visible=False, size=(1024, 768))
            _virtual_display.start()
        except Exception:
            if shutil.which("Xvfb"):
                try:
                    for disp_num in range(99, 110):
                        disp_str = f":{disp_num}"
                        if not os.path.exists(f"/tmp/.X11-unix/X{disp_num}"):
                            proc = subprocess.Popen(
                                ["Xvfb", disp_str, "-screen", "0", "1024x768x24"],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                            )
                            os.environ["DISPLAY"] = disp_str
                            _virtual_display = proc
                            break
                except Exception:
                    pass


def tearDownModule():
    """Clean up virtual display if one was started."""
    global _virtual_display
    if _virtual_display is not None:
        try:
            if hasattr(_virtual_display, "stop"):
                _virtual_display.stop()
            elif hasattr(_virtual_display, "terminate"):
                _virtual_display.terminate()
                _virtual_display.wait(timeout=2)
        except Exception:
            pass
        _virtual_display = None
