from src.utils.get_value import get_value
import subprocess


class Default:

    @staticmethod
    async def install(args, context=None, process=None, item=None):
        package_name = await get_value(args.get("source"), context, process, item)

        try:
            # Run the pip install command
            subprocess.check_call(['pip', 'install', package_name])
            return True
        except subprocess.CalledProcessError as e:
            return f"An error occurred while installing {package_name}: {e}"
