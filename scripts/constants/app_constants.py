baseServiceUrl = '/userManagement'
from scripts.constants import app_configuration

class UserManagement:
    add_user = '/addUser'
    edit_user = 'editUser'
    delete_user = '/deleteUser'
    deactivate_user = '/deActivateUser'
    activate_user = '/activateUser'
    login_check_request = '/login'
    logout_user = '/logoutUser'
    add_tab = '/addSettingTab'
    fetch_tab_data = '/fetchSettingTabData'
    fetch_tab_header_data = '/fetchTabHeaderData'
    diseases_list = '/diseasesList'
    market_trend = '/marketTrend'
    customer_wise_sales = '/customerWiseSales'
    chick_trend = '/chickTrend'
    get_side_bar_data = '/getSideBarData'

    # Setting Tabs Save
    save_bird_price = '/birdsPriceData'
    save_hens_availability = '/hensAvailabilityData'
    sheds_availability = '/shedsData'
    order_hens_data = '/orderHensData'
    sales_data = '/salesData'
    feed_consumption_data = '/feedConsumptionData'
    user_setup_data = '/userSetupData'
    sheds_data='/shedsData'
    order_hens_data='/orderHensData'
    chick_price_data='/chickPriceData'
    mortality_data='/mortalityData'
    diseases_data='/diseasesData'

    # Setting Tables
    feed_consumption_table_data = '/feedConsumptionTableData'
    user_setup_table_data = '/userSetupTableData'
    sheds_table_data = '/shedsTableData'
    sales_table_data = '/salesTableData'
    order_hens_table_data = '/orderHensTableData'
    birds_price_table_data = '/birdsPriceTableData'
    chick_price_table_data = '/chickPriceTableData'
    mortality_table_data = '/mortalityTableData'
    diseases_table_data = '/diseasesTableData'
    blockedUsers_table_data = '/blockedUsersTableData'
    dashboard_table_data = '/dashboardTableData'
    get_user_role_page_data = '/getUserRolePageData'
    set_user_role_page_data = '/setUserRolePageData'
    push_notification = '/pushNotification'

    # SettingsTabDelete
    delete_settings_tab_details = '/deleteSettingsTabDetails'
    unblock_user = '/unBlockUser'






settingsTabMapping = {
    'birdsPrice': app_configuration.BIRD_PRICE_COLLECTION,
    'chickPrice': app_configuration.CHICK_PRICE_COLLECTION,
    'diseases': app_configuration.DISEASES_COLLECTION,
    'feedConsumption': app_configuration.FEED_CONSUMPTION_COLLECTION,
    'feedPrice': '',
    'hensAvailability': app_configuration.HENS_AVAILABILITY_COLLECTION,
    'mortality': app_configuration.MORTALITY_COLLECTION,
    'notifications': '',
    'orderHens': app_configuration.ORDER_HENS_COLLECTION,
    'sales': app_configuration.SALES_COLLECTION,
    'sheds': app_configuration.SHEDS_COLLECTION,
    'userSetup': app_configuration.MONGO_COLLECTION,
    'userRoleSetup': app_configuration.USER_ACCESS_COLLECTION
}
settingsKeyMapping = {
    'birdsPrice': 'date',
    'chickPrice': 'date',
    'diseases': 'diseaseName',
    'feedConsumption': 'batchNo',
    'feedPrice': 'date',
    'hensAvailability': 'date',
    'mortality': 'batchNo',
    'notifications': '',
    'orderHens': 'date',
    'sales': 'userName',
    'sheds': 'shedName',
    'userSetup': 'userName',
    'userRoleSetup': ''
}
VAPID_PRIVATE_KEY = "2RyMboKl-JflKcZSBFx7_t13cAhYdSKw6NCOP_m2n9s"
VAPID_PUBLIC_KEY = "BCTeAlAt_DnLbz7ka22t4DARmnUq7Ts0NxYNYgVPVgym77Y8b82U9EqDTbabwIZWmtGV510xJ07E_vtAY7tCg34"

VAPID_CLAIMS = {
    "sub": "mailto:reddyarunkumar807@gmail.com"
}
