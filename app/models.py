from pydantic import BaseModel


class Campaign(BaseModel):
    campaign_id: str
    source: str
    geo: str
    clicks: int
    registrations: int
    first_time_deposits: int
    cost: float
    revenue: float


class CampaignMetrics(BaseModel):
    campaign_id: str
    source: str
    geo: str
    click_to_registration_rate: float
    registration_to_deposit_rate: float
    revenue_per_click: float
    roi_percent: float
    suspicious_signal: bool
