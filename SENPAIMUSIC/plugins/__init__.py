import glob
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = []
    for f in mod_paths:
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py"):
            # Normalize path separators and remove the work_dir prefix
            module_path = f.replace(work_dir, "").replace("\\", "/").replace("/", ".")
            # Remove the leading dot and .py extension
            module = module_path[1:-3] if module_path.startswith(".") else module_path[:-3]
            if module:  # Only add non-empty module names
                all_modules.append(module)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
