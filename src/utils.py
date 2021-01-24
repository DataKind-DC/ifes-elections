"""General purpose utilities."""
import pathlib


# The project root directory.
ROOT = pathlib.Path(__file__, "..", "..").resolve()


# Paths to project directories.
PATHS = {
    "raw": ROOT / "data" / "raw",
    "processed": ROOT / "data" / "processed",
}
