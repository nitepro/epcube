DOMAIN = "epcube"
DEFAULT_SCAN_INTERVAL = 5
PLATFORMS = ["sensor", "select", "number"]

CONF_SCALE_POWER = "scale_power"

CONF_ENABLE_TOTAL = "enable_total"
CONF_ENABLE_ANNUAL = "enable_annual"
CONF_ENABLE_MONTHLY = "enable_monthly"


BASE_URLS = {
    "EU": "https://monitoring-eu.epcube.com/api",
    "US": "https://monitoring-us.epcube.com/v1/api",
    "JP": "https://monitoring-jp.epcube.com/api"
}

def get_base_url(region: str) -> str:
    return BASE_URLS.get(region.upper(), BASE_URLS["EU"])
