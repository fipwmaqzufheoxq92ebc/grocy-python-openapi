
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.batteries_api import BatteriesApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from grocy.api.batteries_api import BatteriesApi
from grocy.api.calendar_api import CalendarApi
from grocy.api.chores_api import ChoresApi
from grocy.api.current_user_api import CurrentUserApi
from grocy.api.files_api import FilesApi
from grocy.api.generic_entity_interactions_api import GenericEntityInteractionsApi
from grocy.api.print_api import PrintApi
from grocy.api.recipes_api import RecipesApi
from grocy.api.stock_api import StockApi
from grocy.api.stock_by_barcode_api import StockByBarcodeApi
from grocy.api.system_api import SystemApi
from grocy.api.tasks_api import TasksApi
from grocy.api.user_management_api import UserManagementApi
