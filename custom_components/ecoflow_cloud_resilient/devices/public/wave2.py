from custom_components.ecoflow_cloud_resilient.devices.public.data_bridge import to_plain
from typing import Any
from custom_components.ecoflow_cloud_resilient.devices.internal.wave2 import Wave2 as InternalWave2
from custom_components.ecoflow_cloud_resilient.api import EcoflowApiClient
from custom_components.ecoflow_cloud_resilient.sensor import QuotaStatusSensorEntity


class Wave2(InternalWave2):
    def _prepare_data(self, raw_data) -> dict[str, Any]:
        res = super()._prepare_data(raw_data)
        res = to_plain(res)
        return res

    def _status_sensor(self, client: EcoflowApiClient) -> QuotaStatusSensorEntity:
        return QuotaStatusSensorEntity(client, self)
