from typing import Any

from custom_components.ecoflow_cloud_resilient.api import EcoflowApiClient
from custom_components.ecoflow_cloud_resilient.devices.internal.river2_max import River2Max as InternalRiver2Max
from custom_components.ecoflow_cloud_resilient.devices.public.data_bridge import to_plain
from custom_components.ecoflow_cloud_resilient.sensor import QuotaStatusSensorEntity


class River2Max(InternalRiver2Max):
    def _prepare_data(self, raw_data) -> dict[str, Any]:
        res = super()._prepare_data(raw_data)
        res = to_plain(res)
        return res

    def _status_sensor(self, client: EcoflowApiClient) -> QuotaStatusSensorEntity:
        return QuotaStatusSensorEntity(client, self)
