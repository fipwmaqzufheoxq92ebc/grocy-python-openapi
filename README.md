# grocy
Authentication is done via API keys (header *GROCY-API-KEY* or same named query parameter), which you can manage [here](http://localhost:8111/manageapikeys).<br>Additionally requests from within the frontend are also valid (via session cookie).

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import grocy
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import grocy
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import grocy
from pprint import pprint
from grocy.api import batteries_api
from grocy.model.battery_charge_cycle_entry import BatteryChargeCycleEntry
from grocy.model.battery_details_response import BatteryDetailsResponse
from grocy.model.current_battery_response import CurrentBatteryResponse
from grocy.model.error400 import Error400
from grocy.model.error500 import Error500
from grocy.model.inline_object22 import InlineObject22
# Defining the host is optional and defaults to http://localhost:8111/api
# See configuration.py for a list of all supported configuration parameters.
configuration = grocy.Configuration(
    host = "http://localhost:8111/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'


# Enter a context with an instance of the API client
with grocy.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = batteries_api.BatteriesApi(api_client)
    battery_id = 1 # int | A valid battery id
inline_object22 = InlineObject22(
        tracked_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # InlineObject22 | 

    try:
        # Tracks a charge cycle of the given battery
        api_response = api_instance.batteries_battery_id_charge_post(battery_id, inline_object22)
        pprint(api_response)
    except grocy.ApiException as e:
        print("Exception when calling BatteriesApi->batteries_battery_id_charge_post: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8111/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BatteriesApi* | [**batteries_battery_id_charge_post**](docs/BatteriesApi.md#batteries_battery_id_charge_post) | **POST** /batteries/{batteryId}/charge | Tracks a charge cycle of the given battery
*BatteriesApi* | [**batteries_battery_id_get**](docs/BatteriesApi.md#batteries_battery_id_get) | **GET** /batteries/{batteryId} | Returns details of the given battery
*BatteriesApi* | [**batteries_charge_cycles_charge_cycle_id_undo_post**](docs/BatteriesApi.md#batteries_charge_cycles_charge_cycle_id_undo_post) | **POST** /batteries/charge-cycles/{chargeCycleId}/undo | Undoes a battery charge cycle
*BatteriesApi* | [**batteries_get**](docs/BatteriesApi.md#batteries_get) | **GET** /batteries | Returns all batteries incl. the next estimated charge time per battery
*CalendarApi* | [**calendar_ical_get**](docs/CalendarApi.md#calendar_ical_get) | **GET** /calendar/ical | Returns the calendar in iCal format
*CalendarApi* | [**calendar_ical_sharing_link_get**](docs/CalendarApi.md#calendar_ical_sharing_link_get) | **GET** /calendar/ical/sharing-link | Returns a (public) sharing link for the calendar in iCal format
*ChoresApi* | [**chores_chore_id_execute_post**](docs/ChoresApi.md#chores_chore_id_execute_post) | **POST** /chores/{choreId}/execute | Tracks an execution of the given chore
*ChoresApi* | [**chores_chore_id_get**](docs/ChoresApi.md#chores_chore_id_get) | **GET** /chores/{choreId} | Returns details of the given chore
*ChoresApi* | [**chores_executions_calculate_next_assignments_post**](docs/ChoresApi.md#chores_executions_calculate_next_assignments_post) | **POST** /chores/executions/calculate-next-assignments | (Re)calculates all next user assignments of all chores
*ChoresApi* | [**chores_executions_execution_id_undo_post**](docs/ChoresApi.md#chores_executions_execution_id_undo_post) | **POST** /chores/executions/{executionId}/undo | Undoes a chore execution
*ChoresApi* | [**chores_get**](docs/ChoresApi.md#chores_get) | **GET** /chores | Returns all chores incl. the next estimated execution time per chore
*CurrentUserApi* | [**user_get**](docs/CurrentUserApi.md#user_get) | **GET** /user | Returns the currently authenticated user
*CurrentUserApi* | [**user_settings_get**](docs/CurrentUserApi.md#user_settings_get) | **GET** /user/settings | Returns all settings of the currently logged in user
*CurrentUserApi* | [**user_settings_setting_key_delete**](docs/CurrentUserApi.md#user_settings_setting_key_delete) | **DELETE** /user/settings/{settingKey} | Deletes the given setting of the currently logged in user
*CurrentUserApi* | [**user_settings_setting_key_get**](docs/CurrentUserApi.md#user_settings_setting_key_get) | **GET** /user/settings/{settingKey} | Returns the given setting of the currently logged in user
*CurrentUserApi* | [**user_settings_setting_key_put**](docs/CurrentUserApi.md#user_settings_setting_key_put) | **PUT** /user/settings/{settingKey} | Sets the given setting of the currently logged in user
*FilesApi* | [**files_group_file_name_delete**](docs/FilesApi.md#files_group_file_name_delete) | **DELETE** /files/{group}/{fileName} | Deletes the given file
*FilesApi* | [**files_group_file_name_get**](docs/FilesApi.md#files_group_file_name_get) | **GET** /files/{group}/{fileName} | Serves the given file
*FilesApi* | [**files_group_file_name_put**](docs/FilesApi.md#files_group_file_name_put) | **PUT** /files/{group}/{fileName} | Uploads a single file
*GenericEntityInteractionsApi* | [**objects_entity_get**](docs/GenericEntityInteractionsApi.md#objects_entity_get) | **GET** /objects/{entity} | Returns all objects of the given entity
*GenericEntityInteractionsApi* | [**objects_entity_object_id_delete**](docs/GenericEntityInteractionsApi.md#objects_entity_object_id_delete) | **DELETE** /objects/{entity}/{objectId} | Deletes a single object of the given entity
*GenericEntityInteractionsApi* | [**objects_entity_object_id_get**](docs/GenericEntityInteractionsApi.md#objects_entity_object_id_get) | **GET** /objects/{entity}/{objectId} | Returns a single object of the given entity
*GenericEntityInteractionsApi* | [**objects_entity_object_id_put**](docs/GenericEntityInteractionsApi.md#objects_entity_object_id_put) | **PUT** /objects/{entity}/{objectId} | Edits the given object of the given entity
*GenericEntityInteractionsApi* | [**objects_entity_post**](docs/GenericEntityInteractionsApi.md#objects_entity_post) | **POST** /objects/{entity} | Adds a single object of the given entity
*GenericEntityInteractionsApi* | [**userfields_entity_object_id_get**](docs/GenericEntityInteractionsApi.md#userfields_entity_object_id_get) | **GET** /userfields/{entity}/{objectId} | Returns all userfields with their values of the given object of the given entity
*GenericEntityInteractionsApi* | [**userfields_entity_object_id_put**](docs/GenericEntityInteractionsApi.md#userfields_entity_object_id_put) | **PUT** /userfields/{entity}/{objectId} | Edits the given userfields of the given object of the given entity
*PrintApi* | [**print_shoppinglist_thermal_get**](docs/PrintApi.md#print_shoppinglist_thermal_get) | **GET** /print/shoppinglist/thermal | Prints the shoppinglist with a thermal printer
*RecipesApi* | [**recipes_fulfillment_get**](docs/RecipesApi.md#recipes_fulfillment_get) | **GET** /recipes/fulfillment | Get stock fulfillment information for all recipe
*RecipesApi* | [**recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post**](docs/RecipesApi.md#recipes_recipe_id_add_not_fulfilled_products_to_shoppinglist_post) | **POST** /recipes/{recipeId}/add-not-fulfilled-products-to-shoppinglist | Adds all missing products for the given recipe to the shopping list
*RecipesApi* | [**recipes_recipe_id_consume_post**](docs/RecipesApi.md#recipes_recipe_id_consume_post) | **POST** /recipes/{recipeId}/consume | Consumes all products of the given recipe
*RecipesApi* | [**recipes_recipe_id_fulfillment_get**](docs/RecipesApi.md#recipes_recipe_id_fulfillment_get) | **GET** /recipes/{recipeId}/fulfillment | Get stock fulfillment information for the given recipe
*StockApi* | [**stock_barcodes_external_lookup_barcode_get**](docs/StockApi.md#stock_barcodes_external_lookup_barcode_get) | **GET** /stock/barcodes/external-lookup/{barcode} | Executes an external barcode lookoup via the configured plugin with the given barcode
*StockApi* | [**stock_bookings_booking_id_get**](docs/StockApi.md#stock_bookings_booking_id_get) | **GET** /stock/bookings/{bookingId} | Returns the given stock booking
*StockApi* | [**stock_bookings_booking_id_undo_post**](docs/StockApi.md#stock_bookings_booking_id_undo_post) | **POST** /stock/bookings/{bookingId}/undo | Undoes a booking
*StockApi* | [**stock_entry_entry_id_get**](docs/StockApi.md#stock_entry_entry_id_get) | **GET** /stock/entry/{entryId} | Returns details of the given stock
*StockApi* | [**stock_entry_entry_id_printlabel_get**](docs/StockApi.md#stock_entry_entry_id_printlabel_get) | **GET** /stock/entry/{entryId}/printlabel | Prints the label of the given stock entry
*StockApi* | [**stock_entry_entry_id_put**](docs/StockApi.md#stock_entry_entry_id_put) | **PUT** /stock/entry/{entryId} | Edits the stock entry
*StockApi* | [**stock_get**](docs/StockApi.md#stock_get) | **GET** /stock | Returns all products which are currently in stock incl. the next due date per product
*StockApi* | [**stock_products_product_id_add_post**](docs/StockApi.md#stock_products_product_id_add_post) | **POST** /stock/products/{productId}/add | Adds the given amount of the given product to stock
*StockApi* | [**stock_products_product_id_consume_post**](docs/StockApi.md#stock_products_product_id_consume_post) | **POST** /stock/products/{productId}/consume | Removes the given amount of the given product from stock
*StockApi* | [**stock_products_product_id_entries_get**](docs/StockApi.md#stock_products_product_id_entries_get) | **GET** /stock/products/{productId}/entries | Returns all stock entries of the given product in order of next use (Opened first, then first due first, then first in first out)
*StockApi* | [**stock_products_product_id_get**](docs/StockApi.md#stock_products_product_id_get) | **GET** /stock/products/{productId} | Returns details of the given product
*StockApi* | [**stock_products_product_id_inventory_post**](docs/StockApi.md#stock_products_product_id_inventory_post) | **POST** /stock/products/{productId}/inventory | Inventories the given product (adds/removes based on the given new amount)
*StockApi* | [**stock_products_product_id_locations_get**](docs/StockApi.md#stock_products_product_id_locations_get) | **GET** /stock/products/{productId}/locations | Returns all locations where the given product currently has stock
*StockApi* | [**stock_products_product_id_open_post**](docs/StockApi.md#stock_products_product_id_open_post) | **POST** /stock/products/{productId}/open | Marks the given amount of the given product as opened
*StockApi* | [**stock_products_product_id_price_history_get**](docs/StockApi.md#stock_products_product_id_price_history_get) | **GET** /stock/products/{productId}/price-history | Returns the price history of the given product
*StockApi* | [**stock_products_product_id_printlabel_get**](docs/StockApi.md#stock_products_product_id_printlabel_get) | **GET** /stock/products/{productId}/printlabel | Prints the product label of the given product
*StockApi* | [**stock_products_product_id_to_keep_merge_product_id_to_remove_post**](docs/StockApi.md#stock_products_product_id_to_keep_merge_product_id_to_remove_post) | **POST** /stock/products/{productIdToKeep}/merge/{productIdToRemove} | Merges two products into one
*StockApi* | [**stock_products_product_id_transfer_post**](docs/StockApi.md#stock_products_product_id_transfer_post) | **POST** /stock/products/{productId}/transfer | Transfers the given amount of the given product from one location to another (this is currently not supported for tare weight handling enabled products)
*StockApi* | [**stock_shoppinglist_add_expired_products_post**](docs/StockApi.md#stock_shoppinglist_add_expired_products_post) | **POST** /stock/shoppinglist/add-expired-products | Adds expired products to the given shopping list
*StockApi* | [**stock_shoppinglist_add_missing_products_post**](docs/StockApi.md#stock_shoppinglist_add_missing_products_post) | **POST** /stock/shoppinglist/add-missing-products | Adds currently missing products (below defined min. stock amount) to the given shopping list
*StockApi* | [**stock_shoppinglist_add_overdue_products_post**](docs/StockApi.md#stock_shoppinglist_add_overdue_products_post) | **POST** /stock/shoppinglist/add-overdue-products | Adds overdue products to the given shopping list
*StockApi* | [**stock_shoppinglist_add_product_post**](docs/StockApi.md#stock_shoppinglist_add_product_post) | **POST** /stock/shoppinglist/add-product | Adds the given amount of the given product to the given shopping list
*StockApi* | [**stock_shoppinglist_clear_post**](docs/StockApi.md#stock_shoppinglist_clear_post) | **POST** /stock/shoppinglist/clear | Removes all items from the given shopping list
*StockApi* | [**stock_shoppinglist_remove_product_post**](docs/StockApi.md#stock_shoppinglist_remove_product_post) | **POST** /stock/shoppinglist/remove-product | Removes the given amount of the given product from the given shopping list, if it is on it
*StockApi* | [**stock_transactions_transaction_id_get**](docs/StockApi.md#stock_transactions_transaction_id_get) | **GET** /stock/transactions/{transactionId} | Returns all stock bookings of the given transaction id
*StockApi* | [**stock_transactions_transaction_id_undo_post**](docs/StockApi.md#stock_transactions_transaction_id_undo_post) | **POST** /stock/transactions/{transactionId}/undo | Undoes a transaction
*StockApi* | [**stock_volatile_get**](docs/StockApi.md#stock_volatile_get) | **GET** /stock/volatile | Returns all products which are due soon, overdue, expired or currently missing
*StockByBarcodeApi* | [**stock_products_by_barcode_barcode_add_post**](docs/StockByBarcodeApi.md#stock_products_by_barcode_barcode_add_post) | **POST** /stock/products/by-barcode/{barcode}/add | Adds the given amount of the by its barcode given product to stock
*StockByBarcodeApi* | [**stock_products_by_barcode_barcode_consume_post**](docs/StockByBarcodeApi.md#stock_products_by_barcode_barcode_consume_post) | **POST** /stock/products/by-barcode/{barcode}/consume | Removes the given amount of the by its barcode given product from stock
*StockByBarcodeApi* | [**stock_products_by_barcode_barcode_get**](docs/StockByBarcodeApi.md#stock_products_by_barcode_barcode_get) | **GET** /stock/products/by-barcode/{barcode} | Returns details of the given product by its barcode
*StockByBarcodeApi* | [**stock_products_by_barcode_barcode_inventory_post**](docs/StockByBarcodeApi.md#stock_products_by_barcode_barcode_inventory_post) | **POST** /stock/products/by-barcode/{barcode}/inventory | Inventories the by its barcode given product (adds/removes based on the given new amount)
*StockByBarcodeApi* | [**stock_products_by_barcode_barcode_open_post**](docs/StockByBarcodeApi.md#stock_products_by_barcode_barcode_open_post) | **POST** /stock/products/by-barcode/{barcode}/open | Marks the given amount of the by its barcode given product as opened
*StockByBarcodeApi* | [**stock_products_by_barcode_barcode_transfer_post**](docs/StockByBarcodeApi.md#stock_products_by_barcode_barcode_transfer_post) | **POST** /stock/products/by-barcode/{barcode}/transfer | Transfers the given amount of the by its barcode given product from one location to another (this is currently not supported for tare weight handling enabled products)
*SystemApi* | [**system_config_get**](docs/SystemApi.md#system_config_get) | **GET** /system/config | Returns all config settings
*SystemApi* | [**system_db_changed_time_get**](docs/SystemApi.md#system_db_changed_time_get) | **GET** /system/db-changed-time | Returns the time when the database was last changed
*SystemApi* | [**system_info_get**](docs/SystemApi.md#system_info_get) | **GET** /system/info | Returns information about the installed grocy, PHP and SQLite version
*SystemApi* | [**system_log_missing_localization_post**](docs/SystemApi.md#system_log_missing_localization_post) | **POST** /system/log-missing-localization | Logs a missing localization string
*SystemApi* | [**system_time_get**](docs/SystemApi.md#system_time_get) | **GET** /system/time | Returns the current server time
*TasksApi* | [**tasks_get**](docs/TasksApi.md#tasks_get) | **GET** /tasks | Returns all tasks which are not done yet
*TasksApi* | [**tasks_task_id_complete_post**](docs/TasksApi.md#tasks_task_id_complete_post) | **POST** /tasks/{taskId}/complete | Marks the given task as completed
*TasksApi* | [**tasks_task_id_undo_post**](docs/TasksApi.md#tasks_task_id_undo_post) | **POST** /tasks/{taskId}/undo | Marks the given task as not completed
*UserManagementApi* | [**users_get**](docs/UserManagementApi.md#users_get) | **GET** /users | Returns all users
*UserManagementApi* | [**users_post**](docs/UserManagementApi.md#users_post) | **POST** /users | Creates a new user
*UserManagementApi* | [**users_user_id_delete**](docs/UserManagementApi.md#users_user_id_delete) | **DELETE** /users/{userId} | Deletes the given user
*UserManagementApi* | [**users_user_id_permissions_get**](docs/UserManagementApi.md#users_user_id_permissions_get) | **GET** /users/{userId}/permissions | Returns the assigned permissions of the given user
*UserManagementApi* | [**users_user_id_permissions_post**](docs/UserManagementApi.md#users_user_id_permissions_post) | **POST** /users/{userId}/permissions | Adds a permission to the given user
*UserManagementApi* | [**users_user_id_permissions_put**](docs/UserManagementApi.md#users_user_id_permissions_put) | **PUT** /users/{userId}/permissions | Replaces the assigned permissions of the given user
*UserManagementApi* | [**users_user_id_put**](docs/UserManagementApi.md#users_user_id_put) | **PUT** /users/{userId} | Edits the given user


## Documentation For Models

 - [ApiKey](docs/ApiKey.md)
 - [Battery](docs/Battery.md)
 - [BatteryChargeCycleEntry](docs/BatteryChargeCycleEntry.md)
 - [BatteryDetailsResponse](docs/BatteryDetailsResponse.md)
 - [Chore](docs/Chore.md)
 - [ChoreDetailsResponse](docs/ChoreDetailsResponse.md)
 - [ChoreLogEntry](docs/ChoreLogEntry.md)
 - [CurrentBatteryResponse](docs/CurrentBatteryResponse.md)
 - [CurrentChoreResponse](docs/CurrentChoreResponse.md)
 - [CurrentStockResponse](docs/CurrentStockResponse.md)
 - [CurrentVolatilStockResponse](docs/CurrentVolatilStockResponse.md)
 - [DbChangedTimeResponse](docs/DbChangedTimeResponse.md)
 - [Error400](docs/Error400.md)
 - [Error500](docs/Error500.md)
 - [Error500ErrorDetails](docs/Error500ErrorDetails.md)
 - [ExposedEntity](docs/ExposedEntity.md)
 - [ExposedEntityEditRequiresAdmin](docs/ExposedEntityEditRequiresAdmin.md)
 - [ExposedEntityNoDelete](docs/ExposedEntityNoDelete.md)
 - [ExposedEntityNoEdit](docs/ExposedEntityNoEdit.md)
 - [ExposedEntityNoListing](docs/ExposedEntityNoListing.md)
 - [ExposedEntityNotIncludingNotDeletable](docs/ExposedEntityNotIncludingNotDeletable.md)
 - [ExposedEntityNotIncludingNotEditable](docs/ExposedEntityNotIncludingNotEditable.md)
 - [ExposedEntityNotIncludingNotListable](docs/ExposedEntityNotIncludingNotListable.md)
 - [ExternalBarcodeLookupResponse](docs/ExternalBarcodeLookupResponse.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject10](docs/InlineObject10.md)
 - [InlineObject11](docs/InlineObject11.md)
 - [InlineObject12](docs/InlineObject12.md)
 - [InlineObject13](docs/InlineObject13.md)
 - [InlineObject14](docs/InlineObject14.md)
 - [InlineObject15](docs/InlineObject15.md)
 - [InlineObject16](docs/InlineObject16.md)
 - [InlineObject17](docs/InlineObject17.md)
 - [InlineObject18](docs/InlineObject18.md)
 - [InlineObject19](docs/InlineObject19.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject20](docs/InlineObject20.md)
 - [InlineObject21](docs/InlineObject21.md)
 - [InlineObject22](docs/InlineObject22.md)
 - [InlineObject23](docs/InlineObject23.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineObject5](docs/InlineObject5.md)
 - [InlineObject6](docs/InlineObject6.md)
 - [InlineObject7](docs/InlineObject7.md)
 - [InlineObject8](docs/InlineObject8.md)
 - [InlineObject9](docs/InlineObject9.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse200GrocyVersion](docs/InlineResponse200GrocyVersion.md)
 - [Location](docs/Location.md)
 - [MissingLocalizationRequest](docs/MissingLocalizationRequest.md)
 - [Product](docs/Product.md)
 - [ProductBarcode](docs/ProductBarcode.md)
 - [ProductDetailsResponse](docs/ProductDetailsResponse.md)
 - [ProductPriceHistory](docs/ProductPriceHistory.md)
 - [QuantityUnit](docs/QuantityUnit.md)
 - [RecipeFulfillmentResponse](docs/RecipeFulfillmentResponse.md)
 - [Session](docs/Session.md)
 - [ShoppingListItem](docs/ShoppingListItem.md)
 - [ShoppingLocation](docs/ShoppingLocation.md)
 - [StockEntry](docs/StockEntry.md)
 - [StockJournal](docs/StockJournal.md)
 - [StockJournalSummary](docs/StockJournalSummary.md)
 - [StockLocation](docs/StockLocation.md)
 - [StockLogEntry](docs/StockLogEntry.md)
 - [StockTransactionType](docs/StockTransactionType.md)
 - [Task](docs/Task.md)
 - [TimeResponse](docs/TimeResponse.md)
 - [User](docs/User.md)
 - [UserDto](docs/UserDto.md)
 - [UserSetting](docs/UserSetting.md)


## Documentation For Authorization


## ApiKeyAuth

- **Type**: API key
- **API key parameter name**: GROCY-API-KEY
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in grocy.apis and grocy.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from grocy.api.default_api import DefaultApi`
- `from grocy.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import grocy
from grocy.apis import *
from grocy.models import *
```

